import sqlite3

def criarTabelaUsuario(conexao):
    
    cursor = conexao.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS usuario(
            nome TEXT NOT NULL,
            login TEXT NOT NULL,
            senha TEXT NOT NULL
        );'''

    cursor.execute(sql)


def inserirUsuario(conexao):

    nome = input("Insira seu nome: ")
    login = input("Insira seu login: ")
    senha = input("Insira sua senha: ")

    cursor = conexao.cursor()
    sql = '''
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
'''.format(nome, login, senha)
    
    cursor.execute(sql)
    conexao.commit()



def listar_usuario(conexao):
    cursor = conexao.cursor()
    sql="""
    SELECT rowid, * FROM usuario 
    """

    cursor.execute(sql)
    lista=cursor.fetchall()
    
    print("ID\t Nome\t \t\t Login")
    for i in lista:
        print('{} \t {} \t\t {}'.format(i[0], i[1], i[2]))





########################################################
################## PROGRAMA PRINCIPAL ##################
########################################################

conexao = sqlite3.connect("banco.sqlite")

# criarTabelaUsuario(conexao)

listar_usuario(conexao)

# inserirUsuario(conexao)

# conexao.close()
