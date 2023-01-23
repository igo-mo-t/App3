import requests, time
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

# первый день PnL = 0 и Index PnL = 1
def get_PnL():
    net_assets = db.session.query(Сalculations.net_asset_value).all()
    PnL = net_assets[-1] - net_assets[-2]
    return PnL


def get_Index_PnL():
    net_assets = db.session.query(Сalculations.net_asset_value).all()
    Index_PnL_list = db.session.query(Сalculations.Index_PnL).all()
    Index_PnL = Index_PnL_list[-1] * net_assets[-1] / net_assets[-2]      
    return Index_PnL    


def add_in_database():
    records = Сalculations.query.all()
    PnL = 0
    Index_PnL = 1
    while True():
        if records:
            PnL = get_PnL()
            Index_PnL = get_Index_PnL()
        record = Сalculations(dollar_to_bitcoin = get_dollar_to_bitcoin(),
                              net_asset_value = get_net_asset_value(),
                              PnL = PnL,
                              Index_PnL = Index_PnL)
        db.session.add(record)
        db.session.commit()
        time.sleep(10)    