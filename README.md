# Password Toolkit

A desktop application written in Python and Qt (PySide6) to **evaluate the strength of a password** and **generate cryptographically secure passwords**.

The project is designed with a clear separation between the core logic and the graphical interface: the evaluation and generation engine has no dependency on the GUI, so it can be reused in a CLI, a web app or automated tests.

<p align="center">
  <img src="assets\passwordToolkitGen.png" width="45%" alt="Password Toolkit Generate Demo">
  <img src="assets\passwordToolkitEval.png" width="45%" alt="Password Toolkit Evaluate Demo">
</p>

---

## Features

**Evaluate tab**
- Scores any password on an 8-point scale based on length, character variety and presence in a list of common passwords.
- Colour-coded progress bar (red → orange → blue → green) and a textual verdict.
- Flags passwords found in a common-password list as *compromised*, regardless of their length or complexity.

**Generate tab**
- Generates multiple passwords at once with a configurable length range and quantity.
- Choice of character sets: uppercase, lowercase, digits, special characters.
- Every generated password is guaranteed to contain at least one character from each selected set.
- Each result is automatically evaluated and shown in a table with its score and strength.
- Double-click a row to copy the password to the clipboard.

---

## How the score works

| Criterion | Points |
|---|---|
| Not present in the common-password list | 1 |
| Length greater than 8, 12, 17 and 20 characters | 1 each (max 4) |
| Uses 2, 3 or 4 different character types | 1, 2 or 3 |
| **Maximum** | **8** |

A password found in the common-password list always scores **0**, because attackers try those lists first.

| Score | Verdict |
|---|---|
| 0 (in common list) | Compromised |
| 0–3 | Very weak |
| 4 | Weak |
| 5 | Fairly strong |
| 6–8 | Very strong |

---

## Security notes

- Passwords are generated with Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module, which is designed for cryptographic use. The `random` module is deliberately **not** used, because its output is predictable.
- Characters are drawn with replacement and then shuffled with a cryptographically secure RNG, so the position of the guaranteed characters is not predictable.
- Everything runs locally: no password is ever sent over the network or written to disk.

---

## Project structure

```
pyPasswordProject/
├── core/
│   ├── __init__.py
│   ├── password_tools.py      # evaluation and generation logic (no GUI code)
│   └── commonPasswords.txt    # list of common passwords, one per line
├── ui/
│   ├── __init__.py
│   ├── main_window.ui         # window layout, editable in Qt Designer
│   ├── ui_main_window.py      # generated from the .ui file (do not edit)
│   └── main_window.py         # connects the widgets to the core logic
├── main.py                    # application entry point
├── requirements.txt
└── README.md
```

---

## Getting started

### Requirements

- Python 3.9 or newer
- PySide6 (installed via `requirements.txt`)

### Installation

```bash
git clone https://github.com/3rch0m41/pyPasswordProject.git
cd pyPasswordProject

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Run

```bash
python main.py
```

### Common-password list

The file `core/commonPasswords.txt` must contain one password per line. A good source is the [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials) collection (for example the top 10,000 most common passwords). If the file is missing, the app still works but will not detect compromised passwords.

---

## Editing the interface

The layout is defined in `ui/main_window.ui` and can be edited visually with Qt Designer, which is included with PySide6:

```bash
pyside6-designer ui/main_window.ui
```

After saving your changes, regenerate the Python code:

```bash
pyside6-uic ui/main_window.ui -o ui/ui_main_window.py
```

Never edit `ui_main_window.py` by hand: it is overwritten every time it is regenerated. Put all the window logic in `ui/main_window.py` instead.

---

## Roadmap

Planned improvements:

- [ ] **Have I Been Pwned check** — query the [Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords) using its *k-anonymity* model: only the first 5 characters of the password's SHA-1 hash are sent, so the password itself never leaves the machine.
- [ ] **Entropy and crack-time estimate** — show the password's entropy in bits and an estimated time to crack it, for example using the [zxcvbn](https://github.com/dwolfhub/zxcvbn-python) library, which also detects dictionary words, keyboard patterns and dates.
- [ ] **CSV export** — save the generated passwords and their scores to a CSV file.
- [ ] **Password manager features** — store credentials in an encrypted local vault protected by a master password, with the key derived through a memory-hard function such as Argon2id and data encrypted with AES-256-GCM (via the [`cryptography`](https://cryptography.io/) library), plus automatic clipboard clearing after copying.
- [ ] **Dark theme** — a Qt stylesheet (QSS) based dark theme with a toggle between light and dark mode.
- [ ] **Standalone executable** — package the app with [PyInstaller](https://pyinstaller.org/) so it can run without a Python installation, bundling the common-password list as a data file.
- [ ] **Command-line interface** — a CLI built with `argparse` that reuses the same `core` module, e.g. `python cli.py evaluate "MyP@ssw0rd"` or `python cli.py generate --min 12 --max 20 --qty 5`.

---

## Author

**Giulio Malini** (Erchomai)
