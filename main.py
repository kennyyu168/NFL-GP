from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)

import script as sc
import os

# Set the port 
port = int(os.environ.get('PORT', 33507))

app = Flask(__name__, instance_relative_config=True, static_folder='static', static_url_path='/static')
@app.route('/', methods=['GET', 'POST'])
def main():
    """Gets the user input and tries to parse it.

    Returns:
      The rendered page for the result of user input.
    """
    
    # If something was entered i.e. post request
    if request.method == 'POST':
        
        # Reads in the request
        team_readin = request.form['teams']
        
        # Splits request down
        try: 
            split = team_readin.split(",")
            team1 = split[0].strip()
            team2 = split[1].strip()
	    
	    # Calls the main method to get the result
            try:
                result = sc.main(team1, team2)
                team1 = result[0]
                team2 = result[1]
                win = result[2]
                return render_template('index.html', team1=team1, team2=team2, win=win)
	    
	    except TypeError:
	        # Since result isn't good tell user to try again
	        team1 = "A team you've entered doesn't exist, please enter in the format 'Baltimore Ravens, San Francisco 49ers' "
	        return render_template('index.html', team1=team1, team2='', win=2)
	
	except IndexError:
	    # If only 1 team was entered
	    team1 = "Only 1 team was entered, please enter in the format 'Baltimore Ravens, San Francisco 49ers' "
	    return render_template('index.html', team1=team1, team2='', win=2) 
    
    # Else if calling home or loading for the first time
    else: 
        team1 = "Please enter in the format 'Baltimore Ravens, San Francisco 49ers' "
        return render_template('index.html', team1=team1, team2='', win=0)
    
@app.route("/butwhy")
def butwhy():
    """Launches the product explanation page.

    Returns:
      Rendered template for the 'but why' page.
    """
    return render_template('butwhy.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
