from bancodedados import conectar

# ========== CRUD EMPRESAS ==========

def criar_empresa(nome, cnpj, endereco):
    """Cria uma nova empresa no banco de dados"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO empresas (nome, cnpj, endereco) VALUES (%s, %s, %s)",
                    (nome, cnpj, endereco))
        con.commit()
        cur.close()
        con.close()
        return True, "Empresa criada com sucesso!"
    except Exception as e:
        return False, f"Erro ao criar empresa: {str(e)}"

def listar_empresas():
    """Lista todas as empresas do banco de dados"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM empresas")
        empresas = cur.fetchall()
        cur.close()
        con.close()
        return True, empresas
    except Exception as e:
        return False, f"Erro ao listar empresas: {str(e)}"

def editar_empresa(id_empresa, nome, cnpj, endereco):
    """Edita uma empresa existente"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("UPDATE empresas SET nome=%s, cnpj=%s, endereco=%s WHERE id=%s",
                    (nome, cnpj, endereco, id_empresa))
        con.commit()
        cur.close()
        con.close()
        return True, "Empresa editada com sucesso!"
    except Exception as e:
        return False, f"Erro ao editar empresa: {str(e)}"

def excluir_empresa(id_empresa):
    """Exclui uma empresa do banco de dados"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM empresas WHERE id=%s", (id_empresa,))
        con.commit()
        cur.close()
        con.close()
        return True, "Empresa excluída com sucesso!"
    except Exception as e:
        return False, f"Erro ao excluir empresa: {str(e)}"

# ========== CRUD FUNCIONÁRIOS ==========

def criar_funcionario(nome, cargo, salario, empresa_id):
    """Cria um novo funcionário no banco de dados"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO funcionarios (nome, cargo, salario, empresa_id) VALUES (%s, %s, %s, %s)",
                    (nome, cargo, salario, empresa_id))
        con.commit()
        cur.close()
        con.close()
        return True, "Funcionário criado com sucesso!"
    except Exception as e:
        return False, f"Erro ao criar funcionário: {str(e)}"

def listar_funcionarios():
    """Lista todos os funcionários do banco de dados"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT f.id, f.nome, f.cargo, f.salario, e.nome as empresa_nome FROM funcionarios f LEFT JOIN empresas e ON f.empresa_id = e.id")
        funcionarios = cur.fetchall()
        cur.close()
        con.close()
        return True, funcionarios
    except Exception as e:
        return False, f"Erro ao listar funcionários: {str(e)}"

def editar_funcionario(id_funcionario, nome, cargo, salario, empresa_id):
    """Edita um funcionário existente"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("UPDATE funcionarios SET nome=%s, cargo=%s, salario=%s, empresa_id=%s WHERE id=%s",
                    (nome, cargo, salario, empresa_id, id_funcionario))
        con.commit()
        cur.close()
        con.close()
        return True, "Funcionário editado com sucesso!"
    except Exception as e:
        return False, f"Erro ao editar funcionário: {str(e)}"

def excluir_funcionario(id_funcionario):
    """Exclui um funcionário do banco de dados"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM funcionarios WHERE id=%s", (id_funcionario,))
        con.commit()
        cur.close()
        con.close()
        return True, "Funcionário excluído com sucesso!"
    except Exception as e:
        return False, f"Erro ao excluir funcionário: {str(e)}"

def listar_empresas_para_combo():
    """Retorna lista de empresas para usar em combobox"""
    try:
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT id, nome FROM empresas")
        empresas = cur.fetchall()
        cur.close()
        con.close()
        return True, empresas
    except Exception as e:
        return False, f"Erro ao listar empresas: {str(e)}"

