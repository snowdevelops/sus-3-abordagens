import pandas as pd

def carregar_cnes(caminho):
    with open(caminho, encoding="latin-1") as f:
        linha = next(f)
        colunas = [c.strip('"') for c in linha.strip().split(";")]
    return colunas

def contar_linhas(caminho):
    with open (caminho, encoding="latin-1") as f:
        linha = next(f)
        contados = sum(1 for _ in f)
    return contados

def carregar_leitos(caminho):
    linhas = []
    with open(caminho, encoding="latin-1") as f:
        linha = next(f)
        colunas = [l.strip('"') for l in linha.strip().split(";")]
        i_uf = colunas.index("UF")
        i_comp = colunas.index("COMP")

        for linha in f:
            pedacos = [l.strip('"') for l in linha.strip().split(";")]
            if pedacos[i_uf]!= "MG":
                continue
            if pedacos[i_comp] != "202606":
                continue
            linhas.append(pedacos)
    return linhas, colunas

def espiar(caminho):
    with open (caminho, encoding="latin-1") as f:
        next(f)
        print(next(f))

def somar_por_municipio(linhas, colunas):
    i_ibge = colunas.index("CO_IBGE")
    i_leitos = colunas.index("LEITOS_SUS")
    soma = {}
    for pedacos in linhas:
        codigo = pedacos[i_ibge]
        quantidade = int(pedacos[i_leitos])
        if codigo not in soma:
            soma[codigo] = 0
        soma[codigo] += quantidade
    return soma

def carregar_regiao(caminho):
    df = pd.read_excel(caminho, skiprows=2, nrows=853)
    return df