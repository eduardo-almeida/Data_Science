WITH tb_subset_mediana As (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (select count(*) % 2 == 0 FROM points)
    OFFSET (select 2 * count(*) / 4 from points)
),

tb_mediana AS (
    SELECT AVG(qtdPontos) AS Mediana
    FROM tb_subset_mediana
),

tb_subset_quartil_01 As (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (select count(*) % 2 == 0 FROM points)
    OFFSET (select 1 * count(*) / 4 from points)
),

tb_quartil_01 AS (

    SELECT avg(qtdPontos) quartil_01
    FROM tb_subset_quartil_01

),

tb_subset_quartil_03 As (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (select count(*) % 2 == 0 FROM points)
    OFFSET (select 3 * count(*) / 4 from points)
),

tb_quartil_03 AS (

    SELECT avg(qtdPontos) AS quartil_03
    FROM tb_subset_quartil_03

),

tb_stats AS (

    SELECT min(qtdPontos) AS minimo,
        avg(qtdPontos) AS media,
        max(qtdPontos) As maximo,
        max(qtdPontos) - min(qtdPontos) AS amplitude

    FROM points

)

SELECT *
FROM tb_stats, tb_mediana, tb_quartil_01, tb_quartil_03