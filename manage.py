from flask.cli import FlaskGroup
from project import app, db
from flask_apscheduler import APScheduler
from project.functions import add_in_database

cli = FlaskGroup(app)
scheduler = APScheduler()
# scheduler.init_app(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()

    
def start_scheduler():
    with app.app_context():
        scheduler.init_app(app)
        scheduler.start()
        scheduler.add_job(id='scheduled_task', 
                        func=add_in_database, 
                        trigger='interval', 
                        seconds=10)    

if __name__ == "__main__":
    start_scheduler()
    cli()

