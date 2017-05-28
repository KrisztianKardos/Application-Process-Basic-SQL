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


@app.route('/all-school')
def all_school():
    table_headers = [
                    'First name',
                    'Last name',
                    'School name',
                    'Country'
                    ]
    query = all_school_query
    all_school_data = query_manager(query, return_data='all_data')
    return render_template('all-school.html', table_headers=table_headers, all_school_data=all_school_data)


@app.route('/mentors-by-country')
def mentors_by_country():
    table_headers = [
                    'Country',
                    'Count'
                    ]
    query = mentors_by_country_query
    mentors_by_country_data = query_manager(query, return_data='all_data')
    return render_template('mentors-by-country.html', table_headers=table_headers, mentors_by_country_data=mentors_by_country_data)


@app.route('/contacts')
def contacts():
    table_headers = [
                    'School name',
                    'First name',
                    'Last name'
                    ]
    query = contacts_query
    contacts_data = query_manager(query, return_data='all_data')
    return render_template('contacts.html', table_headers=table_headers, contacts_data=contacts_data)


@app.route('/applicants')
def applicants():
    table_headers = [
                    'First name',
                    'Application code',
                    'Creation date'
                    ]
    query = applicants_query
    applicants_data = query_manager(query, return_data='all_data')
    return render_template('applicants.html', table_headers=table_headers, applicants_data=applicants_data)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    table_headers = [
                    'First name',
                    'Application code',
                    'Mentor First name',
                    'Mentor Last name'
                    ]
    query = applicants_and_mentors_query
    applicants_and_mentors_data = query_manager(query, return_data='all_data')
    return render_template('applicants-and-mentors.html', table_headers=table_headers, applicants_and_mentors_data=applicants_and_mentors_data)


if __name__ == '__main__':
    app.run(debug=True)
