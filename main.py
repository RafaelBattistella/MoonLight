# Arquivos
from ui_login import Ui_Login
from ui_principal import Ui_MainWindow
from database import DataBase

# Biblioteca
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
import sys
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import webbrowser


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon('img/MoonLight.png')
        self.setWindowIcon(appIcon)

        self.check_tabelas()

        self.btn_login.clicked.connect(self.checkLogin)

    def check_tabelas(self):

        self.users = DataBase()
        self.users.conecta()
        self.users.create_table_users()

        checado = 'admin'
        autenticado = self.users.check_usuario(checado)

        if autenticado == "sim":

            self.users.table_users_first('Administrador', 'admin', 'admin', 'Administrador')
            self.users.create_table_equipamento()
            self.users.create_table_produto()
            self.users.create_table_OS()
        else:
            pass

    def checkLogin(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txtlogin.text(), self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":

            self.w = MainWindow(autenticado)
            self.w.show()
            self.close()
        else:

            if self.tentativas < 3:
                msg = QMessageBox()
                # msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                # bloquear o usuário
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("MoonLight")
        appIcon = QIcon('img/MoonLight.png')
        self.setWindowIcon(appIcon)

        if user == "user":
            self.bnt_Perfil.setVisible(False)
            self.lb_Perfil.setVisible(True)
        else:
            self.lb_Perfil.setVisible(False)
            self.bnt_Perfil.setVisible(True)

        # ----------------PG sistema___________________________________

        self.bnt_inicio.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_inicio))
        self.bnt_OS.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_OS))
        self.bnt_estoque.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_Estoque))
        self.bnt_Sobre.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_Sobre))
        self.bnt_cadastro.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_Cadastro))
        self.bt_fechaOs.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_FecgharOS))
        self.bt_abrirOs.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_AbrirOS))
        self.bt_requisicao.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_Requisicao))
        self.bt_pedido.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_Pedido))
        self.bt_Equipamento.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_equipamento))
        self.bt_Produto.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_produto))
        self.bnt_Perfil.clicked.connect(lambda: self.tl_geral.setCurrentWidget(self.tl_cadastro_User))

        self.bt_cadastraruser.clicked.connect(self.check_user)
        self.bt_enviar_produto.clicked.connect(self.subscribe_Produto)
        self.bt_enviar_equipamento.clicked.connect(self.subscribe_Equipamento)
        self.bt_requisicao_tabela.clicked.connect(self.check_requisicao)
        self.bt_add_pedido.clicked.connect(self.check_pedido)
        self.bt_linkedin.clicked.connect(self.abrir_link)
        self.bt_abrir_OS.clicked.connect(self.check_abrirOS)
        self.bt_fechar_os.clicked.connect(self.check_fecharOS)

        self.reset_table()

    def subscribe_user(self):

        if self.ed_senha_cadastro.text() != self.ed_senha2_cadastro.text():
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.warning)
            msg.setWindowTitle("Senhas divergentes")
            msg.setText("A senha não é igual")
            msg.exec()
            return None

        nome = self.ed_nome_cadastro.text()
        user = self.ed_usuario_cadastro.text()
        password = self.ed_senha_cadastro.text()
        access = self.cb_perfil_cadastro.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

    def check_user(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_usuario(self.ed_usuario_cadastro.text())

        if autenticado == "sim":
            self.subscribe_user()
        else:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao cadastrar")
            msg.setText(
                f'O usuário {self.ad_material_requisicao.text()} já cadastrado \n Por favor utilizar um outro usuário')
            msg.exec()

    # ------------Produto___________
    def subscribe_Produto(self):

        codg = self.ed_codg_produto.text()
        Equipamento = self.ed_equipamento_produto.text()
        descricao = self.ed_descricao_produto.text()
        qnt = 0

        db = DataBase()
        db.conecta()
        db.insert_produto(codg, descricao, Equipamento, qnt)
        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de produto")
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.ed_codg_produto.clear()
        self.ed_equipamento_produto.clear()
        self.ed_descricao_produto.clear()

        self.reset_table()

    def tabela_Produto(self):

        self.tb_produto.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_produto.setModel(self.model)
        self.model.setTable("produtos")
        self.model.select()

    # ------------Equipamento------------------
    def subscribe_Equipamento(self):

        codg = self.ed_codg_Equipamento.text()
        Equipamento = self.ed_material_Equipamento.text()

        db = DataBase()
        db.conecta()
        db.insert_equipamento(codg, Equipamento)
        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de produto")
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.ed_codg_Equipamento.clear()
        self.ed_material_Equipamento.clear()

        self.reset_table()

    def tabela_Equipamento(self):

        self.tb_equipamento.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_equipamento.setModel(self.model)
        self.model.setTable("equipamento")
        self.model.select()

    # ------------Requisição---------------------------------------------
    def atualizar_requisicao(self):

        codg = self.ad_material_requisicao.text()
        qnt = self.ed_qnt_requisicao
        qnt = int(qnt.text())

        db = DataBase()
        db.conecta()
        db.retirar_produto(codg, qnt)
        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Requisição")
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.ad_material_requisicao.clear()
        self.ed_qnt_requisicao.clear()

        self.reset_table()

    def tabela_requisicao(self):

        self.tb_produto.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_requisicao.setModel(self.model)
        self.model.setTable("produtos")
        self.model.select()

    def check_requisicao(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_requisicao(self.ad_material_requisicao.text())

        if autenticado == "sim":
            self.atualizar_requisicao()
        else:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao atualizar")
            msg.setText(
                f'O códgo {self.ad_material_requisicao.text()} não existe \n Por favor verifique o código ou cadastre o produto')
            msg.exec()

    # ----------Pedido--------------------------
    def atualizar_pedido(self):

        codg = self.ed_material_Pedido.text()
        qnt = self.ad_qnt_Pedido
        qnt = int(qnt.text())

        db = DataBase()
        db.conecta()
        db.adicionar_produto(codg, qnt)

        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Pedido")
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.ed_material_Pedido.clear()
        self.ad_qnt_Pedido.clear()

        self.reset_table()

    def check_pedido(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_requisicao(self.ed_material_Pedido.text())

        if autenticado == "sim":
            self.atualizar_pedido()
        else:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao atualizar")
            msg.setText(
                f'O códgo {self.ed_material_Pedido.text()} não existe \n Por favor verifique o código ou cadastre o produto')
            msg.exec()

    def tabela_pedido(self):

        self.tb_produto.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_pedido.setModel(self.model)
        self.model.setTable("produtos")
        self.model.select()

    # ---------------Utilitários----------------
    def abrir_link(self):

        webbrowser.open("https://www.linkedin.com/in/rafael-watanabe-battistella-082112162/")

    def reset_table(self):

        self.tabela_Equipamento()
        self.tabela_Produto()
        self.tabela_requisicao()
        self.tabela_pedido()
        self.tabela_fechar_OS()
        self.tabela_abrir_OS()

    # ------------OS------------------------
    def subscribe_OS(self):

        nome = self.ed_nome.text()
        ordemServico = self.ed_os.text()
        equipamento = self.ed_equipamento.text()
        estado = "Aberto"

        db = DataBase()
        db.conecta()
        db.insert_OS(ordemServico, nome, equipamento, estado)
        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de produto")
        msg.setText('Cadastro realizado com sucesso!')
        msg.exec()

        self.ed_nome.clear()
        self.ed_os.clear()
        self.ed_equipamento.clear()

        self.reset_table()

    def tabela_fechar_OS(self):

        self.tb_fecharOS.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_fecharOS.setModel(self.model)
        self.model.setTable("OS")
        filter_str = 'estado LIKE "Aberto"'
        self.model.setFilter(filter_str)
        self.model.select()

    def tabela_abrir_OS(self):

        self.tb_abrir_os.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_abrir_os.setModel(self.model)
        self.model.setTable("OS")
        self.model.select()

    def check_abrirOS(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_abrir_os(self.ed_os.text())

        if autenticado == "sim":
            self.subscribe_OS()
        else:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao atualizar")
            msg.setText(f'O códgo {self.ed_os.text()} Já existe \n Por favor verifique o código')
            msg.exec()

    def atualizar_OS(self):

        numeroOS = self.ed_os_fecharOS.text()
        estado = "Fechado"

        db = DataBase()
        db.conecta()
        db.fechar_OS(numeroOS, estado)

        db.close_connection()

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Pedido")
        msg.setText('OS finalizada com sucesso!')
        msg.exec()

        self.ed_os_fecharOS.clear()

        self.reset_table()

    def check_fecharOS(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_fechar_os(self.ed_os_fecharOS.text())

        if autenticado == "sim":
            self.atualizar_OS()
        elif autenticado == "fechado":
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao atualizar")
            msg.setText(f'A OS {self.ed_os_fecharOS.text()} já está fechada \n Por favor verifique a OS')
            msg.exec()
        else:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao atualizar")
            msg.setText(f'O códgo {self.ed_os_fecharOS.text()} não existe \n Por favor verifique o código')
            msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
