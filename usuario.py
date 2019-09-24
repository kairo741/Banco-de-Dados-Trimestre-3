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
    sql = """
    SELECT rowid, * FROM usuario 
    """

    cursor.execute(sql)
    lista = cursor.fetchall()

    print("ID\t Nome\t \t\t Login")
    for i in lista:
        print('{} \t {} \t\t {}'.format(i[0], i[1], i[2]))





#Algoritmo para dar UPDATE em um usuário
def update_usuario(conexao):
    cursor = conexao.cursor()
    rowid = int(input("Qual o ID do usuario que deseja dar update? "))

    sql = """
    SELECT nome, login,senha FROM usuario
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)

    update = input("O que deseja alterar (Nome, Login ou Senha)? ")

    if(update == 'senha' or update == 'Senha'):
        update_x = 'a Senha'
        noSql = "senha"


    elif(update == 'Login' or update == 'login'):
        update_x = 'o Login'
        noSql = "login"


    elif(update == 'nome' or update == 'Nome'):
        update_x = 'o Nome'
        noSql = "nome"


    lista = cursor.fetchall()
    update = input('Deseja realmente dar alterar {} do usuário "{}" que tem o login "{}"? (S/N)'.format(update_x, lista[0][0], lista[0][1]))

    if (update == 'S' or update == 's'):
        while(True):
            confirmar = input("Insira a senha: ")
            if(confirmar == lista[0][2]):
                novo = input("Insira {} novo(a) que deseja alterar: ".format(update_x))
                while(True):
                      
                    confirmar = input("Confirme {}: ".format(update_x))
                    if(confirmar == novo):
                        print("Alterando...")
                        sql_alterar = """
                            UPDATE usuario
                            SET {} = '{}'
                            WHERE rowid = {};
                            """.format(noSql,novo,rowid)

                        cursor.execute(sql_alterar)
                        conexao.commit()

                        print("Você alterou {} do Usuário {}!".format(update_x,rowid))
                        break
                    else:
                        print("Confirmação incorreta!")
                    continuar = input("Deseja continuar (S/N)? ")
                    if (continuar == 'N' or continuar == 'n'):
                        print("Você saiu!")
                        break

            else:
                print("Senha incorreta")

            continuar = input("Deseja continuar (S/N)? ")
            if (continuar == 'N' or continuar == 'n'):
                print("Você saiu!")
                break


    else:
        print("Até mais")






#Algoritmo para excluir de dados.
def excluir_usuario(conexao):
    cursor = conexao.cursor()
    rowid = int(input("Qual o ID do usuario que deseja excluir? "))

    sql = """
    SELECT nome, login,senha FROM usuario
    WHERE rowid = {} 
    """.format(rowid)
    cursor.execute(sql)
    lista = cursor.fetchall()
    excluir = input('Deseja dar excluir o usuário "{}" que tem o login "{}"? (S/N)'.format(lista[0][0], lista[0][1]))

    if (excluir == 'S' or excluir == 's'):
        while(True):
            confirmar = input("Insira a senha (atual) para alterar: ")
            if(confirmar == lista[0][2]):
                print("Excluindo...")

                sql_excluir = """
                    DELETE FROM usuario
                    WHERE rowid = {}
                    """.format(rowid)
                cursor.execute(sql_excluir)
                conexao.commit()

                print("Você excluiu o Usuário {}!".format(rowid))
                break

            else:
                print("Senha incorreta")

            continuar = input("Deseja continuar (S/N)? ")
            if (continuar == 'N' or continuar == 'n'):
                print("Você saiu!")
                break

    else:
        print("Até mais")
