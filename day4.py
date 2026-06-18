import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="backenddb",
    user="postgres",
    password="your_password"
)

print("Connected to database successfully!")


cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL
    )
""")

connection.commit()
print("Todos table created!")

# Insert a todo
cursor.execute("INSERT INTO todos (title) VALUES (%s)", ("Learn PostgreSQL",))
connection.commit()
print("Todo inserted!")

# Read it back
cursor.execute("SELECT * FROM todos")
todos = cursor.fetchall()
print("Todos:", todos)

# Close connection
cursor.close()
connection.close()