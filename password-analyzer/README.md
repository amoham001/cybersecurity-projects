# Password Strength Analyzer

## 📋 Overview

A Python-based tool that evaluates password strength based on industry-standard complexity requirements. The analyzer provides real-time feedback on password security and offers actionable recommendations for improvement.

This project demonstrates understanding of password security principles, input validation, and user feedback mechanisms—core concepts in cybersecurity and compliance frameworks.

---

## 🎯 Skills Demonstrated

- **Python Programming** - Regular expressions, functions, string manipulation
- **Password Security** - NIST guidelines, complexity requirements, entropy
- **Security Best Practices** - Input validation, secure password policies
- **User Experience** - Clear feedback and actionable recommendations
- **Compliance Knowledge** - Security+, NIST SP 800-63B standards

---

## 🚀 Installation & Usage

### Requirements
- Python 3.6+
- No external dependencies

### Setup
```bash
# Clone or download the repository
git clone https://github.com/amoham001/cybersecurity-projects/edit/main/password-analyzer/
cd password-analyzer

# Run the script
python password_tester.py

```

### Basic Usage
```python
# Test a password
password = "MyP@ssw0rd123"
strength, feedback = check\_password\_strength(password)

print(f"Password Strength: {strength}")
for item in feedback:
    print(item)
```

### Output
```code
Password Strength: Very Strong
```
## 💻 Code Explanation
```python
import re

def check_password_strength(password):
    feedback = []
    
    # Step 1: Check length first (must be at least 12)
    if len(password) < 12:
        return "Very Weak", ["❌ Password too short (min 12 characters)"]
    
    # Step 2: If length passes, check other criteria
    score = 1  # Already 1 for passing length
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add numbers")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add special characters")
    
    # Step 3: Map score to strength
    strengths = ["Very Weak", "Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
    strength = strengths[score]
    
    if not feedback:
        feedback.append("✅ All criteria met!")
    
    return strength, feedback

# Test
password = input("Enter a password: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
for item in feedback:
    print(item)



```
How it works:
- For every criteria met a point (+1) is added to "score" variable
- There is a maximum of 5 points
- Any failed criteria are added to the "feedback" list for user guidance
- All passwords are automatically set to "very weak" if they do not pass the "Length" criteria

## 📊 Example Outputs

### Example 1 - Fair Password

<div align="center">

<i>Figure 1 - fair password</i>
[Fair Password](https://github.com/amoham001/cybersecurity-projects/blob/de0737f94b8e51a7fec49322bee1896bfc56590a/password-analyzer/screenshots/fair.png)

</div>

### Example 2 - Very Strong Password

<div align="center">

<i>Figure 2 - very strong password</i>
[Very Strong Password](https://github.com/amoham001/cybersecurity-projects/blob/de0737f94b8e51a7fec49322bee1896bfc56590a/password-analyzer/screenshots/verystrong.png)

</div>

### Example 3 - Very Weak Password

<div align="center">

<i>Figure 1 - very weak password</i>
[Very Weak Password](https://github.com/amoham001/cybersecurity-projects/blob/de0737f94b8e51a7fec49322bee1896bfc56590a/password-analyzer/screenshots/veryweak.png)

</div>


