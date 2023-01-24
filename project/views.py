from project import app
from project.functions import *
from flask import render_template, request

@app.route('/api/PnL')
def get_PnL_template_all_period():
    return render_template('PnL.html',
                           PnL = get_PnL_all_period(),
                           PnL_percent = get_PnL_percent_all_period(),
                           Index_PnL = get_Index_PnL_all_period(),
                           Period = get_all_period())
    
    # DataError
    # IndexError
    
@app.route('/api/PnL_custom_period', methods=['post', 'get'])
def get_PnL_form_custom_period():
    # message = 'Hiiii'
    if request.method == 'POST':
	    # username = request.form.get('username')  # запрос к данным формы
        # password = request.form.get('password')
        
        # if username == 'root' and password == 'pass':
	    #     message = "Correct username and password"
	    # message = f"{request.form.get('datetime_1')}"    
        try: 
            return render_template('custom_period_form.html',
                                PnL = get_PnL_custom_period(),
                                PnL_percent = get_PnL_percent_custom_period(),
                                Index_PnL = get_Index_PnL_custom_period(),
                                Period = get_custom_period())
        except Exception:
            return 'Wrong period selected'
    
    return render_template('custom_period_form.html')