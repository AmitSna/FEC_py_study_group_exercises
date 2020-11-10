is_palindrome = lambda phrase: phrase.lower() == phrase.lower()[::-1]

print("Ingrese la frase a validar: ", end="")

phrase = input()

print(is_palindrome(phrase))
