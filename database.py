import psycopg
import pandas as pd
import streamlit as st


def get_connection():
    return psycopg.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        dbname=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        sslmode="require"
    )


def get_participants():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM participants
                ORDER BY id;
            """)

            rows = cur.fetchall()

            columns = [
                description.name
                for description in cur.description
            ]

            return pd.DataFrame(rows, columns=columns)

def delete_participant(db_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM participants WHERE id = %s;",
                (db_id,)
            )
        conn.commit()

def delete_all_participants():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM participants;")
        conn.commit()