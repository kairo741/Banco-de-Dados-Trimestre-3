# Importando uma biblioteca do Python para operar o sistema operacional (OS)
import os

msg_commit = input("Mensagem do commit: ")

# Se a mensagem for pequena demais, força o usuário a digitar uma msg maior
while len(msg_commit) <= 5:
    print("A mensagem deve ter pelo menos 5 caracteres.")
    msg_commit = input("Mensagem do commit: ")

# Define um email padrão para este script
email = "kairo.amorim2001@gmail.com"

# O \n dentro do print funciona como o <br/> no HTML (pula mais uma linha)
print("\n------------------------------------")

print("Adicionando os novos arquivos...\n")
os.system("git add *")

# O + soma quando os operadores são números e junta (une, concatena) quando são strings
print("Configurando o email do usuário...\n")
os.system('git config user.email "'+email+'"')

print("Efetuando o commit das modificações...\n")
os.system('git commit -m "'+msg_commit+'"')

print("Conectando com os servidores do Github...\n")
os.system('git push origin master')