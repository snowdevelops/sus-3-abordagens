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
