select user_a,
       user_b,
       sum(qtde_figurinhas) as qtde_figurinhas,
       sum(case when qtde_figurinhas = 0 then 0 else 1 end) as qtde_trocas,
       count(1) as qtde_tentativas

from tb_troca

where qtde_figurinhas > 0

group by  user_a, user_b
order by user_a, user_b