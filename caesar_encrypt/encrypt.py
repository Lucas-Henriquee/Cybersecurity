# Encrypt by applying a shift
def caesar_encrypt(text, k):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine base ASCII value depending on case
            base = ord('A') if char.isupper() else ord('a')
            
            # Apply Caesar shift and wrap around alphabet
            shifted = chr((ord(char) - base + k) % 26 + base)
            result += shifted
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

# Decrypt by applying the negative shift
def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)