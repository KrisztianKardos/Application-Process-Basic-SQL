"""SQL handling module"""


mentors_query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                FROM mentors\
                LEFT JOIN schools\
                ON mentors.city = schools.city\
                ORDER BY mentors.id ASC;"""

all_school_query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                    FROM mentors\
                    RIGHT OUTER JOIN schools\
                    ON mentors.city = schools.city\
                    ORDER BY mentors.id ASC;"""

mentors_by_country_query = """SELECT schools.country,\
                            COUNT(mentors.id) AS Number_of_mentors\
                            FROM mentors\
                            LEFT JOIN schools\
                            ON mentors.city = schools.city\
                            GROUP BY country;"""
