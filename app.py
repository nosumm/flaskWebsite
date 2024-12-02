import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project1')
def project1():
    return render_template('project1.html')

@app.route('/project2')
def project2():
    return render_template('project2.html')

@app.route('/project3')
def project3():
    return render_template('project3.html')

@app.route('/project4')
def project4():
    return render_template('project4.html')
@app.route('/street-skating')
def street_skating():
    return render_template('street_skating.html')

@app.route('/park-skating')
def park_skating():
    return render_template('park_skating.html')

@app.route('/skate-camp')
def skate_camp():
    return render_template('skate_camp.html')
@app.route('/skate-camp/2023')
def skate_camp_2023():
    return render_template('skate_camp_2023.html')

@app.route('/skate-camp/2024')
def skate_camp_2024():
    return render_template('skate_camp_2024.html')

@app.route('/skate-camp/2025')
def skate_camp_2025():
    return render_template('skate_camp_2025.html')
@app.route('/travel/been')
def places_been():
    return render_template('places_been.html')

@app.route('/travel/going')
def places_going():
    return render_template('places_going.html')

@app.route('/travel/favorites')
def favorite_places():
    return render_template('favorite_places.html')
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    app.run(debug=True)