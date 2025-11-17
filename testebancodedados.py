from bancodedados import conectar

con = conectar()
cur = con.cursor()

cur.execute("INSERT INTO empresas (nome, cnpj, endereco) VALUES (%s, %s, %s)",
            ("Teste", "00.000.000/0001-00", "Rua X"))

con.commit()

cur.execute("SELECT * FROM empresas")
print(cur.fetchall())

cur.close()
con.close()
