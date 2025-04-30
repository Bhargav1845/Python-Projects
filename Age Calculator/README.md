# 🎂 Age Calculator

This is a simple Python program that calculates your age based on your date of birth and the current date (manually defined in the code).

---

## 📌 Features

- Takes birth **day**, **month**, and **year** as input from the user.
- Compares it with a hardcoded current date.
- Calculates and prints the user's age in years.
- Adjusts the result correctly if the birthday hasn't occurred yet this year.

---

## 🧠 Concepts Used

- Conditional logic
- Tuples for date comparison
- Input/output handling
- Basic date math

---

## ▶️ How to Run

1. Make sure you have Python installed (`python --version` to check).
2. Run the script:

```bash
python age_calculator.py
```

3. Enter your:
   - Birth day (e.g. `15`)
   - Birth month (e.g. `8`)
   - Birth year (e.g. `2004`)

---

## 💡 Example

**Input:**
```
Enter your birth day : 30
Enter your birth month : 4
Enter your birth year : 2005
```

**Output:**
```
19
```

---

## 📌 Note

- The current date is **hardcoded** as `23/3/2025`. For dynamic age calculation, consider using Python's `datetime` module to get the current system date.

---

## 📁 File Structure

```
Age-Calculator/
├── age_calculator.py
└── README.md
```

---

## ✅ To Do (Improvements)

- [ ] Use `datetime.date.today()` for dynamic current date
- [ ] Add error handling for invalid input (e.g., future dates, wrong values)

---

## 🧑‍💻 Author

Made with 💻 by Bhargav
