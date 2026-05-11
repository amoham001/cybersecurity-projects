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

*Figure 1 - fair password*

![Fair Password](https://github.com/amoham001/cybersecurity-projects/blob/de0737f94b8e51a7fec49322bee1896bfc56590a/password-analyzer/screenshots/fair.png)

</div>

### Example 2 - Very Strong Password

<div align="center">
    
*Figure 2 - very strong password*
 
![Very Strong Password](https://github.com/amoham001/cybersecurity-projects/blob/de0737f94b8e51a7fec49322bee1896bfc56590a/password-analyzer/screenshots/verystrong.png)

</div>

### Example 3 - Very Weak Password

<div align="center">

*Figure 3 - very weak Password*

![Very Weak Password](https://github.com/amoham001/cybersecurity-projects/blob/430f21d5bdf5fd18d46f6b54adf806dda429e98e/password-analyzer/screenshots/veryweak.png)

</div>

## 🛠️ Technical Details

| Pattern | Purpose |
|---------|---------|
| `[A-Z]` | Detects uppercase letters |
| `[a-z]` | Detects lowercase letters |
| `\d` | Detects numerical digits |
| `[!@#$%^&*(),.?":{}&#124;<>]` | Detects special characters |

### Scoring System

| Score | Rating |
|-------|--------|
| 0 | Very Weak |
| 1 | Weak |
| 2 | Fair |
| 3 | Good |
| 4 | Strong |
| 5 | Very Strong |

## 💡 Potential Upgrades

## 💡 Potential Enhancements

- [ ] **Breach Database Check** - Implement Have I Been Pwned (HIBP) API integration to check if password appears in known breaches
- [ ] **Common Password Dictionary** - Check against rockyou.txt or similar datasets for commonly used passwords
- [ ] **Entropy Calculation** - Calculate password entropy (bits) and display alongside strength rating
- [ ] **Keyboard Pattern Detection** - Detect sequential patterns like "qwerty" or "12345" and penalize them
- [ ] **Substitution Pattern Detection** - Identify weak patterns like "P@ssw0rd" (common letter-to-symbol replacements)
- [ ] **GUI Interface** - Build graphical interface using Tkinter or Flask web version for easier use
- [ ] **Unicode/International Support** - Add support for non-ASCII characters and international character sets
- [ ] **Batch Analysis** - Accept file input to analyze multiple passwords at once
- [ ] **Customizable Strength Thresholds** - Allow users to define their own minimum requirements
- [ ] **Password History** - Track previously checked passwords and export results to CSV
- [ ] **Active Directory Integration** - Check passwords against organizational policies
- [ ] **Strength Meter Visualization** - Visual progress bar or color-coded strength display
- [ ] **Zxcvbn Integration** - Integrate popular password strength estimator library for advanced analysis
- [ ] **Language-Specific Dictionaries** - Support multiple languages for common password detection
- [ ] **Export Results** - Generate security reports in PDF or HTML format
