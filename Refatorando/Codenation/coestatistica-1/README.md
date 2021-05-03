[![author](https://img.shields.io/badge/author-Eduardo%20Almeida-red.svg)](https://www.linkedin.com/in/eduardo-almeida-814a676a/) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/karinnecristina/Data-Science)

# Conhecendo melhor nossa base de consumidores: qual estado possui os clientes com melhores pontuações de crédito?

## Objetivo

Queremos conhecer melhor nossos clientes por estado. Para isso, iniciamos uma análise na pontuação de crédito. 
Para realizar a verificação inicial, precisamos de alguns valores.
Os valores são a média, a mediana, a moda e o desvio padrão da pontuação de crédito.

## Tópicos

Neste desafio você aprenderá:

- Média;
- Mediana;
- Moda;
- Desvio padrão.

## Requisitos

Você precisará de python 3.6 (ou superior).

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

## Detalhes

A resposta deve conter os valores da média, mediana, moda e desvio padrão da pontuação de crédito para cada estado do dataset.
O arquivo para submissão deve estar em formato json, conforme o arquivo exemplo "submission.json".

**OBSERVAÇÃO:**  É recomendado utilizar Python e pandas para esse desafio, mas também é possível utilizar outras ferramentas e linguagens de programação.

Descrição dos dados:
'id': Identificador do cliente
'sobrenome': Sobrenome do cliente
'pontuacao_credito': Pontuação de crédito do cliente (quanto maior, melhor o cliente geralmente)
'estado_residencia': Estado de residência do cliente
'genero': Gênero do cliente
'nivel_estabilidade': Nível de estabilidade do cliente
'saldo_conta': Saldo disponível na conta do cliente
'numero_produtos': Número de produtos que o cliente consome
'possui_cartao_de_credito': Possui um cartão de crédito cadastrado
'membro_ativo': Membro acessa e consome frequentemente

Obs: Os dados são fictícios, mas tentam representar a realidade de uma base de clientes de um produto SaaS. 




