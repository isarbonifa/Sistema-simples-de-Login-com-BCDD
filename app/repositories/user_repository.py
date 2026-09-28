from app.database import get_db_connection


class UserRepository:

  @staticmethod
  def get_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, password FROM usuarios WHERE username = ?",
        (username,),
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
      # Como usamos sqlite3.Row, podemos retornar como dicionário
      return {"id": row["id"], "username": row["username"], "password": row["password"]}
    return None

  @staticmethod
  def create(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)",
        (username, password),
    )

    conn.commit()
    cursor.close()
    conn.close()