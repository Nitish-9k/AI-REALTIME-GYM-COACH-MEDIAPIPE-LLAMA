import sqlite3
import streamlit as st 
from pathlib import Path

_DB_PATH=str(Path(__file__).parent.parent.parent/"data.db")


@st.cache_resource
def _get_connection():
    conn=sqlite3.connect(_DB_PATH,check_same_thread=False)
    conn.row_factory=sqlite3.Row
    return conn



def __init_db():
    conn=_get_connection()
    with conn:

        conn.execute("""
              CREATE TABLE IF NOT EXISTS users(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT UNIQUE NOT NULL,
                     ceated_at TIMESTAMP DEFUALT CURRENT_TIMESTAMP
                     )              
             """)
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS exercises(
                     id INTEGR PRIMARY KEY,
                     user_id INTEGER NOT NULL REFERENCES USER(id),
                     exercise_name TEXT NOT_NULL,
                     reps INTEGER NOT NULL DEFUALT 0,
                     reps INTEGER NOT NULL DEFUALT 0,
                     sets integr NOT NULL DEFUALT 0,
                     )      
                """)
        

    # authentication fxns
    

def get_user(username):
        conn=_get_connection()

        return conn.execute("""
                SELECT * FROM users WHERE useranme=?
            """,(username)).fetchone()
    

    
def create_user(username):
     conn=_get_connection()
     with conn:
          conn.execute("""
            INSERT INTO users(username) Values(?)
                       """(username))


        


