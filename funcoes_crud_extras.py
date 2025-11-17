import re
import csv
from bancodedados import conectar

def validar_cnpj(cnpj):
    s = re.sub(r'\D', '', cnpj)
    if len(s) != 14 or s == s[0] * 14:
        return False

    def calc(digs):
        soma = 0
        p = len(digs) - 7
        for i, d in enumerate(digs):
            soma += int(d) * (p - i if p - i > 1 else 9 - (i - (len(digs) - 1)))
        r = soma % 11
        return '0' if r < 2 else str(11 - r)

    v1 = calc(s[:12])
    v2 = calc(s[:12] + v1)
    return s.endswith(v1 + v2)


def exportar_funcionarios_csv(caminho):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT f.id, f.nome, f.cargo, f.salario, f.empresa_id, e.nome
        FROM funcionarios f
        LEFT JOIN empresas e ON f.empresa_id = e.id
    """)
    rows = cur.fetchall()
    cur.close()
    con.close()

    with open(caminho, "w", newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(["id","nome","cargo","salario","empresa_id","empresa_nome"])
        w.writerows(rows)


def buscar_empresa_por_nome(nome):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM empresas WHERE nome LIKE %s", (f"%{nome}%",))
    empresas = cur.fetchall()
    cur.close()
    con.close()
    return empresas


def buscar_funcionario_por_nome(nome):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT f.id, f.nome, f.cargo, f.salario, e.nome as empresa_nome 
        FROM funcionarios f 
        LEFT JOIN empresas e ON f.empresa_id = e.id 
        WHERE f.nome LIKE %s
    """, (f"%{nome}%",))
    funcionarios = cur.fetchall()
    cur.close()
    con.close()
    return funcionarios