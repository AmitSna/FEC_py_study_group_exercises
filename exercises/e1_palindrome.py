palindromo = lambda sentencia: print(sentencia.lower() == sentencia.lower()[::-1])

sentencia = input("Ingrese la frase a validar: ")

palindromo(sentencia)
