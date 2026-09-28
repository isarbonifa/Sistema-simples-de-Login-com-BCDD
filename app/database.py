import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# Nome do arquivo de banco de dados que será criado automaticamente na pasta
DB_NAME = "database.db"


def get_db_connection():
  """Abre e retorna uma conexão com o SQLite local"""
  conn = sqlite3.connect(DB_NAME)
  # Isso permite acessar as colunas pelo nome do campo (ex: row['username'])
  conn.row_factory = sqlite3.Row
  return conn