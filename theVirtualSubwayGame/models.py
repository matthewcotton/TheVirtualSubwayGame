from theVirtualSubwayGame import db


# SQLAlchemy class definition for Toronto TTC stations
class Toronto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stationName = db.Column(db.String(25), unique=True, nullable=False)
    plusCode = db.Column(db.String(10))
    line = db.Column(db.String(1))

    def __repr__(self):
        return f"{self.stationName}"

# SQLAlchemy class definition for Sheffield Supertram stops
class Sheffield(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stationName = db.Column(db.String(25), unique=True, nullable=False)
    plusCode = db.Column(db.String(10))
    line = db.Column(db.String(1))

    def __repr__(self):
        return f"{self.stationName}"

# Add classes for London


db.create_all()