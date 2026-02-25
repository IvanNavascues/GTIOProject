import mysql.connector

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',  # Cambiar
    'password': '*Project26',  # Cambiar
    'database': 'votacion'
}

def create_database():
    
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='*Project26'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS votacion")
    conn.commit()
    cursor.close()
    conn.close()

def create_table():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            votes INT DEFAULT 0
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
    create_table()
    print("Base de datos y tabla creadas.")