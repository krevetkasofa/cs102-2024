import unittest

import hello_world


class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        m = "message"
        self.assertEqual(m, hello_world.text())
        
ciphertext = ""
    for symbol in plaintext:
        if symbol.isalpha(): # Если символ - это буква
          if symbol >= "a" and symbol <= "z":
              ciphertext += chr(((ord(symbol) + 2 - ord('a')) % 26) + ord('a'))
          else:
              ciphertext += symbol
        elif symbol.isupper():
          if symbol.isupper():
            if symbol >= "A" and symbol <= "Z":
                ciphertext += chr(((ord(symbol) + 2 - ord('A')) % 26) + ord('A'))
            else:
                ciphertext += symbol
    return ciphertext
