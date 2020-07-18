from app import app, db

@app.route('/api/v1/players/get')
def get_players():
    return "Player"

@app.route('/api/v1/tournaments/get')
def get_tournaments():
    return "Tournaments"

@app.route('/api/v1/draws/get')
def get_draw():
    return "Draw"