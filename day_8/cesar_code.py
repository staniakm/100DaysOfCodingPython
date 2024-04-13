alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def crypt(text, shift):
    encrypted = ""
    for l in text:
        encrypted += get_new_letter(l, shift)
    return encrypted


def get_new_letter(letter, shift_value):
    if letter not in alphabet:
        return letter
    index = alphabet.index(letter)
    new_index = index + shift_value
    if new_index >= len(alphabet):
        new_index = new_index - len(alphabet)
    if new_index < 0:
        new_index = len(alphabet) + new_index
    return alphabet[new_index]


if (direction == "encode"):
    print(crypt(text=text, shift=shift))
else:
    print(crypt(text=text, shift=shift * -1))
