"""
Generate docs/privacy.html from PRIVACY_POLICY.md.

The policy is written once, as markdown, and the published page is generated
from it -- so the page the Microsoft Store reviewer reads cannot drift away from
the one that ships inside the app.

No dependencies on purpose: this has to keep working on a bare Python install
years from now. It handles only the markdown the policy actually uses
(headings, bold, inline code, italics, bullet lists, paragraphs).

    python build.py
"""

import html
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / "PRIVACY_POLICY.md"
OUTPUT = ROOT / "docs" / "privacy.html"

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Privacy policy for CorrecTMe, a Windows utility that corrects text typed in the wrong keyboard layout.">
<style>
  :root {{
    --bg: #ffffff;
    --fg: #1f2328;
    --muted: #59636e;
    --rule: #d8dee4;
    --accent: #0969da;
    --code-bg: #f6f8fa;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #0d1117;
      --fg: #e6edf3;
      --muted: #9198a1;
      --rule: #30363d;
      --accent: #4493f8;
      --code-bg: #161b22;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--fg);
    font: 16px/1.65 -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    -webkit-text-size-adjust: 100%;
  }}
  main {{ max-width: 46rem; margin: 0 auto; padding: 3rem 16px 5rem; }}
  h1 {{ font-size: 1.9rem; line-height: 1.25; margin: 0 0 .4rem; letter-spacing: -.01em; }}
  h2 {{
    font-size: 1.25rem; margin: 2.4rem 0 .8rem; padding-bottom: .35rem;
    border-bottom: 1px solid var(--rule);
  }}
  h3 {{ font-size: 1.05rem; margin: 1.8rem 0 .6rem; }}
  p, li {{ margin: 0 0 .9rem; }}
  ul {{ padding-left: 1.4rem; }}
  li {{ margin-bottom: .55rem; }}
  code {{
    background: var(--code-bg); border-radius: 6px; padding: .15em .4em;
    font: .88em/1 ui-monospace, SFMono-Regular, Consolas, monospace;
    overflow-wrap: anywhere;
  }}
  a {{ color: var(--accent); }}
  em.updated {{ display: block; color: var(--muted); font-style: normal; font-size: .9rem; margin-bottom: 2rem; }}
  footer {{ margin-top: 3.5rem; padding-top: 1rem; border-top: 1px solid var(--rule); color: var(--muted); font-size: .875rem; }}
</style>
</head>
<body>
<main>
{body}
<footer>Generated from <code>PRIVACY_POLICY.md</code> on {built}. The same policy ships inside the app.</footer>
</main>
</body>
</html>
"""


def inline(text: str) -> str:
    """Escape, then apply the inline markdown the policy uses."""
    out = html.escape(text, quote=False)
    out = re.sub(r'`([^`]+)`', r'<code>\1</code>', out)
    out = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', out)
    out = re.sub(r'(?<![\w_])_([^_]+)_(?![\w_])', r'<em>\1</em>', out)
    return out


def convert(markdown: str) -> str:
    """Markdown -> HTML for the subset the policy uses."""
    blocks = []
    paragraph: list = []
    bullets: list = []

    def flush_paragraph():
        if paragraph:
            text = inline(' '.join(paragraph))
            # The "Last updated" line is styled rather than run as body text.
            if text.startswith('<em>Last updated'):
                blocks.append('<em class="updated">%s</em>'
                              % re.sub(r'</?em>', '', text))
            else:
                blocks.append('<p>%s</p>' % text)
            paragraph.clear()

    def flush_bullets():
        if bullets:
            items = ''.join('<li>%s</li>' % inline(b) for b in bullets)
            blocks.append('<ul>%s</ul>' % items)
            bullets.clear()

    for raw in markdown.splitlines():
        line = raw.rstrip()

        if not line.strip():
            flush_paragraph()
            flush_bullets()
            continue

        heading = re.match(r'^(#{1,6})\s+(.*)$', line)
        if heading:
            flush_paragraph()
            flush_bullets()
            level = len(heading.group(1))
            blocks.append('<h%d>%s</h%d>' % (level, inline(heading.group(2)), level))
            continue

        bullet = re.match(r'^[-*]\s+(.*)$', line)
        if bullet:
            flush_paragraph()
            bullets.append(bullet.group(1))
            continue

        # An indented line continues the bullet or paragraph above it.
        if raw.startswith(('  ', '\t')) and bullets:
            bullets[-1] += ' ' + line.strip()
            continue

        flush_bullets()
        paragraph.append(line.strip())

    flush_paragraph()
    flush_bullets()
    return '\n'.join(blocks)


def main() -> None:
    markdown = SOURCE.read_text(encoding='utf-8')
    first_heading = re.search(r'^#\s+(.*)$', markdown, re.M)
    title = first_heading.group(1).replace('—', '-') if first_heading else 'Privacy Policy'

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        PAGE.format(title=html.escape(title),
                    body=convert(markdown),
                    built=date.today().isoformat()),
        encoding='utf-8')
    print("wrote %s (%d bytes)" % (OUTPUT, OUTPUT.stat().st_size))


if __name__ == '__main__':
    main()
