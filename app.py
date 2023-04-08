from flask import Flask, render_template, session, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import *


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "never-tell"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

from converter import Currency 



@app.route('/')
def main_page():
    """ load main page """

    return render_template("home.html")


@app.route('/results', methods = ["POST"])
def results():
    """ Calculates conversion from initial currency to a
    new one based on the amount"""  

    first = request.form.get("first")
    final = request.form.get("final")
    amount = request.form.get("amount", type=float)
    
    curr = Currency(first, final, amount)

    if amount is None:
        alert = "not a valid amount."
        flash(alert)
        return redirect('/')
 
    try:
        converce = curr.convert_amount(first, final, amount)
        result = round(converce, 2)
        result_symbol = curr.curr_symbol(final)
        return render_template('/results.html', result=result, result_symbol=result_symbol )
        
    except (NameError, RatesNotAvailableError):
        flash("Please enter a valid currency")
        return redirect('/')

    except (ValueError, TypeError):
        flash("pleas Check all values")
        return redirect('/')