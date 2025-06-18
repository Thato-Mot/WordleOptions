# 🧠 WordleSolver

A simple Python-based assistant to help me solve Wordle puzzles by filtering a word list based on known clues: correct letters, present letters, absent letters, and invalid positions. (I play Wordle daily and I noticed previous answers do not get repeated... the goal is not to find the word, its to find it in the least amount of tries).

## 📂 Project Structure

```
.
├── Wordler.py
├── words.txt          # A list of valid 5-letter words (one per line)
└── past_words.txt     # A space-separated list of past Wordle answers
```

## 🚀 Features

* Filters out previously used Wordle answers
* Tracks known letters in correct positions (green tiles)
* Handles present letters in unknown positions (yellow tiles)
* Filters out letters known to be absent (gray tiles)
* Accounts for known invalid positions for letters
* Suggests up to 90 possible next guesses

## 🛠️ Usage

### 1. Prepare your files

Ensure you have:

* `words.txt`: a list of 5-letter words (e.g., from a dictionary file).
* `past_words.txt`: a list of words that have already been used as Wordle answers (space-separated on one line).

### 2. Basic Example

```python
from WordleSolver import WordleSolver

solver = WordleSolver("words.txt", "past_words.txt")

# Update clues based on feedback
solver.update_absent_letter('udioste')          # Gray tiles
solver.update_present_letter('ar')              # Yellow tiles
solver.update_invalid_position('a', [0, 3])      # 'a' is not in positions 0 or 3
solver.update_invalid_position('r', [4])         # 'r' is not in position 4

solver.update_known_letters("_____")            # Use '_' for unknown letters

solver.display_progress()                       # See current state and suggestions
```

## 🧠 Logic

Each word suggestion must:

* **Not** be in the list of past answers
* Match the pattern for known correct letters
* Include all present letters (but not in invalid positions)
* Exclude all absent letters
* Avoid known bad positions for certain letters

## ✅ Methods

| Method                                       | Description                                                            |
| -------------------------------------------- | ---------------------------------------------------------------------- |
| `update_known_letters(pattern)`              | Add known letter positions, using `'_'` for unknowns (e.g., `"_r__e"`) |
| `update_present_letter(letter)`              | Add a yellow-letter guess (letter is in the word, unknown position)    |
| `update_absent_letter(letter)`               | Add a gray-letter guess (letter is not in the word)                    |
| `update_invalid_position(letter, positions)` | Specify positions where a letter **cannot** be                         |
| `get_suggestions()`                          | Get a list of remaining candidate words                                |
| `display_progress()`                         | Print current solver state and suggestions                             |

## 🧪 Example Output

```
Current word:  _____
Present letters:  {'r', 'a'}
Absent letters:  {'s', 'u', 'i', 't', 'e', 'd', 'o'}
Suggestions:  ['brank', 'cramp', 'graph', 'wrack', ...]
```

## 📌 Notes

* The solver is case-insensitive.
* Designed for experimentation and daily Wordle help.
* Customize `words.txt` with your preferred word list (e.g., the official Wordle word list).
