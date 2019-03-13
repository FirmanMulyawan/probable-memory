import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

class pengguna(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    fullname = db.Column(db.String())
    email = db.Column(db.String())    
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now)
    iniQuiz = db.relationship('Kuis', backref='users', lazy=True)


    def __init__(self, username, password, fullname, email, created_at, modified_at, deleted_at):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<user id{}>'.format(self.user_id)

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'fullname': self.fullname,
            'email': self.email,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at,
            'Quiz yang telah dibuat': [{'title':item.title} for item in self.iniQuiz]

        }

class Kuis(db.Model):
    __tablename__ = 'quizzes'

    quiz_id = db.Column(db.Integer, primary_key = True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String())
    quiz_category = db.Column(db.String())
    play_times = db.Column(db.Integer())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now)
    questions = db.relationship('ClassQuestion', backref='quizzes', lazy=True)
    
    def __init__(self, creator_id, title, quiz_category, play_times, created_at, modified_at, deleted_at):
        
        self.creator_id = creator_id
        self.title = title
        self.quiz_category = quiz_category
        self.play_times = play_times
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<quizzes id{}>'.format(self.quiz_id)

    def serialize(self):
        return {
            'quiz_id': self.quiz_id,
            'creator_id': self.creator_id,
            'title': self.title,
            'quiz_category': self.quiz_category,
            'play_times': self.play_times,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at,
            'Questions yang telah dibuat': [{'answer':item.answer, 'number':item.number, 'question':item.question} for item in self.questions]

        }

class ClassQuestion(db.Model):
    __tablename__ = 'questions'

    id_questions = db.Column(db.Integer, primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    question = db.Column(db.String())
    number = db.Column(db.Integer())
    answer = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now)
    optionsnya = db.relationship('ClassOptions', cascade='all,delete' ,backref='questions', lazy=True)

    def __init__(self, quiz_id, question, number, answer, created_at, modified_at, deleted_at):
        
        self.quiz_id = quiz_id
        self.question = question
        self.number = number
        self.answer = answer
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '<questions id{}>'.format(self.quiz_id)

    def serialize(self):
        return {
            'id_questions': self.id_questions,
            'quiz_id': self.quiz_id,
            'question': self.question,
            'number': self.number,
            'answer': self.answer,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'deleted_at': self.deleted_at,
            'Option_list': [{'a':item.a, 'b':item.b, 'c':item.c,'d':item.d} for item in self.optionsnya]
        }

class ClassOptions(db.Model):
    __tablename__ = 'options'

    id_options = db.Column(db.Integer, primary_key = True)
    questions_id = db.Column(db.Integer, db.ForeignKey('questions.id_questions'), nullable=False)
    a = db.Column(db.String())
    b = db.Column(db.String())
    c = db.Column(db.String())
    d = db.Column(db.String())
    
    def __init__(self, questions_id, a, b, c, d):
        
        self.questions_id = questions_id
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return '<options id{}>'.format(self.questions_id)

    def serialize(self):
        return {
            'id_options': self.id_options,
            'questions_id': self.questions_id,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d
        }

class ClassLeaderboard(db.Model):
    __tablename__ = 'leaderboards'

    participant = db.Column(db.String, primary_key = True)
    game_pin = db.Column(db.Integer())
    score = db.Column(db.Integer())
    
    
    def __init__(self, participant, game_pin, score):
        self.participant = participant
        self.game_pin = game_pin
        self.score = score

    def __repr__(self):
        return '<leaderboard id{}>'.format(self.participant)

    def serialize(self):
        return {
            'participant': self.participant,
            'game_pin': self.game_pin,
            'score': self.score
        }

class ClassGame(db.Model):
    __tablename__ = 'games'

    game_pin = db.Column(db.Integer, primary_key = True)
    quiz_id = db.Column(db.Integer())
    
    
    def __init__(self, game_pin, quiz_id):
        self.game_pin = game_pin
        self.quiz_id = quiz_id

    def __repr__(self):
        return '<games id{}>'.format(self.quiz_id)

    def serialize(self):
        return {
            'game_pin': self.game_pin,
            'quiz_id': self.quiz_id
        }
