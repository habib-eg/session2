from flask import Flask , render_template,  session, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Task %r>" % self.id


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    print(request.form)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
