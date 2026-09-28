-- Cuidado, esse comando pode deletar qualquer tabela nomeada "municipios"
DROP TABLE IF EXISTS municipios;
CREATE TABLE municipios (
    codigo TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    macrorregiao TEXT NOT NULL,
    populacao INTEGER NOT NULL,
    leitos_sus INTEGER NOT NULL DEFAULT 0
);
-- O arquivo precisa estar acessível ao servidor Postgres.
-- Com Docker: docker cp data/processed/municipios.csv postgres-practice:/tmp/municipios.csv
COPY municipios FROM '/tmp/municipios.csv' WITH (FORMAT csv, HEADER true);