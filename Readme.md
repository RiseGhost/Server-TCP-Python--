# Server TCP Python:

## Project INFO ℹ️:
- Name:             Server TCP Python
- Author:           RiseGhost 👻
- Python version:   3.11

## Implementação:
Este projeto tem com objetivo implementar um servidor TCP multithread em Python 🐍. Que possibelite a torca de mensagem entre um client e todos os clients conectados no servidor.

Para cada client conectado é inciado um __ReadChat__ do lado do client que fica responsável por fazer a leitura de strings devolvidas pelo server.
A classe __ReadChat__ é um _"extend"_ da classe Thread.
Fazendo assim que quando é instaciado um ReadChat ele fica a ser executado em um thread separado do main.

Do lado do server para cada client conectado também é iniciado um thread que fica responsável por ler as strings devolvidas pelos clients e enviar essa string para todos os outros clients.

