from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from models import jenis_mainan
from app import app, db
from models import ClassQuestion

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
# from models import ClassQuestion

# @app.route('/')
# def main():
#     return 'Hello questions'

@app.route("/getAllQuestions", methods=['GET'])
def get_all_Questions():
    try:
        Questions = ClassQuestion.query.order_by(ClassQuestion.id_questions).all()
        return jsonify([Question.serialize() for Question in Questions])
    except Exception as e:
        return(str(e))

@app.route("/getQuestion/<id_>", methods=['GET'])
def get_Question(id_):
    try:
        getQuestion = ClassQuestion.query.filter_by(id_questions = id_).first()
        return jsonify(getQuestion.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addQuestions", methods=['POST'])
def add_Questions():
    quiz_id = request.args.get('quiz_id')
    question = request.args.get('question')
    number = request.args.get('number')
    answer = request.args.get('answer')
    created_at = request.args.get('created_at')
    modified_at = request.args.get('modified_at')
    deleted_at = request.args.get('deleted_at')

    try:
        addQuestions = ClassQuestion (
            quiz_id = quiz_id,
            question = question,
            number = number,
            answer = answer,
            created_at = created_at,
            modified_at = modified_at,
            deleted_at = deleted_at
            )
        db.session.add(addQuestions)
        db.session.commit()
        return "Questions added.add Questions id={}".format(addQuestions.id_questions)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteQuestions/<id_>", methods=['DELETE'])
def remove_Questions(id_):

    try:
        delQuestion=ClassQuestion.query.filter_by(id_questions=id_).first()
        db.session.delete(delQuestion)
        db.session.commit()
        return " Questions deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateQuestions/<id_>", methods=['PUT'])
def update_Questions(id_):
    try:
        updateQuestion=ClassQuestion.query.filter_by(id_questions=(id_)).first()
        updateQuestion.quiz_id=request.args.get('quiz_id')
        updateQuestion.question=request.args.get('question')
        updateQuestion.number=request.args.get('number')
        updateQuestion.answer=request.args.get('answer')
        # updateUser.status_enabled = bool(request.args.get('statusEnabled'))
        # updateUser.created_at=request.args.get('created_at')
        # updateUser.modified_at=request.args.get('modified_at')
        # updateUser.deleted_at=request.args.get('deleted_at')


        db.session.commit()
        return "Questions updated. ClassQuestion= " + str(updateQuestion.id_questions)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    
@app.route('/updateQuestionPerSpecColumn/<id_>/<keyCol>', methods=['PUT'])
def updateQestionsPerSpecColumn(id_,keyCol):   

    try:
        UpColQest = ClassQuestion.query.filter_by(id_questions = (id_)).first()
        
        if (keyCol.lower() == 'quiz_id'):
            UpColQest.quiz_id = request.args.get('keyCol')
            print(UpColQest.quiz_id)
        elif (keyCol.lower() == 'question'):
            UpColQest.question = request.args.get('question')
        elif (keyCol.lower() == 'number'):
            UpColQest.number = request.args.get('keyCol')
        elif (keyCol.lower() == 'answer'):
            UpColQest.answer = request.args.get('keyCol')
        # elif (keyCol.lower() == 'statusenabled'):
        #     user.status_enabled = bool(request.args.get('keyCol'))
        ## tambahin updated_on nanti hahahhh
        else:
            return "No column related exist"

        db.session.commit()
        return "Questions updated. questions-d = " + str(UpColQest.id_questions) + " updated"

    except Exception as e:
        return str(e)

    finally:
        db.session.close()
# if __name__=='__main__':
#     app.run()