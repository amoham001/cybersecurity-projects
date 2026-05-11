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
