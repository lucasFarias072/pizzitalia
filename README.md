# pizzitalia
Repository for an IFPI project to simulate a pizza place

# Instruções:

###### Tenha o python instalado

###### Crie uma pasta e abra ela no terminal

###### Clone o repositório para o seu computador

```
git clone git@github.com:lucasFarias072/pizzitalia.git
```

###### Instale um ambiente virtual (Windows)

```
python -m venv venv
```

###### ou

```
python3 -m venv venv
```

###### caso não dê certo: pesquise sobre isso
 
###### Ative o ambiente virtual (Windows)

```
venv\scripts\activate
```

###### Faça a instalação das dependências que o projeto precisa

```
pip install -r requirements.txt
```

###### Crie e valide as tabelas

```
python manage.py makemigrations
python manage.py migrate
```

###### Execute a aplicação localmente

```
python manage.py runserver
```
