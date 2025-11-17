from PySide6.QtWidgets import *
import sys
from crud_empresas_funcionarios import *
from funcoes_crud_extras import *

#Empresas
class JanelaEmpresas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Empresas")
        self.setGeometry(100, 100, 400, 500)
        
        lay = QVBoxLayout()
        
        lay.addWidget(QLabel("Empresas"))
        
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID (para Editar/Excluir)")
        lay.addWidget(self.id_input)
        
        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome da Empresa")
        self.cnpj = QLineEdit()
        self.cnpj.setPlaceholderText("CNPJ")
        self.endereco = QLineEdit()
        self.endereco.setPlaceholderText("Endereço")
        
        lay.addWidget(self.nome)
        lay.addWidget(self.cnpj)
        lay.addWidget(self.endereco)
        
        self.busca_empresa = QLineEdit()
        self.busca_empresa.setPlaceholderText("Buscar empresa por nome...")
        lay.addWidget(QLabel("Buscar:"))
        lay.addWidget(self.busca_empresa)
        
        botao_buscar = QPushButton("Buscar")
        botao_buscar.clicked.connect(self.buscar_empresa)
        botao_criar = QPushButton("Criar")
        botao_criar.clicked.connect(self.criar_empresa)
        botao_editar = QPushButton("Editar")
        botao_editar.clicked.connect(self.editar_empresa)
        botao_excluir = QPushButton("Excluir")
        botao_excluir.clicked.connect(self.excluir_empresa)
        botao_listar = QPushButton("Listar")
        botao_listar.clicked.connect(self.listar_empresas)
        
        lay.addWidget(botao_buscar)
        lay.addWidget(botao_criar)
        lay.addWidget(botao_editar)
        lay.addWidget(botao_excluir)
        lay.addWidget(botao_listar)
        
        self.lista = QTextEdit()
        self.lista.setReadOnly(True)
        self.lista.setPlaceholderText("Resultados aparecerão aqui...")
        lay.addWidget(QLabel("Lista de Empresas:"))
        lay.addWidget(self.lista)
        
        self.setLayout(lay)
    
    def criar_empresa(self):
        nome = self.nome.text()
        cnpj = self.cnpj.text()
        endereco = self.endereco.text()
        
        if nome == "" or cnpj == "" or endereco == "":
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return
        
        if not validar_cnpj(cnpj):
            QMessageBox.warning(self, "Aviso", "CNPJ inválido!")
            return
        
        sucesso, mensagem = criar_empresa(nome, cnpj, endereco)
        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.id_input.clear()
            self.nome.clear()
            self.cnpj.clear()
            self.endereco.clear()
        else:
            QMessageBox.critical(self, "Erro", mensagem)
    
    def editar_empresa(self):
        id_empresa = self.id_input.text()
        nome = self.nome.text()
        cnpj = self.cnpj.text()
        endereco = self.endereco.text()
        
        if id_empresa == "":
            QMessageBox.warning(self, "Aviso", "Informe o ID da empresa para editar!")
            return
        
        if nome == "" or cnpj == "" or endereco == "":
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return
        
        if not validar_cnpj(cnpj):
            QMessageBox.warning(self, "Aviso", "CNPJ inválido!")
            return
        
        try:
            id_empresa = int(id_empresa)
        except:
            QMessageBox.warning(self, "Aviso", "ID deve ser um número!")
            return
        
        sucesso, mensagem = editar_empresa(id_empresa, nome, cnpj, endereco)
        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.id_input.clear()
            self.nome.clear()
            self.cnpj.clear()
            self.endereco.clear()
        else:
            QMessageBox.critical(self, "Erro", mensagem)
    
    def excluir_empresa(self):
        id_empresa = self.id_input.text()
        
        if id_empresa == "":
            QMessageBox.warning(self, "Aviso", "Informe o ID da empresa para excluir!")
            return
        
        try:
            id_empresa = int(id_empresa)
        except:
            QMessageBox.warning(self, "Aviso", "ID deve ser um número!")
            return
        
        resposta = QMessageBox.question(self, "Confirmar", 
                                       f"Tem certeza que deseja excluir a empresa ID {id_empresa}?",
                                       QMessageBox.Yes | QMessageBox.No)
        
        if resposta == QMessageBox.Yes:
            sucesso, mensagem = excluir_empresa(id_empresa)
            if sucesso:
                QMessageBox.information(self, "Sucesso", mensagem)
                self.id_input.clear()
                self.nome.clear()
                self.cnpj.clear()
                self.endereco.clear()
            else:
                QMessageBox.critical(self, "Erro", mensagem)
    
    def listar_empresas(self):
        sucesso, resultado = listar_empresas()
        if sucesso:
            if resultado:
                texto = "ID | Nome | CNPJ | Endereço\n"
                texto += "-" * 50 + "\n"
                for emp in resultado:
                    texto += f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]}\n"
                self.lista.setText(texto)
            else:
                self.lista.setText("Nenhuma empresa cadastrada.")
        else:
            QMessageBox.critical(self, "Erro", resultado)
    
    def buscar_empresa(self):
        nome_busca = self.busca_empresa.text()
        if nome_busca == "":
            QMessageBox.warning(self, "Aviso", "Digite um nome para buscar!")
            return
        
        resultado = buscar_empresa_por_nome(nome_busca)
        if resultado:
            texto = "ID | Nome | CNPJ | Endereço\n"
            texto += "-" * 50 + "\n"
            for emp in resultado:
                texto += f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]}\n"
            self.lista.setText(texto)
        else:
            self.lista.setText("Nenhuma empresa encontrada.")

#Funcionários
class JanelaFuncionarios(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Funcionários")
        self.setGeometry(550, 100, 400, 500)
        
        lay = QVBoxLayout()
        
        lay.addWidget(QLabel("Funcionários"))
        
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID (para Editar/Excluir)")
        lay.addWidget(self.id_input)
        
        self.nome_f = QLineEdit()
        self.nome_f.setPlaceholderText("Nome do Funcionário")
        self.cargo_f = QLineEdit()
        self.cargo_f.setPlaceholderText("Cargo")
        self.sal_f = QLineEdit()
        self.sal_f.setPlaceholderText("Salário")
        self.empresa_f = QLineEdit()
        self.empresa_f.setPlaceholderText("ID da Empresa")
        
        lay.addWidget(self.nome_f)
        lay.addWidget(self.cargo_f)
        lay.addWidget(self.sal_f)
        lay.addWidget(self.empresa_f)
        
        self.busca_funcionario = QLineEdit()
        self.busca_funcionario.setPlaceholderText("Buscar funcionário por nome...")
        lay.addWidget(QLabel("Buscar:"))
        lay.addWidget(self.busca_funcionario)
        
        botao_buscar = QPushButton("Buscar")
        botao_buscar.clicked.connect(self.buscar_funcionario)
        botao_exportar = QPushButton("Exportar CSV")
        botao_exportar.clicked.connect(self.exportar_csv)
        botao_criar = QPushButton("Criar")
        botao_criar.clicked.connect(self.criar_funcionario)
        botao_editar = QPushButton("Editar")
        botao_editar.clicked.connect(self.editar_funcionario)
        botao_excluir = QPushButton("Excluir")
        botao_excluir.clicked.connect(self.excluir_funcionario)
        botao_listar = QPushButton("Listar")
        botao_listar.clicked.connect(self.listar_funcionarios)
        
        lay.addWidget(botao_buscar)
        lay.addWidget(botao_exportar)
        lay.addWidget(botao_criar)
        lay.addWidget(botao_editar)
        lay.addWidget(botao_excluir)
        lay.addWidget(botao_listar)
        
        self.lista = QTextEdit()
        self.lista.setReadOnly(True)
        self.lista.setPlaceholderText("Resultados aparecerão aqui...")
        lay.addWidget(QLabel("Lista de Funcionários:"))
        lay.addWidget(self.lista)
        
        self.setLayout(lay)
    
    def criar_funcionario(self):
        nome = self.nome_f.text()
        cargo = self.cargo_f.text()
        salario = self.sal_f.text()
        empresa_id = self.empresa_f.text()
        
        if nome == "" or cargo == "" or salario == "" or empresa_id == "":
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return
        
        try:
            salario = float(salario)
            empresa_id = int(empresa_id)
        except:
            QMessageBox.warning(self, "Aviso", "Salário deve ser um número e Empresa ID deve ser um número inteiro!")
            return
        
        sucesso, mensagem = criar_funcionario(nome, cargo, salario, empresa_id)
        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.id_input.clear()
            self.nome_f.clear()
            self.cargo_f.clear()
            self.sal_f.clear()
            self.empresa_f.clear()
        else:
            QMessageBox.critical(self, "Erro", mensagem)
    
    def editar_funcionario(self):
        id_funcionario = self.id_input.text()
        nome = self.nome_f.text()
        cargo = self.cargo_f.text()
        salario = self.sal_f.text()
        empresa_id = self.empresa_f.text()
        
        if id_funcionario == "":
            QMessageBox.warning(self, "Aviso", "Informe o ID do funcionário para editar!")
            return
        
        if nome == "" or cargo == "" or salario == "" or empresa_id == "":
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")
            return
        
        try:
            id_funcionario = int(id_funcionario)
            salario = float(salario)
            empresa_id = int(empresa_id)
        except:
            QMessageBox.warning(self, "Aviso", "IDs devem ser números inteiros e Salário deve ser um número!")
            return
        
        sucesso, mensagem = editar_funcionario(id_funcionario, nome, cargo, salario, empresa_id)
        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.id_input.clear()
            self.nome_f.clear()
            self.cargo_f.clear()
            self.sal_f.clear()
            self.empresa_f.clear()
        else:
            QMessageBox.critical(self, "Erro", mensagem)
    
    def excluir_funcionario(self):
        id_funcionario = self.id_input.text()
        
        if id_funcionario == "":
            QMessageBox.warning(self, "Aviso", "Informe o ID do funcionário para excluir!")
            return
        
        try:
            id_funcionario = int(id_funcionario)
        except:
            QMessageBox.warning(self, "Aviso", "ID deve ser um número!")
            return
        
        resposta = QMessageBox.question(self, "Confirmar", 
                                       f"Tem certeza que deseja excluir o funcionário ID {id_funcionario}?",
                                       QMessageBox.Yes | QMessageBox.No)
        
        if resposta == QMessageBox.Yes:
            sucesso, mensagem = excluir_funcionario(id_funcionario)
            if sucesso:
                QMessageBox.information(self, "Sucesso", mensagem)
                self.id_input.clear()
                self.nome_f.clear()
                self.cargo_f.clear()
                self.sal_f.clear()
                self.empresa_f.clear()
            else:
                QMessageBox.critical(self, "Erro", mensagem)
    
    def listar_funcionarios(self):
        sucesso, resultado = listar_funcionarios()
        if sucesso:
            if resultado:
                texto = "ID | Nome | Cargo | Salário | Empresa\n"
                texto += "-" * 60 + "\n"
                for func in resultado:
                    texto += f"{func[0]} | {func[1]} | {func[2]} | R$ {func[3]} | {func[4] if func[4] else 'N/A'}\n"
                self.lista.setText(texto)
            else:
                self.lista.setText("Nenhum funcionário cadastrado.")
        else:
            QMessageBox.critical(self, "Erro", resultado)
    
    def buscar_funcionario(self):
        nome_busca = self.busca_funcionario.text()
        if nome_busca == "":
            QMessageBox.warning(self, "Aviso", "Digite um nome para buscar!")
            return
        
        resultado = buscar_funcionario_por_nome(nome_busca)
        if resultado:
            texto = "ID | Nome | Cargo | Salário | Empresa\n"
            texto += "-" * 60 + "\n"
            for func in resultado:
                texto += f"{func[0]} | {func[1]} | {func[2]} | R$ {func[3]} | {func[4] if func[4] else 'N/A'}\n"
            self.lista.setText(texto)
        else:
            self.lista.setText("Nenhum funcionário encontrado.")
    
    def exportar_csv(self):
        caminho, _ = QFileDialog.getSaveFileName(self, "Salvar CSV", "", "CSV Files (*.csv)")
        if caminho:
            try:
                exportar_funcionarios_csv(caminho)
                QMessageBox.information(self, "Sucesso", "Funcionários exportados com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao exportar: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    janela_empresas = JanelaEmpresas()
    janela_empresas.show()
    
    janela_funcionarios = JanelaFuncionarios()
    janela_funcionarios.show()
    
    sys.exit(app.exec())
