def contar_numeros(vetor):
  positivos = 0
  negativos = 0
  zeros = 0

  for num in vetor:
      if num > 0:
          positivos += 1
      elif num < 0:
          negativos += 1
      else:
          zeros += 1

  return positivos, negativos, zeros


def ler_vetor():
  try:
      n = int(input("Digite o tamanho do vetor: "))
      vetor = []
      for i in range(n):
          num = int(input(f"Digite o {i+1}º número: "))
          vetor.append(num)
      return vetor
  except ValueError:
      print("Por favor, digite apenas números inteiros.")


vetor = ler_vetor()
positivos, negativos, zeros = contar_numeros(vetor)
print("Quantidade de números positivos:", positivos)
print("Quantidade de números negativos:", negativos)
print("Quantidade de zeros:", zeros)
