from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import ClassGame

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
# from models import ClassGame

@app.route('/')
def main():
    return 'Hello Games'

@app.route("/getAllGames", methods=['GET'])
def get_all_Games():
    try:
        gamesnya=ClassGame.query.order_by(ClassGame.game_pin).all()
        return jsonify([forGames.serialize() for forGames in gamesnya])
    except Exception as e:
        return(str(e))

@app.route("/getGame/<id_>", methods=['GET'])
def get_users(id_):
    try:
        getGame=ClassGame.query.filter_by(game_pin=id_).first()
        return jsonify(getGame.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addGame", methods=['POST'])
def add_Game():
    game_pin = request.args.get('game_pin')   
    quiz_id = request.args.get('quiz_id')
    
    try:
        addGam = ClassGame (
            game_pin = game_pin,
            quiz_id = quiz_id
            
            )
        db.session.add(addGam)
        db.session.commit()
        return "Game added.addGam id={}".format(addGam.game_pin)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteGame/<id_>", methods=['DELETE'])
def remove_Game(id_):

    try:
        delGam=ClassGame.query.filter_by(game_pin=id_).first()
        db.session.delete(delGam)
        db.session.commit()
        return " game deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateGame/<id_>", methods=['PUT'])
def update_Game(id_):
    try:
        updateGame=ClassGame.query.filter_by(game_pin=(id_)).first()
        updateGame.quiz_id=request.args.get('quiz_id')

        db.session.commit()
        return "Game updated. ClassGame= " + str(updateGame.game_pin)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    
@app.route('/updateGamePerSpecColumn/<id_>/<keyCol>', methods=['PUT'])
def updateUserPerSpecColumn(id_,keyCol):   

    try:
        updateGamePerSpecColumn = ClassGame.query.filter_by(game_pin = (id_)).first()
        
        if (keyCol.lower() == 'quiz_id'):
            updateGamePerSpecColumn.quiz_id = request.args.get('keyCol')
            print(updateGamePerSpecColumn.quiz_id)        
        else:
            return "No column related exist"

        db.session.commit()
        return "game updated. game-d = " + str(updateGamePerSpecColumn.game_pin) + " updated"

    except Exception as e:
        return str(e)

    finally:
        db.session.close()
# if __name__=='__main__':
#     app.run()