def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for symb in plaintext:
        if symb.isalpha():
            shift_amount = shift % 26
            if symb.islower():
                shifted = chr((ord(symb) - ord("a") + shift_amount) % 26 + ord("a"))
            elif symb.isupper():
                shifted = chr((ord(symb) - ord("A") + shift_amount) % 26 + ord("A"))
        else:
            shifted = symb
        ciphertext += shifted
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for symb in ciphertext:
        if symb.isalpha():
            shift_amount = shift % 26
            if symb.islower():
                shifted = chr((ord(symb) - ord("a") - shift_amount) % 26 + ord("a"))
            elif symb.isupper():
                shifted = chr((ord(symb) - ord("A") - shift_amount) % 26 + ord("A"))
        else:
            shifted = symb
        plaintext += shifted
    return plaintext
