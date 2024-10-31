def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)

    for i in range(len(plaintext)):
        symbol = plaintext[i]
        if symbol.isalpha():
            shift = ord(keyword[i % keyword_length]) - ord("A")
            base = ord("A") if symbol.isupper() else ord("a")
            ciphertext += chr((ord(symbol) - base + shift) % 26 + base)
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)

    for i in range(len(ciphertext)):
        symbol = ciphertext[i]
        if symbol.isalpha():
            shift = ord(keyword[i % keyword_length]) - ord("A")
            base = ord("A") if symbol.isupper() else ord("a")
            plaintext += chr((ord(symbol) - base - shift) % 26 + base)
        else:
            plaintext += symbol
    return plaintext
