# Email Risk Analyzer

## Overview
Email Risk Analyzer is a Python-based cybersecurity project that detects suspicious or phishing emails by analyzing email content. The program identifies risky keywords, unsafe links, and sensitive data prompts, then classifies emails as Safe, Suspicious, or High Risk.

---

## Features
- Detects phishing-related keywords
- Identifies suspicious links
- Generates risk scores
- Classifies emails based on risk level
- Supports multi-line email input

---

## Technologies Used
- Python
- Regular Expressions (`re` module)

---

## How to Run

### Step 1: Save the file
Save the Python code as:

```bash
email_risk_analyzer.py
```

### Step 2: Run the program

```bash
python email_risk_analyzer.py
```

---

## Example Input

```text
Urgent! Verify your account now.
Click here: http://fake-bank.com
Enter your password immediately.
END
```

---

## Example Output

```text
----- EMAIL ANALYSIS REPORT -----
Status : HIGH RISK
Risk Score : 5

Detected Issues:
- urgent
- verify your account
- click here
- password
- Suspicious Link
```
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/434e11c9-b95b-44ce-9211-67969baadfd1" />

---

## Project Objective
The objective of this project is to help users identify potentially unsafe or phishing emails by analyzing suspicious patterns commonly used in cyberattacks.

---

## Author
Nandhitha V N 
