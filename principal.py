import sqlite3
import usuario

########################################################
################## PROGRAMA PRINCIPAL ##################
########################################################
conexao = sqlite3.connect("banco.sqlite")

# criarTabelaUsuario(conexao)
# usuario.inserirUsuario(conexao)
usuario.excluir_usuario(conexao)

# usuario.update_usuario(conexao)

# usuario.listar_usuario(conexao)


conexao.close()
###