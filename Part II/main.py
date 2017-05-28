from flask import Flask, render_template, redirect, request
import psycopg2
from queries import *
from database_manager import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors():
    table_headers = [
                    'First name',
                    'Last name',
                    'School name',
                    'Country'
                    ]
    query = mentors_query
    mentors_data = query_manager(query, return_data='all_data')
    return render_template('mentors.html', table_headers=table_headers, mentors_data=mentors_data)


if __name__ == '__main__':
    app.run(debug=True)