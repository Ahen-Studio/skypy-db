from skypydb.security import EncryptionManager

# Generate a secure encryption key
encryption_key = EncryptionManager.generate_key()
print(encryption_key) # don't show this key to anyone
