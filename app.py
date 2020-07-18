from app import app, db, tasks
from app.models import Player, Tournament
from threading import Thread

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Player': Player, 'Tournament': Tournament}

if __name__ == "__main__":

    # start background tasks
    thread = Thread(target=tasks.threaded_task, args=(3600,))
    thread.daemon = True
    thread.start()

    app.run()