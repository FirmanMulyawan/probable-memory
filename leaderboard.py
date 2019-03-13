from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import ClassLeaderboard

# db = SQLAlchemy()
# app = Flask(__name__)

# POSTGRES = {
#     'user': 'postgres',
#     'pw': '3210151201900081KTp',
#     'db': 'kahoot',
#     'host': 'localhost',
#     'port': '5432'
# }
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# db.init_app(app)
# from models import ClassLeaderboard

# @app.route('/')
# def leaderboard():
#     return 'Hello Leaderboard'

@app.route("/getAllLeaderboard", methods=['GET'])
def get_all_leaderboard():
    try:
        leader=ClassLeaderboard.query.order_by(ClassLeaderboard.participant).all()
        return jsonify([lead.serialize() for lead in leader])
    except Exception as e:
        return(str(e))

@app.route("/getleaderboard/<id_>", methods=['GET'])
def get_leaderboard(id_):
    try:
        varGetLead=ClassLeaderboard.query.filter_by(participant=id_).first()
        return jsonify(varGetLead.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addLeaderboard", methods=['POST'])
def add_leaderboard():
    participant = request.args.get('participant')
    game_pin = request.args.get('game_pin')   
    score = request.args.get('score')
    
    try:
        addLeader = ClassLeaderboard (
            participant = participant,
            game_pin = game_pin,
            score = score
            
            )
        db.session.add(addLeader)
        db.session.commit()
        return "leaderboard added.addLeader id={}".format(addLeader.participant)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteLeader/<name_>", methods=['DELETE'])
def remove_Leader(name_):

    try:
        delLead=ClassLeaderboard.query.filter_by(participant=name_).first()
        db.session.delete(delLead)
        db.session.commit()
        return " Leaderboard deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateLeader/<name_>", methods=['PUT'])
def update_Game(name_):
    try:
        updateLeader=ClassLeaderboard.query.filter_by(participant=(name_)).first()
        updateLeader.game_pin=request.args.get('game_pin')
        updateLeader.score=request.args.get('score')


        db.session.commit()
        return "leader updated. ClassLeaderboard= " + str(updateLeader.participant)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    