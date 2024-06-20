import sqlite3
import os

def conectar_db(db_path):
    """Estabelece uma conexão com o banco de dados SQLite especificado."""
    return sqlite3.connect(db_path)

def listar_tabelas(conn):
    """Retorna uma lista de todas as tabelas no banco de dados."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [tabela[0] for tabela in cursor.fetchall()]

def main():
    print("Bem-vindo ao Table Trimmer!")
    db_path = input("Digite o caminho para o arquivo de banco de dados SQLite: ")
    conn = conectar_db(db_path)

    tabelas = listar_tabelas(conn)
    print("Tabelas disponíveis no banco de dados:")
    for idx, tabela in enumerate(tabelas, start=1):
        print(f"{idx}. {tabela}")

    # Mais funcionalidade aqui...

    conn.close()

if __name__ == '__main__':
    main()
