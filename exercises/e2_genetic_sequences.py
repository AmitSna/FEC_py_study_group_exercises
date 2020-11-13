"""
contar_secuencias_geneticas = lambda secuencias: "Secuencias detectadas: {0}".format(len([seq for seq in secuencias.split("AUG") if seq[-3:] in ["UAA", "UAG", "UGA"]]))
"""

def contar_secuencias_geneticas(secuencias):
	return "Secuencias detectadas: {0}".format(len([seq for seq in secuencias.split("AUG") if seq[-3:] in ["UAA", "UAG", "UGA"]]))
