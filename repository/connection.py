import psycopg2

# This file is used to define a function to get the database connection

def get_connection():
    connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="admindata",
            host="project1-database.cgj5gn7ymodb.us-east-1.rds.amazonaws.com",
            port="5432"
    )

    return connection
