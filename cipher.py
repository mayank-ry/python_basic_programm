import string

cipher_dict = {}
letters = string.ascii_letters

for i in range(len(letters)):
    next_index = (i + 1) % len(letters)
    cipher_dict[letters[i]] = letters[next_index]

print(cipher_dict)

data = ""

with open("file.txt", "r") as f:
    with open("meow.txt", "w") as out_file:
        while True:
            c = f.read(1)
            if not c:
                print("End Of File")
                break
            if c in cipher_dict:
                data = cipher_dict[c]
            else:
                data = c
            print(data)
            out_file.write(data)  # ✅ har character write hoga