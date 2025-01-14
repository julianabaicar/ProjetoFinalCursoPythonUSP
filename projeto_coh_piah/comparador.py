from processamento import separa_sentencas, separa_frases, separa_palavras, n_palavras_unicas, n_palavras_diferentes

def compara_assinatura(as_a, as_b):
    somatorio_diferencas = 0
    for i in range(len(as_a)):
        somatorio_diferencas += abs(as_a[i] - as_b[i])
    grau_similaridade = somatorio_diferencas / len(as_a)
    return grau_similaridade

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    tamanho_medio_palavra = sum(len(palavra) for palavra in palavras) / len(palavras)
    type_token_ratio = n_palavras_diferentes(palavras) / len(palavras)
    hapax_legomana_ratio = n_palavras_unicas(palavras) / len(palavras)
    tamanho_medio_sentenca = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)
    complexidade_sentenca = len(frases) / len(sentencas)
    tamanho_medio_frase = sum(len(frase) for frase in frases) / len(frases)

    return [tamanho_medio_palavra, type_token_ratio, hapax_legomana_ratio, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    assinaturas_textos = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura_texto, ass_cp) for assinatura_texto in assinaturas_textos]
    infectado = min(range(len(textos)), key=lambda i: similaridades[i])
    return infectado + 1
