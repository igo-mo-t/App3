from project import app
from project.functions import *
from flask import render_template, request

@app.route('/api/PnL')
def get_PnL_template_all_period():
    """
    По GET запросу возвращает html шаблон с PnL, PnL_%, Index_PnL, Period(UTC),
    рассчитанными за весь период работы приложения.
    """
    return render_template('PnL.html',
                           PnL = get_PnL_all_period(),
                           PnL_percent = get_PnL_percent_all_period(),
                           Index_PnL = get_Index_PnL_all_period(),
                           Period = get_all_period())
    
   
    
@app.route('/api/PnL_custom_period', methods=['post', 'get'])
def get_PnL_form_custom_period():
    """
    По GET запросу возвращает html шаблон формы,
    в которой можно ввести начало и конец кастомного периода в UTC часовом поясе для расчета PnL
    
    При методе POST возвращает html шаблон с рассчитанными PnL, PnL_%, Index_PnL, Period(UTC)
    за кастомный(выбранный) период работы приложения.
    
    В случае неверно выбранного периода, или периода, когда приложение не работало 
    и расчеты не производились, вернет сообщение 'Wrong period selected'
    """
    if request.method == 'POST':
        try: 
            return render_template('custom_period_form.html',
                                PnL = get_PnL_custom_period(),
                                PnL_percent = get_PnL_percent_custom_period(),
                                Index_PnL = get_Index_PnL_custom_period(),
                                Period = get_custom_period())
        except Exception:
            return 'Wrong period selected'

    return render_template('custom_period_form.html')