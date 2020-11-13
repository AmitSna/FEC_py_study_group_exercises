"""
contar_secuencias_geneticas = lambda secuencias: "Secuencias detectadas: {0}".format(len([seq for seq in secuencias.split("AUG") if seq[-3:] in ["UAA", "UAG", "UGA"]]))
"""

def contar_secuencias_geneticas(secuencias):
	#Cantidad Secuencias Genéticas:
	print("Secuencias detectadas: {0}".format(len(["AUG"+seq for seq in secuencias.split("AUG") if seq[-3:] in ["UAA", "UAG", "UGA"]])))

	#Opcional 1: Mostrar por consola las secuencias detectadas
	print("Las secuencias encontradas son: {0}".format(", ".join(["AUG"+seq for seq in secuencias.split("AUG") if seq[-3:] in ["UAA", "UAG", "UGA"]])))
	
	#Opcional 2: Indicar cuantos codones contiene cada secuencia
	print("Las cantidades de codones de cada secuencia son: {0}".format(", ".join([str(len("AUG"+seq)//3) for seq in secuencias.split("AUG") if seq[-3:] in ["UAA", "UAG", "UGA"]])))
	
	#Opcional 3: Emplear un diccionario para guardar todas las secuencias
	registro_secuencias = {}
	for seq in secuencias.split("AUG"):
		if seq[-3:] in ["UAA", "UAG", "UGA"]:
			if "AUG"+seq in registro_secuencias:
				registro_secuencias["AUG"+seq] += 1
			else:
				registro_secuencias["AUG"+seq] = 1
	print(f"El registro de secuencias es: {registro_secuencias}\n")
	
	#Opcional 4: Guardar las secuencias en un documento de texto, excel o como prefieran
	import pandas as pd
	
	data_frame = pd.DataFrame(list(registro_secuencias.items()),columns = ["Secuencias Encontradas", "Cantidad"])
	
	data_frame.to_excel("Secuencias.xlsx") #Crea el excel Secuencias.xlsx en el mismo directorio



contar_secuencias_geneticas("AUGGGGUACUACUAUAGGUAGAUGUGAAUGUGAAUGUGA")

contar_secuencias_geneticas("AUGUGA")

contar_secuencias_geneticas("AUGGGGUaUxAXUA-AGGUaG")

contar_secuencias_geneticas("AUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAG")
