from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    my_projects = ['stuff', 'things Iv Done', 'Appropreate things to say', 'stop being a dipp stick']
    return render_template('projects.html', projects=my_projects)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)