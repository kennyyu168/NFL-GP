from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)

import script as sc

app = Flask(__name__, instance_relative_config=True, static_folder='static', static_url_path='/static')
@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If something was entered i.e. post request
    if request.method == 'POST':
        
        # Reads in the request
        team_readin = request.form['teams']
        
        # Splits request down
        split = team_readin.split(", ")
        team1 = split[0]
        team2 = split[1]
        
        # Calls the main method to get the result
        result = sc.main(team1, team2)
        team1 = result[0]
        team2 = result[1]
        win = result[2]
        return render_template('index.html', team1=team1, team2=team2, win=win)
    
    # Else if calling home or loading for the first time
    else: 
        team1 = "Please enter in the format 'Baltimore Ravens, San Francisco 49ers' "
        return render_template('index.html', team1=team1, team2='', win = 0)
    
    
@app.route("/butwhy")
def butwhy():
    return render_template('butwhy.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)