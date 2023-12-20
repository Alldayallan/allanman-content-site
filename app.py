from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Francisco, California',
    'salary': '$100,000 - $120,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'San Francisco, California',
    'salary': '$120,000 - $160,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'San Francisco, California',
}, {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'San Francisco, California',
    'salary': '$120,000 - $165,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='AllanMan')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
