# coding:utf-8
from flask import Flask,render_template
import json

app = Flask(__name__)
print app.name
FILEPATH_JOB_SALARY = '../analysis/input/avg_salary.csv'
FILEPATH_CITY_SALARY = '../analysis/input/city_salary.json'
FILEPATH_CITY_SALARY_POS = '../analysis/input/city.json'


@app.route('/')
@app.route('/test1')
def test1():
    f = open(FILEPATH_JOB_SALARY)
    jobname,salary = zip(*map(lambda x: x.strip().split(','), f.readlines()))
    f.close()
    jobname = json.dumps(jobname)
    salary = map(float,salary)
    print(jobname,salary)
    # return render_template('job_salary.html',jobname=jobname,salary=salary)
    return render_template('index1.html',jobname=jobname,salary=salary)

@app.route('/job_salary/<job>')
def job_salary(job):
    f = open(FILEPATH_CITY_SALARY)
    js = json.load(f)
    return render_template('indexjob.html', data=js[job], name=job)

@app.route('/city_salary/<job>')
def city_salary(job):
    f = open(FILEPATH_CITY_SALARY_POS)
    js = json.load(f)
    points = filter(lambda x:x['city']==job,js)[0]['points']
    print points
    return render_template('heat_map.html', points=points, name=job)

if __name__ == '__main__':
    app.run()