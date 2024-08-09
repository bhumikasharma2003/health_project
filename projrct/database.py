import sqlite3 
# to create a database and to create a table
conn = sqlite3.connect('mental_health.db')

query = """
create table project 
(Age Integer, Gender Integer , self_employed Integer, family_history Integer, treatment Integer,
       work_interfere Integer, no_employees Integer, remote_work Integer, tech_company Integer,
       benefits, care_options Integer, wellness_program Integer, seek_help Integer,
       anonymity Integer, leave Integer, mental_health_consequence Integer,
       phys_health_consequence Integer, coworkers Integer, mental_health_interview Integer,
       mental_vs_physical Integer, obs_consequence Integer)"""

query_to_fetch = """
select * from project
"""

# to create table 
cur = conn.cursor()  # cursor sql 
# cur.execute(query)
# print("Your database and your table is created!")

# to fetch the data from database 
cur.execute(query_to_fetch)
for record in cur.fetchall():
    print(record)


cur.close()
conn.close()

