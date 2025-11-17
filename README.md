# CRUD-PySide-6
Criei essa aplicação em Python usando o PySide6 para a interface gráfica e MySQLWorkbench para o banco de dados, a aplicação permite cadastrar, editar, listar e excluir empresas e funcionários. 
# Sistema CRUD de Empresas e Funcionários

**Atenção:**  
Recomendo usar o **Python 3.10** para rodar este projeto, pois o **PySide6** não funciona no Python 3.14.

## O que você precisa ter instalado

- Python 3.10 (recomendado) ou outra versão compatível
- MySQLWorkbench ou PostgreSQL configurado e rodando na sua máquina
- Algumas bibliotecas Python, que mostrarei no guia

## Como começar

### 1. Instalar as bibliotecas

Abra o terminal na pasta do seu projeto e rode o comando abaixo:

```bash
pip install PySide6 mysql-connector-python
```

Ou se você estiver tiver baixado o Python 3.10 e tem mais de uma versão dele, use:

```bash
py -3.10 -m pip install PySide6 mysql-connector-python
```

### 2. Criar o banco de dados

Agora, você precisa criar o banco de dados no MySQL. Abra o MySQL e execute o arquivo **crud_empresas.sql** que está na pasta do projeto, ele vai criar as tabelas que o sistema precisa.

### 3. Configurar suas credenciais

Nunca coloque suas informações diretamente no arquivo de integração com o banco de dados se for publicar seu projeto, crie em um outro arquivo **config.py** que não vai para o Git, por questão segurança, ele contém a senha do banco de dados.

No arquivo **config.py** use o seguinte modelo nele:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "SUA_SENHA_DO_MYSQL/POSTGRESQL_AQUI"
DB_DATABASE = "crud_empresas"
```

### 4. Rodar o programa

Agora que tudo está configurado, só rodar o programa com um dos comandos abaixo:

```bash
python pyside.py
```

Ou caso queira rodar especificamente com o python 3.10:

```bash
py -3.10 pyside.py
```

Vão ser abertas duas janelas, uma para gerenciar as empresas e outra para os funcionários.

## Funcionalidades

### Empresas

- **Criar:** Preencha os campos (Nome, CNPJ, Endereço) e clique em "Criar".
- **Editar:** Coloque o ID da empresa, altere os campos que quiser e clique em "Editar".
- **Excluir:** Digite o ID da empresa e clique em "Excluir".
- **Listar:** Clique em "Listar" para ver todas as empresas cadastradas.
- **Buscar:** Digite um nome no campo de busca e clique em "Buscar" para encontrar empresas.

**Validação de CNPJ:** O sistema vai checar se o CNPJ está correto antes de salvar.

### Funcionários

- **Criar:** Preencha os campos (Nome, Cargo, Salário, ID da Empresa) e clique em "Criar".
- **Editar:** Coloque o ID do funcionário, altere os campos que precisar e clique em "Editar".
- **Excluir:** Digite o ID do funcionário e clique em "Excluir".
- **Listar:** Clique em "Listar" para ver todos os funcionários cadastrados.
- **Buscar:** Digite um nome no campo de busca e clique em "Buscar" para encontrar funcionários.

