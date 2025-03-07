import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

DB_API_KEY = os.getenv("DB_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash"


class QuerySQL(BaseModel):
    query: str


def conn_db():
    result = urlparse(DB_API_KEY)

    conn = psycopg2.connect(
        dbname=result.path[1:],  # Elimina la primera "/"
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port,
        sslmode="require",
    )

    return conn


def get_tables(cursor):
    cursor.execute(
        """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """
    )
    return cursor.fetchall()


def get_structure_tables(cursor, tables):
    db_structure = ""

    for table in tables:
        table_name = table[0]
        db_structure += f"Table: {table_name}\n"
        cursor.execute(
            f"""
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = %s;
        """,
            (table_name,),
        )
        columns = cursor.fetchall()
        for column in columns:
            db_structure += (
                f"  Column: {column[0]}, Type: {column[1]}, Nullable: {column[2]}\n"
            )
        db_structure += "\n"

    return db_structure


def query_openai(db_structure, user_prompt):
    system_prompt = """
    Vas a ser un experto de SQL.
    Cualquier consulta que se te haga, tienes que convertirla a una consulta SQL. Tienes que responder únicamente con la consulta SQL.
    Esta es la información de la estructura de las tablas de la base de datos:\n
    """
    system_prompt += db_structure

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=f"{system_prompt}\n\nQuery: {user_prompt}",
            config={
                "response_mime_type": "application/json",
                "response_schema": QuerySQL,
            },
        )
        query = response.parsed.query

        return query
    except Exception as e:
        print("Ocurrió un error:", e)


def query_db(cursor, query):
    try:
        cursor.execute(query)
        response = cursor.fetchall()
        print(response)
    except Exception as e:
        print("ERROR: Realizaste una consulta incorrecta")


def get_user_prompt():
    user_prompt = input("Query: ")
    return user_prompt


if __name__ == "__main__":
    try:
        conn = conn_db()
        cursor = conn.cursor()

        tables = get_tables(cursor)
        db_structure = get_structure_tables(cursor, tables)

        user_prompt = get_user_prompt()

        query = query_openai(db_structure, user_prompt)
        query_db(cursor, query)

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
