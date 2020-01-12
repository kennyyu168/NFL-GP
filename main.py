from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)

import script as sc

app = Flask(__name__, instance_relative_config=True, static_folder='static', static_url_path='/static')
@app.route('/', method=['GET', 'POST'])
def main():
    if request.method == 'POST':
        team_readin = request.form['teams']
        split = team_readin.split(", ")
        team1 = split[0]
        team2 = split[1]
        
    
    
    
@app.route("/butwhy")
def butwhy():
    return render_template('butwhy.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)