def contar_ocorrencias(texto):

  texto = texto.lower()

  
  palavras = texto.split()
  for i in range(len(palavras)):
  
      palavras[i] = palavras[i].strip('.,!?;:')

 
  contagem = {}


  for palavra in palavras:
      if palavra in contagem:
          contagem[palavra] += 1
      else:
          contagem[palavra] = 1

  return contagem

texto = "como seria isso um teste aberto"
ocorrencias = contar_ocorrencias(texto)
print("Número de ocorrências de cada palavra:")
for palavra, num_ocorrencias in ocorrencias.items():
  print(f"{palavra}: {num_ocorrencias}")
