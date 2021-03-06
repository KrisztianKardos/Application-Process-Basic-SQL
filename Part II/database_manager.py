import psycopg2
from local_config import *


def query_manager(query, return_data='all_data'):
    '''
       Sets connection with the database and executes the queries.
       Decides what kind of data need to be returned.
    '''
    connect_str = 'dbname={0} user={1} password={2} host={3}'.format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(query)

    if return_data == 'all_data':
        data_from_query = cursor.fetchall()
        conn.close()
        return data_from_query
    elif return_data == 'no_data':
        conn.close()