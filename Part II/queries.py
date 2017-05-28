"""SQL handling module"""


mentors_query = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                FROM mentors\
                LEFT JOIN schools\
                ON mentors.city = schools.city\
                ORDER BY mentors.id ASC"

all_schools_query = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                FROM mentors\
                RIGHT OUTER JOIN schools\
                ON mentors.city = schools.city\
                ORDER BY mentors.id ASC"