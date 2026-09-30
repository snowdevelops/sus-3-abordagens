\timing on
-- Quantos leitos SUS cada região tem ? (16 linhas, CENTRO com 9984)
SELECT macrorregiao, SUM(leitos_sus) AS leitos_por_regiao
FROM municipios
GROUP BY macrorregiao
ORDER BY leitos_por_regiao DESC;

-- Quantidade de leitos por mil pessoas, dividido por macrorregião (arredondado)

WITH total AS (
    SELECT macrorregiao, SUM(leitos_sus) AS leitos, SUM(populacao) AS pop
    FROM municipios
    GROUP BY macrorregiao
)
SELECT macrorregiao, leitos, ROUND(leitos * 1000.0 / pop , 2) AS por_mil
FROM total
ORDER BY por_mil DESC;

-- TOP 3 por macrorregião por leitos (48 linhas expectadas)

WITH ranqueados AS (
    SELECT nome, macrorregiao, leitos_sus,
    ROW_NUMBER() OVER (PARTITION BY macrorregiao ORDER BY leitos_sus DESC) AS pos
    FROM municipios)
SELECT * FROM ranqueados WHERE pos <= 3
ORDER BY macrorregiao, pos;

-- Municípios sem leitos por macrorregião e suas porcentagens

WITH contagem_municipios AS (
    SELECT macrorregiao, COUNT(*) AS cidades
    FROM municipios
    GROUP BY macrorregiao
),
zerados AS (
    SELECT macrorregiao, COUNT(*) AS sem_leitos
    FROM municipios
    WHERE leitos_sus = 0
    GROUP BY macrorregiao
)
SELECT contagem_municipios.macrorregiao, contagem_municipios.cidades, zerados.sem_leitos, ROUND(zerados.sem_leitos * 100.0 / contagem_municipios.cidades, 2) AS pct
FROM contagem_municipios
LEFT JOIN zerados ON contagem_municipios.macrorregiao = zerados.macrorregiao
ORDER BY pct DESC;