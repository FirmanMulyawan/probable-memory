from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import ClassOptions
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
# from models import ClassOptions

@app.route('/')
def main():
    return 'Hello options'

@app.route("/getAllOptions", methods=['GET'])
def get_all_Options():
    try:
        option = ClassOptions.query.order_by(ClassOptions.id_options).all()
        return jsonify([Options.serialize() for Options in option])
    except Exception as e:
        return(str(e))

@app.route("/getOption/<id_>", methods=['GET'])
def get_Option(id_):
    try:
        getOption = ClassOptions.query.filter_by(id_options = id_).first()
        return jsonify(getOption.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addOptions", methods=['POST'])
def add_Options():
    questions_id = request.args.get('questions_id')
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')

    try:
        addOptions = ClassOptions (
            questions_id = questions_id,
            a = a,
            b = b,
            c = c,
            d = d
            )
        db.session.add(addOptions)
        db.session.commit()
        return "Options added.add Options id={}".format(addOptions.id_options)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteOptions/<id_>", methods=['DELETE'])
def remove_Options(id_):

    try:
        delOption=ClassOptions.query.filter_by(id_options=id_).first()
        db.session.delete(delOption)
        db.session.commit()
        return " Options deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateOptions/<id_>", methods=['PUT'])
def update_Options(id_):
    try:
        updateOption=ClassOptions.query.filter_by(id_options=(id_)).first()
        updateOption.questions_id=request.args.get('questions_id')
        updateOption.a=request.args.get('a')
        updateOption.b=request.args.get('b')
        updateOption.c=request.args.get('c')
        updateOption.d=request.args.get('d')


        db.session.commit()
        return "Options updated. ClassOptions= " + str(updateOption.id_options)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    
@app.route('/updateOptionPerSpecColumn/<id_>/<keyCol>', methods=['PUT'])
def updateOptionPerSpecColumn(id_,keyCol):   

    try:
        UpOption = ClassOptions.query.filter_by(id_options = (id_)).first()
        
        if (keyCol.lower() == 'questions_id'):
            UpOption.questions_id = request.args.get('keyCol')
            print(UpOption.questions_id)
        elif (keyCol.lower() == 'a'):
            UpOption.a = request.args.get('a')
        elif (keyCol.lower() == 'b'):
            UpOption.b = request.args.get('keyCol')
        elif (keyCol.lower() == 'c'):
            UpOption.c = request.args.get('keyCol')
        elif (keyCol.lower() == 'd'):
            UpOption.d = request.args.get('keyCol')
       
        else:
            return "No column related exist"

        db.session.commit()
        return "Options updated. options-d = " + str(UpOption.id_options) + " updated"

    except Exception as e:
        return str(e)

    finally:
        db.session.close()
# if __name__=='__main__':
#     app.run()