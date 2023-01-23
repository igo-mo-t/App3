import requests
from project import db
from project.models import Сalculations


def get_uri_dollar_to_bitcoin():
    return 'https://test.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=future'


def get_dollar_to_bitcoin():
    res = requests.get(get_uri_dollar_to_bitcoin())
    dollar_to_bitcoin = [result['mark_price'] for result in res.json()['result'] 
                         if result['instrument_name'] == 'BTC-PERPETUAL']
    return dollar_to_bitcoin[0]


def get_uri_balance():
    return 'https://test.deribit.com/api/v2/private/get_account_summary?currency=BTC'


def get_net_asset_value():
    res = requests.get(get_uri_balance(),
                       headers={'Authorization': 
                           'Basic a1I5YTFEbVY6VERFU01icnJtbG1meHBCMWdNMGpxaEVNMEI5ZGlzZGRHOXZCbGdiZWJZaw=='})
    balance = res.json()['result']['balance']
    net_asset_value = balance * get_dollar_to_bitcoin()
    return net_asset_value


def get_PnL():
    last_net_asset_value = db.session.query(Сalculations.net_asset_value).order_by(Сalculations.id.desc()).first()
    PnL = get_net_asset_value() - last_net_asset_value[0]
    return PnL


def get_Index_PnL():
    last_net_asset_value = db.session.query(Сalculations.net_asset_value).order_by(Сalculations.id.desc()).first()
    last_Index_PnL = db.session.query(Сalculations.Index_PnL).order_by(Сalculations.id.desc()).first()
    Index_PnL = last_Index_PnL[0] * get_net_asset_value() / last_net_asset_value[0]      
    return Index_PnL    


def add_in_database():
    records = db.session.query(Сalculations).all()
    PnL = 0
    Index_PnL = 1
    if records:
        PnL = get_PnL()
        Index_PnL = get_Index_PnL()
    record = Сalculations(dollar_to_bitcoin = get_dollar_to_bitcoin(),
                          net_asset_value = get_net_asset_value(),
                          PnL = PnL,
                          Index_PnL = Index_PnL)
    db.session.add(record)
    db.session.commit()
        
        
def get_PnL_all_period():
    PnL_list = db.session.query(Сalculations.PnL).all()
    PnL_all_period = sum([PnL[0] for PnL in PnL_list])
    return PnL_all_period


def get_PnL_percent_all_period():
    Index_PnL_list = db.session.query(Сalculations.Index_PnL).order_by(Сalculations.id).all()
    PnL_percent_all_period = ((Index_PnL_list[-1][0]/Index_PnL_list[0][0]) - 1) * 100
    return PnL_percent_all_period


def get_Index_PnL_all_period(): 
    Index_PnL_all_period = db.session.query(Сalculations.Index_PnL).order_by(Сalculations.id.desc()).first()
    return Index_PnL_all_period


def get_all_period():
    calculations_date_list = db.session.query(Сalculations.calculations_date).order_by(Сalculations.id).all()
    all_period = f'{calculations_date_list[0][0]} - {calculations_date_list[-1][0]}'
    return all_period         