from flask import Flask, jsonify, request
from app import app, db
from models import Kuis

@app.route('/tesquiz')
def tesquiz():
    return 'Hello quizzes'

@app.route("/getAllQuizzes", methods=['GET'])
def get_all_Quizzes():
    try:
        kuisnya = Kuis.query.order_by(Kuis.quiz_id).all()
        return jsonify([Kuisdong.serialize() for Kuisdong in kuisnya])
    except Exception as e:
        return(str(e))

@app.route("/getQuizzes/<id_>", methods=['GET'])
def get_Quizzes(id_):
    try:
        getKuis=Kuis.query.filter_by(quiz_id=id_).first()
        return jsonify(getKuis.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addQuizzes", methods=['POST'])
def add_Quizzes():
    creator_id = request.args.get('creator_id')
    title = request.args.get('title')
    quiz_category = request.args.get('quiz_category')
    play_times = request.args.get('play_times')
    created_at = request.args.get('created_at')
    modified_at = request.args.get('modified_at')
    deleted_at = request.args.get('deleted_at')

    try:
        addQuiz = Kuis (
            creator_id = creator_id,
            title = title,
            quiz_category = quiz_category,
            play_times = play_times,
            created_at = created_at,
            modified_at = modified_at,
            deleted_at = deleted_at
            )
        db.session.add(addQuiz)
        db.session.commit()
        return "users added.addQuiz id={}".format(addQuiz.quiz_id)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteQuiz/<id_>", methods=['DELETE'])
def remove_Quiz(id_):

    try:
        delKuis=Kuis.query.filter_by(quiz_id=id_).first()
        db.session.delete(delKuis)
        db.session.commit()
        return " Quizzes deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateQuizzes/<id_>", methods=['PUT'])
def update_Quizzes(id_):
    try:
        updateQuizzes=Kuis.query.filter_by(quiz_id=(id_)).first()
        updateQuizzes.creator_id=request.args.get('creator_id')
        updateQuizzes.title=request.args.get('title')
        updateQuizzes.quiz_category=request.args.get('quiz_category')
        updateQuizzes.play_times=request.args.get('play_times')
        # updateUser.status_enabled = bool(request.args.get('statusEnabled'))
        # updateUser.created_at=request.args.get('created_at')
        # updateUser.modified_at=request.args.get('modified_at')
        # updateUser.deleted_at=request.args.get('deleted_at')


        db.session.commit()
        return "Quiz updated. Kuis= " + str(updateQuizzes.quiz_id)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    
@app.route('/updateQuizPerSpecColumn/<id_>/<keyCol>', methods=['PUT'])
def updateQuizPerSpecColumn(id_,keyCol):   

    try:
        UpColQu = Kuis.query.filter_by(quiz_id = (id_)).first()
        
        if (keyCol.lower() == 'creator_id'):
            UpColQu.creator_id = request.args.get('keyCol')
            print(UpColQu.creator_id)
        elif (keyCol.lower() == 'quiz_category'):
            UpColQu.quiz_category = request.args.get('quiz_category')
        elif (keyCol.lower() == 'title'):
            UpColQu.title = request.args.get('keyCol')
        elif (keyCol.lower() == 'play_times'):
            UpColQu.play_times = request.args.get('keyCol')
        # elif (keyCol.lower() == 'statusenabled'):
        #     user.status_enabled = bool(request.args.get('keyCol'))
        ## tambahin updated_on nanti hahahhh
        else:
            return "No column related exist"

        db.session.commit()
        return "Quizzes updated. quiz-d = " + str(UpColQu.quiz_id) + " updated"

    except Exception as e:
        return str(e)

    finally:
        db.session.close()
# if __name__=='__main__':
#     app.run()