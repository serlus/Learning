def frequencia(texto):
    frequencia_por_palavra = [texto.count(p) for p in texto]
    return dict(zip(texto, frequencia_por_palavra))

def popularidade(texto, palavras):
    dFrequencia = frequencia(texto)
    return dict((k, dFrequencia[k]) for k in palavras if k in dFrequencia)

print(popularidade(open('texto.txt').read().split(), ['filhos', 'amada']))