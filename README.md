What this is- The same analysis implemented in three ways: pure Python, Pandas, SQL. https://github.com/snowdevelops/acesso-leitos-sus-mg

Why - The honest answer is that it's a learning exercise. But there's a real technical point too, implementing the same pipeline three ways and verifying identical results is how you know you understand what the abstractions do.

For the following info, it's essential that foreign readers know what the terms mean; "leitos_sus" equals to Brazillian public service SUS beds to each municipality, registered as "nome" that goes inside a bigger and broader geographic parameter "macrorregioes" that equals to english translating, macrorregions.

The numbers that verify agreement - 33607 beds, 21393441 people, 853 municipalities, 449 with zero beds, Belo Horizonte 6403.

How to reproduce:
    Download the raw data files - https://dadosabertos.saude.gov.br/dataset/hospitais-e-leitos , https://www.saude.mg.gov.br/estudos-assistenciais-e-regionalizacao/ , https://dados.gov.br/dados/conjuntos-dados/taxa-de-cobertura-de-planos-de-saude

    Run the Python pipeline → produces data/processed/municipios.csv
    docker cp that CSV into the container at /tmp/
    Run schema.sql
    Run consultas.sql

    Run the script on /sus-tres-abordagens/com_sql/schema.sql with "docker exec -i postgres-practice -U snow -d sus < schema.sql"  --CAUTION ! the script drops any table named "municipios" before recreating it.

Dependencies: Python 3.12 +, pandas, Postgres 17.