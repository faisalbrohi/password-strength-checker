# 🔐 Password Strength Checker - Streamlit Web App

This project is a *Password Strength Checker* built with *Python* and *Streamlit*. It allows users to test the strength of their passwords and receive real-time feedback on how to improve them.

This tool is useful for:
- Educating users on password security
- Understanding password best practices
- Showcasing beginner-friendly cybersecurity and Python web app skills

---

## 🚀 Features

- *Real-Time Strength Check* – Enter a password and instantly get a rating.
- *Strength Categories* – Passwords are classified as:
  - ❌ Weak
  - ⚠️ Moderate
  - ✅ Strong
- *Improvement Suggestions* – The app provides specific tips to make your password stronger.
- *Clean and User-Friendly Interface* – Built with Streamlit for an interactive experience.

---

## 🧠 How It Works (Code Explanation)

### 1. *Password Validation Logic*

The core of the app is a Python function that analyzes a password using *regular expressions*:

```python
def check_password_strength(password):
    strength = 0
    remarks = []
It checks for:
	•	Minimum length (8 characters)
	•	Uppercase letters: A-Z
	•	Lowercase letters: a-z
	•	Digits: 0-9
	•	Special characters: !@#$%^&*()...

Each satisfied condition adds 1 point to the strength score.

if len(password) < 8:
    remarks.append("Too short (min 8 characters)")
else:
    strength += 1

Other conditions are checked using re.search(), such as:
if re.search(r"[A-Z]", password):
    strength += 1
else:
    remarks.append("Add uppercase letters")

2. Rating Logic

Based on the total score (0 to 5), the password is rated:
if strength <= 2:
    rating = "❌ Weak"
elif strength in [3, 4]:
    rating = "⚠️ Moderate"
else:
    rating = "✅ Strong"

Suggestions are stored in a list and displayed only if there are things to improve.

🖥️ Streamlit Web Interface

We use Streamlit to make this script interactive:

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password", type="password")

When the user enters a password, it’s checked and feedback is displayed with colors:

st.markdown(f"*Strength*: <span style='color:{color}'>{rating}</span>"

🧪 How to Run Locally

1. Clone the repository.

git clone https://github.com/faisalbrohi/password-strength-checker.git
cd password-strength-checker

2. Create a virtual environment (optional but recommended)
   
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies.
pip install -r requirements.txt

4. Launch the app

streamlit run App.py

📁 Project Structure

password_strength_checker/
│
├── App.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignore virtual env and other unnecessary files

📌 Technologies Used
	•	Python 3
	•	Streamlit – For building the web UI
	•	Regex (re module) – For pattern matching
	•	Git & GitHub – For version control and hosting

✍️ Author

Shah Faial
Beginner in Cybersecurity & Networking | Passionate about building security tools
[LinkedIn](http://linkedin.com/in/shahfaisalrahim) | GitHub

✅ Future Improvements (Optional Ideas)
	•	Add a password generator
	•	Display password entropy score
	•	Add dark/light theme toggle
	•	Save password analysis history (locally or in a DB)
