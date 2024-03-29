# Desafio Final - Blog de Notícias 🚧 Squad Grace-Hopper

![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=STATUS&message=CONSTRU%C3%87%C3%83O&color=GREEN&style=for-the-badge)


### 🚀 Navegação do README:

- [Organização da equipe no Projeto Final](#organização-da-equipe-no-projeto-final-📍)
- [Tecnologias utilizadas [Back-end | Front-end]](#tecnologias-utilizadas-back-end--front-end)
- [Estrutura do Diretório com os arquivos e pastas](#estrutura-do-diretório-arquivos-e-pastas)
- [Instalação e criação do Ambiente Virtual](#instalação-e-criação-de-ambiente-virtual-🔧)
- [Padrões de Commit](#padrões-dos-commits---tipo-e-descrição-💻)
- [Apresentação do Projeto](#apresentação-do-projeto)
- [Squad Grace Hopper](#squad-grace-hopper)

<br>
<div style="text-align: center;">
    <img src="https://github.com/anaisateodoro/DesafioFinal_SquadGraceHopper/assets/70113922/6c29fd60-e288-42fe-ba9e-aecb2d641b44" alt="Blog portal de notícias" width="300" style="display: block; margin: 0 auto;">
</div>

<br>

# Organização da equipe no Projeto Final 📍

- Realizamos uma reunião inicial de planejamento para discutir o escopo do projeto, requisitos e definir metas e prioridades.
- Utilizaremos a ferramenta do Trello com uso do Kanban para manter a equipe na mesma página e seguir o trabalho com fluidez na  organização do projeto.
- Criamos diferentes listas para organizar as tarefas, como "Estruturas e Requisitos", "Backlog", "Doing", "Pendente","Blocked" e "Done".
- Estabelecemos aqui o [quadro do projeto no Trello 💡](https://trello.com/b/AiO9uDdS/desafiofinalsquadgracehopper).

- A data final de entrega do projeto é dia 12/04 e estamos trabalhando para garantir que todas as tarefas sejam concluídas até essa data.


# Tecnologias utilizadas [Back-end | Front-end]
* Python 3
* Django
* HTML
* CSS
* Bootstrap


# Requisitos Mínimos
**Windows:**

1. Acesse o site oficial do Python (https://www.python.org/downloads/).
2. Baixe o instalador do Python 3 para Windows.
3. Execute o instalador. Durante a instalação, marque a opção "Add Python 3.x to PATH" para adicionar o Python ao seu PATH.

**Linux:**

Na maioria das distribuições Linux, o Python já vem pré-instalado. No entanto, se você precisar instalar ou atualizar o Python, pode usar o seguinte comando:

```bash
sudo apt-get update
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

1. Clone o projeto <code>git clone https://github.com/anaisateodoro/DesafioFinal_SquadGraceHopper </code>
2. Entre no diretório do projeto <code>cd django-blog-noticias </code>
3. Create a Virtual Environment :-
    * no Windows <code>python -m venv env </code>
    * no Linux/Mac <code>python3 -m venv env </code>
4. Ative o Virtual Environment <code>source env/bin/activate </code>
5. Instale os pacotes requeridos <code>pip install -r requirments.txt</code>
6. Migrate Database :-
    * no Windows <code>py manage.py migrate</code>
    * no Linux/Mac <code>python3 manage.py migrate</code>
7. Crie SuperUser :-
    * no Windows <code>py manage.py createsuperuser</code>
    * no Linux/Mac <code>python3 manage.py createsuperuser</code>
8. Finalmente rode o projeto :
    * no Windows <code>py manage.py runserver</code>
    * no Linux/Mac <code>python3 manage.py runserver</code>

- Abra no seu navegador o servidor local em **localhost:8000**
- Ou se preferir, no seu terminal vá até o link do seu servidor local e pressione a tecla Ctrl + click mouse, que o projeto rodará na porta http://127.0.0.1:8000


# Estrutura do diretório: arquivos e pastas

- Em construção


# Padrões dos commits - Tipo e descrição 💻

<table>
  <thead>
    <tr>
      <th>Comando Git</th>
      <th>Resultado no GitHub</th>
    </tr>
  </thead>
 <tbody>
    <tr>
      <td>
        <code>git commit -m ":tada: Commit inicial"</code>
      </td>
      <td>🎉 Commit inicial</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":books: docs: Atualização do README"</code>
      </td>
      <td>📚 docs: Atualização do README</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":bug: fix: Loop infinito na linha 50"</code>
      </td>
      <td>🐛 fix: linha 10</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":sparkles: feat: Página de login"</code>
      </td>
      <td>✨ feat: Página de login</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":bricks: ci: Modificação no Dockerfile"</code>
      </td>
      <td>🧱 ci: Modificação no Dockerfile</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":recycle: refactor: Passando para functions"</code>
      </td>
      <td>♻️ refactor: Passando para functions</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":zap: perf: Melhoria no tempo de resposta"</code>
      </td>
      <td>⚡ perf: Melhoria no tempo de resposta</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":boom: fix: Revertendo mudanças ineficientes"</code>
      </td>
      <td>💥 fix: Revertendo mudanças ineficientes</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":lipstick: feat: Estilização CSS do formulário"</code>
      </td>
      <td>💄 feat: Estilização CSS do formulário</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":test_tube: test: Criando novo teste"</code>
      </td>
      <td>🧪 test: Criando novo teste</td>
    </tr>
    <tr>
      <td>
        <code>git commit -m ":bulb: docs: Comentários sobre a função LoremIpsum( )"</code>
      </td>
      <td>💡 docs: Comentários sobre a função LoremIpsum( )</td>
    </tr>
    <tr>
 </thead>
  </tbody>
</table>


# Apresentação do Projeto
- Slides 📊: [Apresentação Google]()
- Vídeo da apresentação 🎥: [YouTube]()


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


| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/108764670?v=4" width=115><br><sub>Adriana Lúcia</sub>](https://github.com/Dricalucia) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/70113922?v=4" width=115><br><sub>Anaísa Teodoro</sub>](https://github.com/anaisateodoro) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/151036471?v=4" width=115><br><sub>Caroline Rossafa</sub>](https://github.com/CRossafa) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/128868936?v=4" width=115><br><sub>Cintia Andrade</sub>](https://github.com/Cintiabge) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/76233172?v=4" width=115><br><sub>Larissa V. Menezes</sub>](https://github.com/vitoriastm) |  
| :---: | :---: | :---: | :---: | :---: |
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/65911301?v=4" width=115><br><sub>Luciane Fernandes</sub>](https://github.com/LucianeFernandesRoque) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/22503706?v=4" width=115><br><sub>Marina Reis</sub>](https://github.com/marireis) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/104047636?v=4" width=115><br><sub>Nathália Dias</sub>](https://github.com/nathaliadt) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/91030675?v=4" width=115><br><sub>Terezinha Lima</sub>](https://github.com/TerezinhaLima) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/11962383?v=4" width=115><br><sub>Vanessa Hallak</sub>](https://github.com/vhallak) |  
[<img loading="lazy" src="https://avatars.githubusercontent.com/u/14989288?s=200&v=4" width=115><br><sub>Andreia Vieira Gomes</sub>](https://github.com/WoMakersCode)
---

© 2024 - Squad Grace Hopper

[↑↑ - Voltar ao Topo](#desafio-final---blog-de-notícias-🚧-squad-grace-hopper)

