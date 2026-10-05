# CorrecTMe — public pages

The public site for [CorrecTMe](https://github.com/IdoAmrani1/CorectMe54), a
Windows app that corrects text typed in the wrong keyboard layout.

**This repo is public on purpose, and holds no source code.** The Microsoft
Store requires a privacy policy at a publicly reachable URL (Store policy
10.5.1) for any app that can access personal information — which applies to
CorrecTMe whether or not data ever leaves the device, and it never does. The app
itself stays in a private repo.

## Pages

| Page | URL |
|---|---|
| Landing page | `https://idoamrani1.github.io/correctme/` |
| Privacy policy | `https://idoamrani1.github.io/correctme/privacy.html` |

The privacy policy URL is the one to paste into the Partner Center submission.

## Editing the policy

`PRIVACY_POLICY.md` is the source. `docs/privacy.html` is **generated** — do not
edit it by hand:

```bash
python build.py
```

No dependencies; it only handles the markdown the policy actually uses.

Keep `PRIVACY_POLICY.md` in step with the copy that ships inside the app (the
app shows it from its About window), so the page a Store reviewer reads and the
one a user reads are the same document. When the app's behaviour changes, update
both and revise the "Last updated" date.

## GitHub Pages

Pages serves from the `main` branch, `/docs` folder. `docs/.nojekyll` stops
Jekyll processing the plain HTML.
