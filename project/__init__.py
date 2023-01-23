from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler


app=Flask(__name__)
scheduler = APScheduler()


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:test@db/test'


db=SQLAlchemy(app)
migrate=Migrate(app, db)


def start_scheduler():
    from project.functions import add_in_database as scheduled_task
    scheduler.init_app(app)
    scheduler.start()
    scheduler.add_job(id='scheduled_task', 
                      func=scheduled_task, 
                      trigger='interval', 
                      seconds=10)


from project import views

if __name__ == "__main__":
    start_scheduler()
    app.run()