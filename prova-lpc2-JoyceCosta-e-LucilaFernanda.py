"""
DUPLA: Lucila Fernada(lffs@etepd.com) e Joyce Costa(jdfc@etepd.com)


"""


import sqlite3 

conn = sqlite3.connect("vagaApp.db")

cursor = conn.cursor()

conn.execute ('''CREATE TABLE IF NOT EXISTS vaga(
id_vaga INTEGER PRIMARY KEY AUTOINCREMENT,
titulo_vaga TEXT,
salario_vaga TEXT,
data_criacao DATE,
nome_empresa TEXT,
nome_cargo TEXT,
descricao_vaga TEXT,
status BOOLEAN
);''')



print("MENU\n1.Cadastrar\n2.Listar\n3.Atualizar\n4.Deletar\n5.Sair")
menu = int(input("Selecione alguma das opções: "))

while(menu!=5):

    if(menu==1):
        titulo=input("Titulo: ")
        salario=input("salario: ")
        data=input("data: ")
        empresa=input("empresa: ")
        cargo=input("cargo: ")
        descricao=input("descricao: ")
        status=input("status: ")
        lista = [titulo,salario,data,empresa,cargo,descricao,status]
        # cadastrar 
        conn.execute('''INSERT INTO vaga(titulo_vaga, salario_vaga, data_criacao, nome_empresa, nome_cargo, descricao_vaga, status) VALUES(?,?,?,?,?,?,?)''', lista)


    if(menu==2):
        # listar
        cursoR = conn.execute('''SELECT * FROM vaga;''')

        for i in cursoR:
            print(i)


    if(menu==3):
        # Alterar Vaga
        id_vaga_informado = input("Informe o identificado para se alterar: ")
        print("INFORME OS NOVOS DADOS: ")
        titulo_novo=input("Titulo: ")
        salario_novo=input("salario: ")
        data_novo=input("data: ")
        empresa_novo=input("empresa: ")
        cargo_novo=input("cargo: ")
        descricao_novo=input("descricao: ")
        status_novo=input("status: ")
        cursor.execute("""UPDATE vaga SET titulo=?, salario=?, data=?, empresa=?, cargo=?, descricao=?,status=? WHERE id_vaga = id_vaga_informado""", (titulo_novo,salario_novo,data_novo,empresa_novo,cargo_novo,descricao_novo,status_novo))


    if(menu==4):
        # Deletar Vaga
        id_vaga_informado = input("Informe o identificado para se alterar: ")
        conn.execute("DELETE FROM vaga WHERE id_vaga = id_vaga_informado")


    if(menu==5):
        break














