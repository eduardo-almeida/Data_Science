with tb_network as (
    select user_a,
        user_b,
        sum(qtde_figurinhas) as qtde_figurinhas,
        sum(case when qtde_figurinhas = 0 then 0 else 1 end) as qtde_trocas,
        count(1) as qtde_tentativas

    from tb_troca

    group by  user_a, user_b

    order by user_a, user_b )

select user,
       sum(qtde_relacionamentos) as qtde_relacionamentos,
       sum(qtde_figurinhas) as qtde_figurinhas

from (
    select user_a as user,
    qtde_figurinhas,
    (1) as qtde_relacionamentos
    from tb_network
    where qtde_figurinhas > 0

    UNION ALL

    select user_b as user,
    qtde_figurinhas,
    (1) as qtde_relacionamentos
    from tb_network
    where qtde_figurinhas > 0
)

group by user

order by qtde_relacionamentos desc