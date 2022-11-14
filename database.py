import sqlite3

class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    #------------Users-------------------------

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                
                CREATE TABLE IF NOT EXISTS users(
                
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                    
                );
            
            """)

        except AttributeError:
            print("faça a conexão")

    def check_usuario(self, user):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM users;

            """)

            for linha in cursor.fetchall():
                if linha[2] == user:
                    return "não"
                else:
                    continue
            return "sim"
        except:
            pass

    def table_users_first(self, name, user, password, access):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                 INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)
                
            
            """,(name, user, password, access))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def insert_user(self, name, user, password, access):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)
                
            
            """,(name, user, password, access))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def check_user(self, user, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT * FROM users;
            
            """)

            for linha in cursor.fetchall():
                if linha[2] == user and linha[3] == password and linha[4] == "Administrador":
                    return "administrador"
                elif linha[2] == user and linha[3] == password and linha[4] == "Usuário":
                    return "user"
                else:
                    continue
            return "sem acesso"
        except:
            pass

    #------------Equipamento-----------------------

    def create_table_equipamento(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                 CREATE TABLE IF NOT EXISTS equipamento(
                     
                     codgEquip INTEGER NOT NULL PRIMARY KEY,
                     descricaoEquip TEXT NOT NULL
                 );

             """)

        except AttributeError:
            print("faça a conexão")

    def insert_equipamento(self, codgEquip,  descricaoEquip):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO equipamento(codgEquip, descricaoEquip) VALUES(?, ?)


            """, (codgEquip, descricaoEquip))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    #-------------Produto----------------------------

    def create_table_produto(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                
                
                CREATE TABLE IF NOT EXISTS produtos(

                    codgProd TEXT NOT NULL PRIMARY KEY,
                    descricaoProd TEXT NOT NULL,
                    equipamento TEXT NOT NULL,
                    qntProd INT
                    
                );

            """)

        except AttributeError:
            print("faça a conexão")

    def insert_produto(self, codgProd, descricaoProd, equipamento, qntProd):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO produtos(codgProd, descricaoProd, equipamento, qntProd) VALUES(?, ?, ?, ?)


            """, (codgProd, descricaoProd, equipamento, qntProd))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    #-----------Movimentação de estoque-----------------------

    def adicionar_produto(self, codgProd, qntProd):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                UPDATE produtos SET qntProd = qntProd + ? WHERE codgProd = ?

            """, (qntProd, codgProd))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def check_requisicao(self, codgProd):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM produtos;

            """)

            for linha in cursor.fetchall():
                if linha[0] == codgProd:
                    return "sim"
                else:
                    continue
            return "não"
        except:
            pass

    def retirar_produto(self, codgProd, qntProd):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                UPDATE produtos SET qntProd = qntProd - ? WHERE codgProd = ?

            """, (qntProd, codgProd))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    #---------OS------------------------------

    def create_table_OS(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""


                CREATE TABLE IF NOT EXISTS OS(

                    ordemServico TEXT NOT NULL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    equipamento TEXT NOT NULL,
                    estado TEXT NOT NULL

                );

            """)

        except AttributeError:
            print("faça a conexão")

    def insert_OS(self, ordemServico, nome, equipamento, estado):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO OS(ordemServico, nome, equipamento, estado) VALUES(?, ?, ?, ?)


            """, (ordemServico, nome, equipamento, estado))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def fechar_OS(self, numeroOS, estado):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                UPDATE OS SET estado = ? WHERE ordemServico = ?

            """, (estado, numeroOS))
            self.connection.commit()
        except AttributeError:
            print("faça a conexão")

    def check_abrir_os(self, codgOS):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM OS;

            """)

            for linha in cursor.fetchall():
                if linha[0] == codgOS:
                    return "não"
                else:
                    continue
            return "sim"
        except:
            pass

    def check_fechar_os(self, codgOS):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM OS;

            """)

            for linha in cursor.fetchall():
                if linha[0] == codgOS:
                    if linha[3] == "Aberto":
                        return "sim"
                    else:
                        return "fechado"
                else:
                    continue
            return "não"
        except:
            pass


if __name__ == "__main__":

    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table_equipamento()
    db.create_table_produto()
    db.create_table_OS()
    db.close_connection()












