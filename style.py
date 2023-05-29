import sys, random

#Este ficheiro python apenas server para fazer estilização de elementos no terminal, como por exemplo:
#- Limpar o terminal;
#- Atribuição de emojis aos clientes
#- Atribuição de cores aos clientes

UserTheme = [("🐻","\033[0;33m"),("🦊","\033[0;31m"),("🐼","\033[0;37m"),("🐍","\033[0;32m"),("👻","\033[0;37m"),("😺","\033[0;33m"),("🐔","\033[0;37m"),("🦀","\033[0;31m"),("🐳","\033[0;34m"),("🐠","\033[0;34m"),("🐉","\033[0;33m"),("🦄","\033[0;35m"),("🦩"," \033[0;35m"),("🐞","\033[0;31m"),("🦁","\033[0;33m"),("🐣","\033[0;33m"),("🦉","\033[0;37m")]
ResetConsoleColor = "\033[0m"

def ChoiseUserTheme():
    return random.choice(UserTheme)

def CleanConsole():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
