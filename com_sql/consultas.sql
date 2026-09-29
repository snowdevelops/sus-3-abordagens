\timing on
-- Quantoss leitos SUS cada região tem ? (16 linhas, CENTRO com 9984)
SELECT macrorregiao, SUM(leitos_sus) AS total
FROM municipios
GROUP BY macrorregiao
ORDER BY total DESC;

--Quantidade de leitos por mil pessoas, dividido por macrorregião (arredondado)

WITH total AS (
    SELECT macrorregiao, SUM(leitos_sus) AS leitos, SUM(populacao) AS pop
    FROM municipios
    GROUP BY macrorregiao
)
SELECT macrorregiao, leitos, ROUND(leitos * 1000.0 / pop , 2) AS por_mil
FROM total
ORDER BY por_mil DESC;

--TOP 3 por macrorregião por leitos (48 linhas expectadas)

WITH total AS (
    SELECT nome, macrorregiao, leitos_sus,
    ROW_NUMBER() OVER (PARTITION BY macrorregiao ORDER BY leitos_sus DESC) AS pos
    FROM municipios)
SELECT * FROM total WHERE pos <= 3;