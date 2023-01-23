from project import db
from datetime import datetime

class Сalculations(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    calculations_date = db.Column(db.DateTime(), default = datetime.utcnow)
    dollar_to_bitcoin = db.Column(db.Float())
    net_asset_value = db.Column(db.Float())
    PnL = db.Column(db.Float())
    Index_PnL = db.Column(db.Float())