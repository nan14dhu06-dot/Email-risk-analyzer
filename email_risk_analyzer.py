import re

# Suspicious keywords list
risk_keywords = [
    "urgent",
    "verify your account",
    "click here",
    "password",
    "bank details",
    "login now",
    "limited time",
    "security alert",
    "otp",
    "confirm identity"
]

# Function to analyze email
def analyze_email(email_text):
    risk_score = 0
    detected = []

    # Check suspicious keywords
    for word in risk_keywords:
        if word.lower() in email_text.lower():
            risk_score += 1
            detected.append(word)

    # Detect links
    links = re.findall(r'https?://\S+', email_text)

    # Check suspicious links
    if links:
        for link in links:
            if "https://" not in link:
                risk_score += 2
                detected.append("Suspicious Link")

    # Display result
    print("\n----- EMAIL ANALYSIS REPORT -----")

    if risk_score == 0:
        print("Status : SAFE")
    elif risk_score <= 2:
        print("Status : SUSPICIOUS")
    else:
        print("Status : HIGH RISK")

    print("Risk Score :", risk_score)

    if detected:
        print("Detected Issues:")
        for item in detected:
            print("-", item)
    else:
        print("No suspicious content detected.")

# Multi-line email input
print("Paste the email content (Type END on a new line to finish):")

lines = []

while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

email = "\n".join(lines)

# Analyze the email
analyze_email(email)