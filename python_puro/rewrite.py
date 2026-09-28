def carregar_leitos(caminho):
    linhas = []
    with open(caminho, encoding="latin-1") as f:
        linha = next(f)
        colunas = [l.strip('"') for l in linha.strip().split(";")]
        i_uf = colunas.index("UF")
        i_comp = colunas.index("COMP") 

        for linha in f:
            pedacos = [l.strip('"') for l in linha.strip().split(";")]
            if pedacos[i_uf] != "MG":
                continue
            if pedacos[i_comp] != "202606":
                continue
            linhas.append(pedacos)
    return linhas, colunas
leitos,coluna_leitos = carregar_leitos("data/raw/Leitos_2026.csv")
print (len(leitos))

def somar_por_municipio(linhas, colunas):
    i_ibge = colunas.index("CO_IBGE")
    i_leitos_sus = colunas.index("LEITOS_SUS")
    soma = {}
    for pedacos in linhas:
        codigo = pedacos[i_ibge]
        quantidade = int(pedacos[i_leitos_sus])
        if codigo not in soma:
            soma[codigo] = 0
        soma[codigo] += quantidade
    return soma

soma = somar_por_municipio(leitos, coluna_leitos)
print(len(soma))
print(soma["310620"])