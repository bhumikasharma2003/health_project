from flask import Flask, render_template,request, url_for
import sqlite3
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

random_forest = joblib.load(r'./models/randomforest.lb')

app = Flask(__name__)
data_insert_query = """r
insert into project ('Age', 'Gender', 'self_employed', 'family_history', 'treatment',
       'work_interfere', 'no_employees', 'remote_work', 'tech_company',
       'benefits', 'care_options', 'wellness_program', 'seek_help',
       'anonymity', 'leave', 'mental_health_consequence',
       'phys_health_consequence', 'coworkers', 'mental_health_interview',
       'mental_vs_physical', 'obs_consequence')
values(?,?,?,?,?,?,?,?)
"""
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")  

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    if request.method == "POST":
        #to receive the data
        Age = int(request.form["age"])
        Gender = int(request.form["gender"])
        self_employed = int(request.form["self_employed"]) 
        family_history = int(request.form["family_history"]) 
        #treatment = int(request.form["treatment"]) 
        work_interfere = int(request.form["work_interfere"]) 
        no_employees = int(request.form["no_employees"]) 
        remote_work = int(request.form["remote_work"]) 
        tech_company = int(request.form["tech_company"])  
        benefits = int(request.form["benefits"])
        care_option = int(request.form["care_options"])
        wellness_program = int(request.form["wellness_program"]) 
        seek_help = int(request.form["seek_help"])
        anonymity = int(request.form["anonymity"]) 
        leave = int(request.form["leave"]) 
        mental_health_consequences = int(request.form["mental_health_consequences"]) 
        phys_health_consequences = int(request.form["phys_health_consequences"]) 
        coworkers = int(request.form["coworkers"])
        mental_health_interview = int(request.form["mental_health_interview"]) 
        mental_vs_physical = int(request.form["mental_vs_physical"])  
        obs_consequence= int(request.form["obs_consequence"]) 
        

        unseen_data = [[Age,Gender,self_employed,family_history,work_interfere,no_employees,remote_work,tech_company,benefits,care_option,wellness_program,seek_help,anonymity,leave,mental_health_consequences,phys_health_consequences,coworkers,mental_health_interview,mental_vs_physical,obs_consequence]]
        prediction =random_forest.predict(unseen_data)[0]
        
        print(prediction)
        conn = sqlite3.connect('mental_health.db')
        cur = conn.cursor()
        if prediction==0:
               return " your prediction is here : no"
        else:
               return "your prediction is here : yes"
        #print(final)
    for record in cur.fetchall():
         print(prediction)
           
    return render_template('final.html' , output=prediction)
    cur.close()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)