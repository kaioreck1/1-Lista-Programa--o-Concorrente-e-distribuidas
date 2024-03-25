import numpy as np

def ordenar_vetor(vetor):
    vetor_ordenado = np.sort(vetor)
    return vetor_ordenado

vetor = np.array([3, 1, 5, 2, 4])
vetor_ordenado = ordenar_vetor(vetor)
print("Vetor original:", vetor)
print("Vetor ordenado:", vetor_ordenado)
