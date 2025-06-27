# PRODIGY_ST_03
A Python-based automated login test suite using Selenium WebDriver to validate positive and negative login scenarios on the SauceDemo web application. Includes test cases for valid credentials, invalid login attempts, and empty field submissions.
# 🚀 Automated Login Test using Selenium | Prodigy InfoTech Internship – Task 03

This repository contains an automated test suite developed in **Python** using **Selenium WebDriver** to validate the login functionality of a sample web application. It is part of **Task-03** of the **Software Testing Internship** at **Prodigy InfoTech**.

---

## 🌐 Website Under Test

**URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## ✅ Test Scenarios Covered

1. **Positive Test Case**
   - Valid login with correct username and password

2. **Negative Test Cases**
   - Invalid login with wrong credentials
   - Login attempt with empty fields

---

## 🧰 Technologies Used

- Python 3
- Selenium WebDriver
- ChromeDriver (or any browser driver of choice)
- VS Code / PyCharm (for development)

---

## 📁 Project Structure

PRODIGY_ST_03/
│
├── test_login.py # Main Python script containing test cases
├── requirements.txt # Python dependencies
├── .gitignore # Files ignored by Git
└── README.md # Project documentation

yaml
Copy code

---

## ▶️ How to Run the Tests

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/PRODIGY_ST_03.git
cd PRODIGY_ST_03
2. Install Dependencies
Make sure you have Python and pip installed. Then run:

bash
Copy code
pip install -r requirements.txt
3. Run the Test Script
bash
Copy code
python test_login.py
🧪 Sample Output
pgsql
Copy code
✅ Valid login test passed.
❌ Invalid login test passed.
⚠️ Empty field login test passed.
