import os
import sys
import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class Database:
    """
    Manage MySQL database connection.
    """
    def __init__(self, db_name="Rebellion"):
        """
        Establish connection to database.
        :param db_name: name of database
        """
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database=db_name,
                                                      user='root',
                                                      password='')
            self.cursor = self.connection.cursor()
        except Error as error:
            print("Failed to connect to database: {}".format(error))

    def select(self, query):
        """
        Retrieves event from database.
        :param query: select query
        :return: event records
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        """
        Close connection to database.
        """
        self.cursor.close()
