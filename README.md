Meu Projeto Django: Atividade de Templates
Descrição do Projeto
Este é um projeto simples em Django desenvolvido como parte de uma atividade de programação web. O objetivo é demonstrar a criação e o uso de templates HTML e arquivos estáticos (CSS) para construir um site com múltiplas páginas.

O projeto inclui as seguintes funcionalidades:

Página Inicial (/): Uma introdução ao site.

Página Sobre (/sobre/): Informações sobre a atividade e os aprendizados.

Página de Contato (/contato/): Detalhes para contato.

As páginas utilizam um template base (base.html) para reutilizar o código comum e possuem estilos de fundo e cores de título distintos, conforme solicitado na atividade.

Tecnologias Utilizadas
Django: Framework web para Python.

HTML5: Estrutura das páginas.

CSS3: Estilização das páginas.

Como Executar o Projeto
Siga os passos abaixo para rodar o projeto localmente:

Pré-requisitos
Python 3.x instalado.

O gerenciador de pacotes pip instalado.

Passo a Passo
Clone o Repositório:

git clone https://github.com/seu-usuario/meu-projeto-django.git
cd meu-projeto-django

Crie e Ative o Ambiente Virtual:

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

Instale as Dependências:

pip install -r requirements.txt

Observação: Se você ainda não criou o arquivo requirements.txt, pode fazê-lo com o comando: pip freeze > requirements.txt

Execute as Migrações do Banco de Dados:

python manage.py migrate

Inicie o Servidor de Desenvolvimento:

python manage.py runserver

Abra seu navegador e acesse: http://127.0.0.1:8000/.

Estrutura do Projeto
meu-projeto-django/
├── myproject/
│   ├── settings.py
│   └── urls.py
├── website/
│   ├── static/
│   │   ├── style.css
│   │   └── imagens/
│   │       ├── laptop.jpg
│   │       ├── prancheta.jpg
│   │       └── celular.jpg
│   ├── templates/
│   │   └── website/
│   │       ├── base.html
│   │       ├── contato.html
│   │       ├── index.html
│   │       └── sobre.html
│   ├── urls.py
│   └── views.py
├── manage.py
├── .gitignore
└── README.md

Autor

Patrick Eitz
