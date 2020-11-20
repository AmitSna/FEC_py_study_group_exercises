#justificador = lambda string: "".join([string[i:i + 30] + "\n" for i in range(0, len(string), 30)])

def justificador(string):
	return "".join([string[i:i + 30] + "\n" for i in range(0, len(string), 30)])

print(justificador("Esta es una cadena de texto de ejemplo de unos 60 caracteres"))
print(justificador("Cadenita de tan sólo 32 símbolos"))
print(justificador("hola"))
print(justificador("¡stringsstringsstringsstrings!"))
