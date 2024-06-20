# Como rodar o projeto localmente

## Pré-requisitos
- Python 3.6 ou superior
- Pip (gerenciador de pacotes Python)
- Virtualenv (para criar ambientes virtuais Python)

## Passo 1: Configurar Ambiente Virtual
Com o terminal aberto no diretório do projeto:
- Para criar o ambiente virtual, execute o comando: `python -m venv env`

- Para ativar o ambiente virtual, execute:

  No windows: `.\env\Scripts\activate`

  No macOS/Linux: `source env/bin/activate`

## Passo 2: Instalar Dependências
`pip install -r requirements.txt`

## Passo 3: Configurar Banco de Dados
- Cria as migrations do projeto com o comando: `python manage.py makemigrations`
- Aplique as migrações ao banco de dados com o comando: `python manage.py migrate`

## Passo 4: Rodar o Servidor Local
Execute o comando: `python manane.py runserver`

Acesse o projeto no navegador utilizando o endereço: `http://127.0.0.1:8000/`
