import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/Travel')
def travel():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC').fetchall()
    conn.close()
    return render_template('travel.html', posts=posts)

@app.route('/Skateboarding')
def skateboarding():
    return render_template('skateboarding.html')

@app.route('/Software Engineering')
def swe():
    return render_template('swe.html')

@app.route('/homeowner')
def homeowner():
    return render_template('homeowner.html')

@app.route('/maui2024')
def maui2024():
    return render_template('maui2024.html')

@app.route('/guatemala2024')
def guat2024():
    return render_template('guat2024.html')

@app.route('/turk2023')
def turk2023():
    return render_template('turk2023.html')

@app.route('/italy2023')
def italy2023():
    return render_template('italy2023.html')

@app.route('/cdmx2023')
def cdmx2023():
    return render_template('cdmx2023.html')

@app.route('/ireland2023')
def ireland2023():
    return render_template('ireland2023.html')

@app.route('/irelandmalta2022')
def iremalta2022():
    return render_template('iremalta2022.html')

@app.route('/tulum2020')
def tulum2020():
    return render_template('tulum2020.html')
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