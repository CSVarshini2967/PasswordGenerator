import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generate a secure password with customizable options.
    
    Args:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters A-Z
        use_lowercase (bool): Include lowercase letters a-z  
        use_digits (bool): Include digits 0-9
        use_symbols (bool): Include symbols !@#$%^&*
    
    Returns:
        str: Generated password
    """
    
    # Build character pool based on user preferences
    character_pool = ""
    
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Make sure we have at least one character type selected
    if not character_pool:
        raise ValueError("At least one character type must be selected!")
    
    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def generate_multiple_passwords(count=5, length=12, **kwargs):
    """Generate multiple passwords at once."""
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length, **kwargs))
    return passwords

def check_password_strength(password):
    """
    Basic password strength checker.
    
    Args:
        password (str): Password to check
        
    Returns:
        dict: Strength analysis
    """
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    score = sum([has_lower, has_upper, has_digit, has_symbol])
    
    strength_levels = {
        1: "Weak",
        2: "Fair", 
        3: "Good",
        4: "Strong"
    }
    
    return {
        "score": score,
        "strength": strength_levels.get(score, "Very Weak"),
        "length": len(password),
        "has_lowercase": has_lower,
        "has_uppercase": has_upper,
        "has_digits": has_digit,
        "has_symbols": has_symbol
    }

def main():
    """Main function to run the password generator interactively."""
    print("Welcome to the Python Password Generator!")
    print("=" * 40)
    
    while True:
        try:
            # Get user preferences
            print("\nPassword Options:")
            length = int(input("Enter password length (default 12): ") or 12)
            
            print("\nCharacter types to include:")
            use_lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
            use_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
            use_digits = input("Include numbers? (Y/n): ").lower() != 'n'
            use_symbols = input("Include symbols? (Y/n): ").lower() != 'n'
            
            count = int(input("How many passwords to generate? (default 1): ") or 1)
            
            # Generate passwords
            print(f"\n Generated Password{'s' if count > 1 else ''}:")
            print("-" * 40)
            
            if count == 1:
                password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
                print(f"Password: {password}")
                
                # Show strength analysis
                strength = check_password_strength(password)
                print(f"Strength: {strength['strength']} ({strength['score']}/4)")
                print(f"Length: {strength['length']} characters")
                
            else:
                passwords = generate_multiple_passwords(
                    count, length, 
                    use_uppercase=use_uppercase,
                    use_lowercase=use_lowercase, 
                    use_digits=use_digits,
                    use_symbols=use_symbols
                )
                
                for i, pwd in enumerate(passwords, 1):
                    strength = check_password_strength(pwd)
                    print(f"{i:2d}. {pwd} (Strength: {strength['strength']})")
            
        except ValueError as e:
            print(f"Error: {e}")
            continue
        except KeyboardInterrupt:
            print("\n\n Thanks for using the password generator!")
            break
        
        # Ask if user wants to generate more
        again = input("\nGenerate more passwords? (Y/n): ").lower()
        if again == 'n':
            print("Thanks for using the password generator!")
            break

# Example usage
if __name__ == "__main__":
    # You can run the interactive version
    main()
    
    # Or use the functions directly:
    # password = generate_password(16, use_symbols=True)
    # print(f"Generated password: {password}")
    # print(check_password_strength(password))