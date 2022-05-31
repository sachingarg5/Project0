import psycopg2
from repository.connection import get_connection
from models.user_info_dto import User
from models.job_dto import Job

def select_job_by_id(info_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM job_info WHERE info_id = {info_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchall()
            if record is None:
                break
            # job_info = Job(record[0], record[1], record[2],record[3], record[4], record[5])
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def insert_job_info(user_dto: User, job_type: str, description: str, budget:int,contact:str):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO job_info VALUES (default, %s, %s, %s, %s, %s) RETURNING job_id;"

    try:
        cursor.execute(qry, (user_dto.info_id, job_type, description, budget, contact))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()