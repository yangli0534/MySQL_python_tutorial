# -*- coding: utf-8 -*-

"""
@author: Leon
@time: 2021-04-27

"""

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        #user=input("Enter username: "),
        #password=getpass("Enter password: "),
        user='root',
        password='oppaha89',
        database='online_movie_rating',
    ) as connection:
        print(connection)

        # # CREATE NEW DATABASE
        # create_db_query = "CREATE DATABASE online_movie_rating"
        # with connection.cursor() as cursor:
        #     cursor.execute(create_db_query)

        # # SHOW DATABAE
        # show_db_query = "SHOW DATABASES"
        # with connection.cursor() as cursor:
        #     cursor.execute(show_db_query)
        #     for db in cursor:
        #         print(db)

        # # CREATE TABLE
        # create_movies_table_query = """
        # CREATE TABLE movies(
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     title VARCHAR(100),
        #     release_year YEAR(4),
        #     genre VARCHAR(100),
        #     collection_in_mil INT
        # )
        # """
        # with connection.cursor() as cursor:
        #     cursor.execute(create_movies_table_query)
        #     connection.commit()
        #
        # create_reviewers_table_query = """
        # CREATE TABLE reviewers (
        #     id INT AUTO_INCREMENT PRIMARY KEY,
        #     first_name VARCHAR(100),
        #     last_name VARCHAR(100)
        # )
        # """
        # with connection.cursor() as cursor:
        #     cursor.execute(create_reviewers_table_query)
        #     connection.commit()
        #
        # create_ratings_table_query = """
        # CREATE TABLE ratings (
        #     movie_id INT,
        #     reviewer_id INT,
        #     rating DECIMAL(2,1),
        #     FOREIGN KEY(movie_id) REFERENCES movies(id),
        #     FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        #     PRIMARY KEY(movie_id, reviewer_id)
        # )
        # """
        # with connection.cursor() as cursor:
        #     cursor.execute(create_ratings_table_query)
        #     connection.commit()

        # show_table_query = "DESCRIBE movies"
        # with connection.cursor() as cursor:
        #     cursor.execute(show_table_query)
        #     # Fetch rows from last executed query
        #     result = cursor.fetchall()
        #     for row in result:
        #         print(row)


except Error as e:
    print(e)
