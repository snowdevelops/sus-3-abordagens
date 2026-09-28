from src.carregar import carregar_cnes, contar_linhas, carregar_leitos, espiar , somar_por_municipio, carregar_regiao
import pandas as pd

colunas = carregar_cnes("data/raw/Leitos_2026.csv")
contados = contar_linhas("data/raw/Leitos_2026.csv")
espiar("data/raw/Leitos_2026.csv")
leitos, coluna_leitos = carregar_leitos("data/raw/Leitos_2026.csv")
soma = somar_por_municipio(leitos, coluna_leitos)
regiao = carregar_regiao("data/raw/Planilha-de-Regionalizacao_Versao-2026.xlsx")
df_leitos = pd.DataFrame(list(soma.items()), columns=["codigo", "leitos_sus"])
regiao["Código DATASUS/ MS"] = regiao["Código DATASUS/ MS"].astype(str)
df = regiao.merge(df_leitos, left_on="Código DATASUS/ MS", right_on="codigo", how="left")
df_cnes = pd.DataFrame(leitos, columns= coluna_leitos)
df_cnes["LEITOS_SUS"] = df_cnes["LEITOS_SUS"].astype(int)
soma_pd = df_cnes.groupby("CO_IBGE")["LEITOS_SUS"].sum()
codigos_planilha = set(regiao["Código DATASUS/ MS"])
codigos_cnes = set(soma.keys())
df["leitos_sus"] = df["leitos_sus"].fillna(0)
df["Macrorregião de Saúde"] = df["Macrorregião de Saúde"].str.strip()
pop = df.groupby("Macrorregião de Saúde")["POPULAÇÃO CENSO DEMOGRÁFICO (IBGE/2025)"].sum()
leitos_grupo = df.groupby("Macrorregião de Saúde")["leitos_sus"].sum()
taxa = leitos_grupo / pop *1000
df.to_csv("data/processed/municipios.csv", index = False)
saida = df[["Código DATASUS/ MS", "Município ", "Macrorregião de Saúde",
            "POPULAÇÃO CENSO DEMOGRÁFICO (IBGE/2025)", "leitos_sus"]].copy()
saida["leitos_sus"] = saida["leitos_sus"].astype(int)
saida.columns = ["codigo", "nome", "macrorregiao", "populacao", "leitos_sus"]
saida.to_csv("data/processed/municipios.csv", index=False)
zeros = [k for k, v in soma.items() if v == 0]
print(len(zeros))
print(zeros)
print(df["leitos_sus"].isna().sum())
print((df["leitos_sus"] == 0).sum())