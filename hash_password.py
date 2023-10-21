import bcrypt
# password = userInput
def hashh(password):
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashAndSalt.decode()

# save "hashAndSalt" in data base
# To check:
# password = userInput
def valid(password, hashAndSalt):
    valid = bcrypt.checkpw(password.encode(), hashAndSalt.encode()) #logical
    return valid
