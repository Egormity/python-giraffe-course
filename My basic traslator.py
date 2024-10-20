
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "g"
        if letter in "AEIOU":
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter your phrase to translate: ")))