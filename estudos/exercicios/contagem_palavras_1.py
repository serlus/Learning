def popularidade(texto, palavra):
    import re
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(palavra), texto))

palavras = "nos, a, preste"
texto = "Ao nos resolver a esta tarefa, preste nos atenção nos seguintes a nos pontos:"
d = dict( (v, popularidade(texto, v)) for v in palavras.split(",") )
print(d)