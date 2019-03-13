from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
from users import tesUser
from quizzes import get_all_Quizzes
from question import get_all_Questions
from option import get_all_Options
from leaderboard import  get_all_leaderboard

POSTGRES = {
    'user': 'postgres',
    'pw': '3210151201900081KTp',
    'db': 'kahoot',
    'host': 'localhost',
    'port': '5432'
}

app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

# @app.route('/')
# def main():
#     return 'Hello users'