# CorrecTMe — Privacy Policy

_Last updated: 2026-10-04_

CorrecTMe ("the App") is a Windows utility that automatically corrects text typed
in the wrong keyboard layout (for example, Hebrew typed while the keyboard is set
to English, or vice versa). This document explains exactly what the App reads,
what it stores, and what it never does.

## What the App reads

To do its job, CorrecTMe reads keyboard input **system-wide** — that is, in every
application, not just its own window — because it has no other way to detect that
a word was typed in the wrong layout while you are typing it. This is the same
category of access used by any keyboard-layout-correction or text-expansion
utility (e.g. Punto Switcher-style tools).

The App also notices when a **mouse button is pressed**, anywhere. A click can
move the text cursor without a key being pressed, and the App must then forget
what it was about to correct, or the correction would land in the wrong place.
It reads nothing else about the mouse — not where you click or what you click
on — and records nothing about it.

### Clipboard

When you ask the App to flip selected text — with the shortcut, or from the tray
menu — it briefly uses the Windows clipboard to read that selection. Windows
offers no other reliable way for one program to see what is selected in another.
The App sends a Copy command to the application you are using, reads the result,
and puts your previous clipboard contents back. The text is held in memory only:
it is never written to a file and never transmitted.

Two consequences you should know about:

- **The copy is performed by the application you are typing in, not by the App.**
  That copy may therefore appear in Windows clipboard history (Win+V), in the
  cloud clipboard if you have that enabled, and in any clipboard manager you have
  installed. The App cannot prevent this, and it does not apply to the App's own
  write when it restores your clipboard, which is marked private.
- **Only plain text can be restored.** If you had an image, a file, or formatted
  content on the clipboard, it is destroyed by the Copy command itself, before
  the App reads anything. The App warns you when this happens.

The App does not read your clipboard at any other time — not in the background,
and not while correcting as you type.

**Do not use the flip shortcut on passwords or other sensitive text.** The App
declines to act in Windows password fields it can recognise, but it cannot
recognise password fields inside web pages.

## What the App stores, and where

Everything the App stores lives in `%APPDATA%\CorrecTMe\` on your own machine:

- **`corrections_log.jsonl`** — a rolling history of your **last 10
  corrections** (original text, corrected text, confidence score, and the name
  of the application you were typing in). It is automatically trimmed to the
  last 10 entries on every write; older entries are deleted, not archived. You
  can clear it at any time from **Settings → Clear Correction Log Now**, or
  switch logging off entirely from the same screen.
- **`settings.json`** — your chosen settings (language pair, hotkeys,
  correction sensitivity, etc.).
- **`app.log`** — a diagnostic log used to troubleshoot problems. At the
  App's default logging level this records only that a correction happened and
  how many characters it affected — **not** the text itself. Your typed text is
  recorded here only if you deliberately raise the logging level to DEBUG for
  troubleshooting. The file is size-capped and rotates automatically. You may
  delete it at any time.

The Undo (Ctrl+Z) feature works from an in-memory record of the single most
recent correction, which is discarded when the App closes; it does not read the
correction history file.

## What the App never does

- **Nothing you type is ever transmitted over the network.** CorrecTMe makes no
  network requests at runtime, has no telemetry, no analytics, and no update
  pinging.
- The App does not collect, sell, or share any data with third parties, because
  it does not send any data anywhere.
- The App does not require or request administrator privileges.

## Your controls

- **Pause/disable** the App at any time from the tray icon or with the toggle
  hotkey.
- **Clear your correction history** at any time from Settings.
- **Uninstall** the App like any other Windows application; this removes the
  App and, if you choose to also delete `%APPDATA%\CorrecTMe`, your local
  settings, correction history and diagnostic log.

## Third-party data

The App ships with word-frequency dictionaries used to score whether a block of
text looks like real English/Hebrew/etc. words. These dictionaries are derived
from Wikipedia content, which is licensed under Creative Commons
Attribution-ShareAlike 4.0 (CC BY-SA 4.0). See `NOTICES.md` for full attribution
and third-party license details.

## Contact

For privacy questions about CorrecTMe, contact the developer through the support
channel listed on the app's Microsoft Store listing page.

## Changes to this policy

If this policy changes, the "Last updated" date above will be revised and the
new version will ship with the next App update.
