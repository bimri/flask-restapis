from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/<db_name>.db"
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialization = db.Column(db.String(50))

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return "<Product %d>" % self.id


db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
