# Desafio Final - Blog de Notícias | Squad Grace-Hopper

![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

### 🚀 Navegação do readme:

- [Organização da equipe](#organização-da-equipe-👍)
- [Tecnologias utilizadas](#Tecnologias utilizadas [Back-end | Front-end]🎯)
- [Requisitos Mínimos](#requisitos-mínimos-🧭)
- [Estrutura do Diretório com os arquivos e pastas](#estrutura-do-diretório-arquivos-e-pastas)
- [Instalação e criação do Ambiente Virtual](#instalação-e-criação-de-ambiente-virtual-🔧)
- [Padrões de Commit](#padrões-dos-commits---tipo-e-descrição-💻)
- [Apresentação do Projeto](#apresentação-do-projeto)
- [Squad Grace Hopper](#squad-grace-hopper)

<br>
<div style="text-align: center;">
    <img src="https://github.com/anaisateodoro/django-blog-noticias/assets/70113922/294ca833-4eab-4bad-b05c-53a97d17d67a" alt="Blog portal de notícias" width="300" style="display: block; margin: 0 auto;">
</div>
<br>
<br>

# Organização da equipe 👍

- Realizamos uma reunião inicial de planejamento para discutir o escopo e requisitos do projeto, além de definir metas e prioridades.
- Utilizaremos para o gerenciamento do projeto a ferramenta do Trello, na visualização das tasks com uso do quadro Kanban e as Sprint e Dayli Meeting com o metodolo Ágil do Scrum, afim de manter a equipe focada em entregas contínuas e fluidez da organização do Blog de Notícias.
- Nesse quadro kanban, criamos diferentes listas para organizar as tarefas, como "Estruturas e Requisitos", "Backlog", "Doing", "Pendente","Blocked", "Testes", "Features" e "Done".
- Estabelecemos o quadro do projeto no -> [Trello 💡](https://trello.com/b/AiO9uDdS/desafiofinalsquadgracehopper).

# Tecnologias utilizadas [Back-end | Front-end]🎯

- Editor de códigos (IDE a sua escolha);
- Python 3
- Django
- HTML
- CSS
- Bootstrap 4
- PostgreSQL

# Requisitos Mínimos 🧭

**Windows:**

1. Acesse o site oficial do Python (https://www.python.org/downloads/).
2. Baixe o instalador do Python 3 para Windows.
3. Execute o instalador. Durante a instalação, marque a opção "Add Python 3.x to PATH" para adicionar o Python ao seu PATH.

**Linux:**

Na maioria das distribuições Linux, o Python já vem pré-instalado. No entanto, se você precisar instalar ou atualizar o Python, pode usar o seguinte comando:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3
```

**Mac:**

1. Acesse o site oficial do Python (https://www.python.org/downloads/).
2. Baixe o instalador do Python 3 para Mac.
3. Execute o instalador.

# Instalação e Criação de Ambiente Virtual 🔧

Clone este repositório remoto no seu diretório local.Certifique-se que tenha instalado o Python3. Depois, no seu repositório local, vá para pasta
onde efetuou o clone do repositório.

💡 Utilize os seguintes comandos no terminal:

1. Clone o projeto <code>git clone https://github.com/anaisateodoro/django-blog-noticias.git </code> e instale o Django <code>pip install django</code>
2. Entre no diretório do projeto, crie uma pasta <code>mkdir django-blog-noticias</code> e depois certifique-se que esteja dentro dessa pasta<code>cd django-blog-noticias </code> e depois para abrir a IDE da sua preferência digite o comando <code>code .</code>.
3. Create a Virtual Environment :
   - no Windows <code>python -m venv env </code>
   - no Linux/Mac <code>python3 -m venv env </code>
4. Ative o Virtual Environment:
   - no Windows <code>venv\Scripts\Activate</code>
   - no Linux/Mac <code>source env/bin/activate</code>
5. Instale os pacotes requeridos <code>pip install -r requirements.txt</code>
   Caso no linux pedir uma atualização do gerenciador de bibliotecas, use o comando <code>pip install --upgrade pip</code> e para instalar <code>pip freeze > requirements.txt</code>
   Para configuração do banco de dados, Instale as dependências
   `pip install psycopg2`,
   `pip install psycopg2-binary`
6. Migrate Database :

- Somente na primeira vez, para configuração do db <code>python manage.py makemigrations</code>
- Executar as migrações para criação da tabela de dados.
  - no Windows <code>py manage.py migrate</code>
  - no Linux/Mac <code>py manage.py migrate</code>
- Se caso der erro de postgressql, verifique se o bd está ativo na sua maquina.
  - no Linux `sudo service postgresql start`
  - no Windows:
    1. Pressione a tecla Windows + R para abrir a caixa de diálogo Executar.
    2. Digite `services.msc` e pressione Enter. Isso abrirá o Gerenciador de Serviços.
    3. Procure pelo serviço PostgreSQL na lista. O nome do serviço geralmente começa com "postgresql", seguido pela versão do PostgreSQL (por exemplo, "postgresql-x64-13").
    4. Clique com o botão direito do mouse no serviço PostgreSQL e selecione "Iniciar".
7. Crie SuperUser :-
   - no Windows <code>py manage.py createsuperuser</code>
   - no Linux/Mac <code>python3 manage.py createsuperuser</code>
8. Finalmente rode o projeto :
   - no Windows <code>py manage.py runserver</code>
   - no Linux/Mac <code>python manage.py runserver</code>

- Abra no seu navegador o servidor local em **localhost:8000**
- Ou se preferir, no seu terminal vá até o link do seu servidor local e pressione a tecla Ctrl + click mouse, que o projeto rodará na porta http://127.0.0.1:8000

# Estrutura do diretório: arquivos e pastas

- Em construção

![tree_diretorio](https://github.com/anaisateodoro/django-blog-noticias/assets/70113922/b9f21d85-ca87-43a8-a2c5-80f080abf5a4)

<br>
# Padrões dos commits - Tipo e descrição 💻

| Comando Git | Resultado no GitHub |
|-------------|---------------------|
| `git commit -m ":tada: Commit inicial"` | 🎉 Commit inicial |
| `git commit -m ":books: docs: Atualização do README"` | 📚 docs: Atualização do README |
| `git commit -m ":bug: fix: Loop infinito na linha 50"` | 🐛 fix: linha 10 |
| `git commit -m ":sparkles: feat: Página de login"` | ✨ feat: Página de login |
| `git commit -m ":bricks: ci: Modificação no file"` | 🧱 ci: Modificação no file |
| `git commit -m ":recycle: refactor: Passando para functions"` | ♻️ refactor: Passando para functions |
| `git commit -m ":zap: perf: Melhoria no tempo de resposta"` | ⚡ perf: Melhoria no tempo de resposta |

# Apresentação do Projeto

- Slides 📊: [Apresentação Slides - Canvas](https://www.canva.com/design/DAGCJzplkOs/oOyyCzquOKS19Fd6CYn90A/edit?utm_content=DAGCJzplkOs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
)
- Vídeo da apresentação 🎥: [YouTube](https://youtu.be/AxdWmpDjb_w)

# Squad Grace Hopper

1. Adriana Lúcia de França Rodrigues<br>
2. Anaisa Mayara Teodoro<br>
3. Andreia Vieira Gomes<br>
4. Caroline Mariane Silva Rossafa<br>
5. Cintia Andrade<br>
6. Larissa Vitória Menezes<br>
7. Luciane Fernandes Roque<br>
8. Marina dos Reis Barros<br>
9. Nathalia Dias<br>
10. Terezinha de Jesus Ferreira<br>
11. Vanessa Hallak Alves<br>

|        [<img loading="lazy" src="https://avatars.githubusercontent.com/u/108764670?v=4" width=115><br><sub>Adriana Lúcia</sub>](https://github.com/Dricalucia)        | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/70113922?v=4" width=115><br><sub>Anaísa Teodoro</sub>](https://github.com/anaisateodoro) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/151036471?v=4" width=115><br><sub>Caroline Rossafa</sub>](https://github.com/CRossafa) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/128868936?v=4" width=115><br><sub>Cintia Andrade</sub>](https://github.com/Cintiabge)   | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/76233172?v=4" width=115><br><sub>Larissa V. Menezes</sub>](https://github.com/vitoriastm) |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/65911301?v=4" width=115><br><sub>Luciane Fernandes</sub>](https://github.com/LucianeFernandesRoque) |     [<img loading="lazy" src="https://avatars.githubusercontent.com/u/22503706?v=4" width=115><br><sub>Marina Reis</sub>](https://github.com/marireis)     | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/104047636?v=4" width=115><br><sub>Nathália Dias</sub>](https://github.com/nathaliadt)  | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/91030675?v=4" width=115><br><sub>Terezinha Lima</sub>](https://github.com/TerezinhaLima) |    [<img loading="lazy" src="https://avatars.githubusercontent.com/u/11962383?v=4" width=115><br><sub>Vanessa Hallak</sub>](https://github.com/vhallak)     |

## [<img loading="lazy" src="https://avatars.githubusercontent.com/u/14989288?s=200&v=4" width=115><br><sub>Andreia Vieira Gomes</sub>](https://github.com/WoMakersCode)

© 2024 - Squad Grace Hopper

[↑↑ - Voltar ao Topo](#desafio-final---🚧blog-de-notícias--squad-grace-hopper)
