from project import app
from project.functions import *
from flask import render_template

@app.route('/api/PnL')
def get_PnL_template_all_period():
    return render_template('PnL.html',
                           PnL = get_PnL_all_period(),
                           PnL_percent = get_PnL_percent_all_period(),
                           Index_PnL = get_Index_PnL_all_period(),
                           Period = get_all_period())