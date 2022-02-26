from feeling import analisar_frase,exibir_resultado,classificador,vetorizador

print('E ai, como estamos?')
sentimentos = input("me fala como se sente:")
exibir_resultado( analisar_frase(classificador, vetorizador,sentimentos))