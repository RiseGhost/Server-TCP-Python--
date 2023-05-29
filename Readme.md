# Server TCP Python:

## Project INFO ℹ️:
- Name:             Server TCP Python
- Author:           RiseGhost 👻
- Python version:   3.11

__TCP -> Transmission Control Protocol__

## Introdução:
Este projeto tem como objetivo implementar um servidor TCP multithread em Python 🐍. Que possibilite a troca de mensagens entre um client e todos os clients conectados no servidor.

## CLI interface:
Tanto o servidor como o cliente operam sobre uma interface de CLI (console line interface). Embora tenha as suas limitações é possível executar este projeto sem grandes problemas nela.

![](https://user-images.githubusercontent.com/91985039/241814865-2b02479c-216c-4bb7-9f8b-589ae49c4a76.jpg)

### User Theme 🎨:
Para cada cliente novo conectado ao servidor é lhe atribuído um __UserTheme__ que é basicamente um icon representado por um emoji e um cor. Isso ajuda a distinguir melhor aquele utilizador dentro do servidor.

O ficheiro responsável por fazer o __UserTheme__ é o style.py.

É possivel, embora difícel, que dois ou mais clientes tenham o mesmo __UserTheme__.

## Client 👱🏽:
Para cada client é criado dois Threads.

Um main Thread responsável por fazer a leitura dos inputs do utilizador e enviar para o servidor.

Um Thread secundário que é instanciado pelo class __ReadChat__ que fica responsável por ler os outputs dado pelo servidor e imprimir na tela do usuário.

![](https://user-images.githubusercontent.com/91985039/241814849-eebff499-0a4e-4e02-a047-c2d13856e983.png)

## Server 🖥️:
O servidor opera mediante dois threads principais. Um deles sendo o MainThread responsável por inicia o servidor e por ficar a ler inputs da linha de comandos. E um segundo thread fica ocioso a executar a função __WaitForClients__. Esse thread fica responsável por esperar a conexão de um novo cliente e após receber ele processa essa conexão e cria um thread que fica responsável por receber os inputs desse cliente e fazer broadcast do mesmo.

Ou seja para cada novo cliente que se conecta ao servidor um novo thread é criado.

![](https://user-images.githubusercontent.com/91985039/241814847-aababb25-f6a9-4448-b84c-08bfb135338f.png)

## Tratamento de erros e exceptions ❎:
Este projeto tem a capacidade de tratar alguns erros e exceptions que possam acontecer durante a execução do código como por exemplo:

- Porta inválida:

![](https://user-images.githubusercontent.com/91985039/241816303-0e5165df-80ec-42e6-89eb-c030baa9b8d3.jpg)

- Erro ao conectar com o servidor:

![](https://user-images.githubusercontent.com/91985039/241816304-01490968-9976-4a3e-93b2-3a89c7003865.jpg)

- Você esta sozinho no servidor:

![](https://user-images.githubusercontent.com/91985039/241816308-6feda359-8866-4b4e-8aad-2e5f6801d3c2.jpg)

- Conexão com o servidor perdida (client):

![](https://user-images.githubusercontent.com/91985039/241816310-03e27ce0-577b-470b-8610-adcb51c91da2.jpg)

- Cliente desconectado (server):

![](https://user-images.githubusercontent.com/91985039/241816493-ef59e999-ac8f-4764-970e-88a454bc83c8.jpg)


## Code Problems ❌:
Apesar de tudo o código apresenta algum problemas entre os quais:

- Se um cliente 1 estiver a escrever algum enquanto outro cliente manda uma mensagem a mensagem que estava a ser escrita pelo cliente 1 é apagada. Algo que pode ser resolvida adicionando um interface gráfica ao projeto.
