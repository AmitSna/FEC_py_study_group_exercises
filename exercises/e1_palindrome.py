is_palindrome = lambda phrase: print(["No es Palíndromo", "Es Palíndromo"][phrase.lower() == phrase.lower()[::-1]])

phrase = input("Ingrese la frase a validar: ")

is_palindrome(phrase)
