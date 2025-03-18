import random
import string

def generate_secure_password(
    length: int = 12,
    include_numbers: bool = True,
    include_symbols: bool = True
) -> str:
    """
    Generate a secure random password
    
    Args:
        length: Length of the password
        include_numbers: Include numbers in the password
        include_symbols: Include special characters
        
    Returns:
        str: Generated password
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''
    
    # Combine all allowed characters
    all_characters = letters + digits + symbols
    
    if not all_characters:
        raise ValueError("At least one character set must be selected")
    
    # Ensure minimum length
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # Ensure password contains at least one character from each selected set
    if include_numbers and not any(c in digits for c in password):
        password = password[:-1] + random.choice(digits)
    
    if include_symbols and not any(c in symbols for c in password):
        password = password[:-1] + random.choice(symbols)
    
    return password 