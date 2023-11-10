import sqlite3

def connect_database():
    conn = sqlite3.connect("C:\\Users\\gatsu\\Desktop\\Coding\\Python\\Prática de BD\\BD\\tp4.db")
    return conn

def create_tables(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS empresa (cnpj TEXT PRIMARY KEY, nome TEXT, num_funcionarios INTEGER NOT NULL);")
    c.execute("CREATE TABLE IF NOT EXISTS jogo (nome TEXT PRIMARY KEY, genero TEXT, empresa_resp TEXT, FOREIGN KEY(empresa_resp) REFERENCES empresa(cnpj));")
    c.execute("CREATE TABLE IF NOT EXISTS jogador (id TEXT PRIMARY KEY, nick TEXT UNIQUE, id_jogo TEXT, FOREIGN KEY(id_jogo) REFERENCES jogo(nome));")
    c.close()

def adicionar_empresa(conn, cnpj, nome, num_funcionarios):
    c = conn.cursor()
    c.execute("INSERT INTO empresa VALUES (?, ?, ?)", (cnpj, nome, num_funcionarios))
    conn.commit()
    c.close()

def adicionar_jogo(conn, nome, genero, empresa_resp):
    c = conn.cursor()
    c.execute("INSERT INTO jogo VALUES (?, ?, ?)", (nome, genero, empresa_resp))
    conn.commit()
    c.close()

def adicionar_jogador(conn, id, nick, id_jogo):
    c = conn.cursor()
    c.execute("INSERT INTO jogador VALUES (?, ?, ?)", (id, nick, id_jogo))
    conn.commit()
    c.close()
    

def remover_empresa(conn, cnpj):
    c = conn.cursor()
    c.execute("DELETE FROM empresa WHERE cnpj=?", (cnpj,))
    conn.commit()
    c.close()

def remover_jogo(conn, nome):
    c = conn.cursor()
    c.execute("DELETE FROM jogo WHERE nome=?", (nome,))
    conn.commit()
    c.close()

def remover_jogador(conn, id):
    c = conn.cursor()
    c.execute("DELETE FROM jogador WHERE id=?", (id,))
    conn.commit()
    c.close()

def atualizar_empresa(conn, novo_num_funcionarios, cnpj):
    c = conn.cursor()
    c.execute("UPDATE empresa SET num_funcionarios=? WHERE cnpj=?", (novo_num_funcionarios, cnpj))
    conn.commit()
    c.close()

def atualizar_jogo(conn, novo_genero, nome):
    c = conn.cursor()
    c.execute("UPDATE jogo SET genero=? WHERE nome=?", (novo_genero, nome))
    conn.commit()
    c.close()

def atualizar_jogador(conn, novo_nick, id):
    c = conn.cursor()
    c.execute("UPDATE jogador SET nick=? WHERE id=?", (novo_nick, id))
    conn.commit()
    c.close()
    
def pesquisar_empresa(conn, cnpj):
    c = conn.cursor()
    output = c.execute("SELECT * FROM empresa where cnpj=?", (cnpj,))
    for row in output:
        print(row)
    c.close()
    
def pesquisar_jogo(conn, nome):
    c = conn.cursor()
    output = c.execute("SELECT * FROM jogo where nome=?", (nome,))
    for row in output:
        print(row)
    c.close()
    
def pesquisar_jogador(conn, id):
    c = conn.cursor()
    output = c.execute("SELECT * FROM jogador where id=?", (id,))
    for row in output:
        print(row)
    c.close()
    
def inserir_array_jogo(conn, lista_jogos):
    c = conn.cursor()
    c.executemany("INSERT INTO jogo VALUES (?, ?, ?)", lista_jogos)
    conn.commit()
    c.close()
    
def buscar_jogos_empresas(conn, st):    # st = string
    c = conn.cursor()
    output = c.execute("SELECT * FROM empresa WHERE nome LIKE ?", ('%' + st + '%',))
    for row in output:
        print(row)
    c.close()

if __name__ == "__main__":
    conn = connect_database()
    create_tables(conn)
    adicionar_empresa(conn, "9310293", "Bethesda", 25)
    adicionar_jogo(conn, "Skyrim", "RPG", "9310293")
    adicionar_jogador(conn, "3784", "No0bMaster69", "45354")
    adicionar_jogador(conn, "7483", "Maqueico", "Minecraft")
    adicionar_jogador(conn, "3172", "Mamaco", "Overwatch")
    
    pesquisar_empresa(conn, "9310293")
    pesquisar_jogo(conn, "Skyrim")
    pesquisar_jogador(conn, "3784")
    
    remover_jogador(conn, "3784")
    
    atualizar_empresa(conn, 30, "9310293")
    atualizar_jogo(conn, "Aventura", "Minecraft")

    adicionar_empresa(conn, "3128371", "Nintendo", 43)
    adicionar_empresa(conn, "4327908", "Blizzard", 53)
    adicionar_empresa(conn, "4729387", "CD Projekt Red", 13)
    adicionar_empresa(conn, "9078095", "Rockstar", 29)
    adicionar_empresa(conn, "6578932", "Mojang", 80)
    
    jogos = [
    ["The Legend of Zelda", "Ação", "3128371"],
    ["Overwatch", "Tiro", "4327908"],
    ["The Witcher", "RPG", "4729387"],
    ["GTA", "Ação", "9078095"],
    ["Minecraft", "Sandbox", "6578932"]
    ]
    
    inserir_array_jogo(conn, jogos)
    
    buscar_jogos_empresas(conn, 'n')
    
    conn.close()

