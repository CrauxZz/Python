import itertools
import zipfile
import string


name = "crackfile"
chars = string.ascii_letters, string.digits, string.punctuation

for guess in itertools.product(chars, repeat=5):
    guess = ''.join(guess)
    try:
        with zipfile.Zipfile(name, "r") as zip_ref:
            zip.ref.extractall(pwd = guess.enconde("utf-8"))
            print(f"File extracted" "Password: ", guess)
            break
    except Exception as e:
        pass
