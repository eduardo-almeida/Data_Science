[![author](https://img.shields.io/badge/author-Eduardo%20Almeida-red.svg)](https://www.linkedin.com/in/eduardo-almeida-814a676a/) [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/karinnecristina/Data-Science)

# Redução de dimensionalidade e seleção de variáveis

Neste desafio vamos praticar redução de dimensionalidade com PCA e seleção
de variáveis com RFE.

## Objetivo

O objetivo deste desafio é explorar sobre como funciona o PCA e como podemos
obter _data sets_ de dimensões mais baixas através dele.

Para isso, vamos contar com o _data set_ [FIFA 2019](https://www.kaggle.com/karangadiya/fifa19)
que contém originalmente 89 variáveis com diversos atributos de mais de 18 mil jogadores
do _game_ FIFA 2019.

## Tópicos

Neste desafios nós vamos explorar:

* Redução de dimensionalidade
* PCA
* Seleção de variáveis
* RFE

## Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes dependências
do desafio:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
$ deactivate
```
