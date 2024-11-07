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
