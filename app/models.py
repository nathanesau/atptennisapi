from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String) 
    country_code = db.Column(db.String)

    def __repr__(self):
        return '<Player {}>'.format(self.id)

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Tournament {}>'.format(self.name)

class Entrant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_seed = db.Column(db.Integer)
    player_result = db.Column(db.Integer)

    def __repr__(self):
        return '<Entrant {}>'.format(self.id)

class Matchup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    player1_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player2_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    round_num = db.Column(db.Integer)
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'))

    def __repr__(self):
        return '<Matchup {}>'.format(self.matchup)
