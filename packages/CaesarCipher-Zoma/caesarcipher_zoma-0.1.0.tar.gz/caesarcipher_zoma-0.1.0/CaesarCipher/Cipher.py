class Caesar_Cipher:
    default_key = { "a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
            "h": "k","i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o":
            "r", "p": "s","q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y",
            "w": "z", "x": "a","y": "b", "z": "c", " ":" "}
    def __init__(self, key = default_key, antikey = default_key):
        self.key = key
        self.antikey = antikey

    def encrypt_message(self, message):
        encrypted_message = ''
        for char in message:
            for dic_key, dic_value in self.key.items():
                if char == dic_key:
                    encrypted_message += dic_value
        return encrypted_message
    
    def decrypt_message(self, message):
        decrypted_message = ''
        for char in message:
            for dic_key, dic_value in self.key.items():
                if char == dic_value:
                    decrypted_message += dic_key
        return decrypted_message
    
    def check_input(self, message):
        for char in message:
            if not (char.isalpha() or char == ' '):
                raise ValueError("Input is not valid, only alphabets and spaces are allowed.")
    
    @staticmethod
    def get_cipher(message, key = None,  encrypt = True):
        cipher = Caesar_Cipher(key)
        if encrypt:
            return cipher.encrypt_message(message)
        else:
            return cipher.decrypt_message(message)


cipher = Caesar_Cipher()
message = "hello world"
encrypted = cipher.encrypt_message(message)
print("Encrypted:", encrypted)
decrypted = cipher.decrypt_message(encrypted)
print("Decrypted:", decrypted)

