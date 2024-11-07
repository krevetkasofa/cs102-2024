<<<<<<< HEAD
def decrypt_scytale(ciphertext, n):
    columns = len(ciphertext) // n
    table = ["" for _ in range(n)]

    for i in range(columns):
        for j in range(n):
            table[j] += ciphertext[i * n + j]

    plaintext = "".join(table)
    return plaintext


ciphertext = "РНОАЫЙКЕСЕ_КТВА"
n = 3
decoded_message = decrypt_scytale(ciphertext, n)
print(decoded_message)
=======

>>>>>>> 73be9d99add19b72e4276a267fce06592f5ffb69
