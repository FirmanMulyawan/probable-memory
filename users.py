from flask import Flask, jsonify, request
from app import app, db
from models import pengguna

@app.route('/u')
def tesUser():
    return 'tes koneksi users'

@app.route("/getAllUsers", methods=['GET'])
def get_all_Users():
    try:
        usersPengguna=pengguna.query.order_by(pengguna.user_id).all()
        return jsonify([pengguna.serialize() for pengguna in usersPengguna])
    except Exception as e:
        return(str(e))

@app.route("/getUsers/<id_>", methods=['GET'])
def get_users(id_):
    try:
        getUser=pengguna.query.filter_by(user_id=id_).first()
        return jsonify(getUser.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addUser", methods=['POST'])
def add_User():
    username = request.args.get('username')
    password = request.args.get('password')
    fullname = request.args.get('fullname')
    email = request.args.get('email')
    created_at = request.args.get('created_at')
    modified_at = request.args.get('modified_at')
    deleted_at = request.args.get('deleted_at')

    try:
        addUser = pengguna (
            username = username,
            password = password,
            fullname = fullname,
            email = email,
            created_at = created_at,
            modified_at = modified_at,
            deleted_at = deleted_at
            )
        db.session.add(addUser)
        db.session.commit()
        return "users added.addUser id={}".format(addUser.user_id)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteUser/<id_>", methods=['DELETE'])
def remove_User(id_):

    try:
        delUser=pengguna.query.filter_by(user_id=id_).first()
        db.session.delete(delUser)
        db.session.commit()
        return " user deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateUsers/<id_>", methods=['PUT'])
def update_Users(id_):
    try:
        updateUser=pengguna.query.filter_by(user_id=(id_)).first()
        updateUser.username=request.args.get('username')
        updateUser.password=request.args.get('password')
        updateUser.fullname=request.args.get('fullname')
        updateUser.email=request.args.get('email')
        # updateUser.status_enabled = bool(request.args.get('statusEnabled'))
        # updateUser.created_at=request.args.get('created_at')
        # updateUser.modified_at=request.args.get('modified_at')
        # updateUser.deleted_at=request.args.get('deleted_at')


        db.session.commit()
        return "user updated. pengguna= " + str(updateUser.user_id)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    
@app.route('/updateUserPerSpecColumn/<id_>/<keyCol>', methods=['PUT'])
def updateUserPerSpecColumn(id_,keyCol):   

    try:
        updateUserPerSpecColumn = pengguna.query.filter_by(user_id = (id_)).first()
        
        if (keyCol.lower() == 'username'):
            updateUserPerSpecColumn.username = request.args.get('keyCol')
            print(updateUserPerSpecColumn.username)
        elif (keyCol.lower() == 'email'):
            updateUserPerSpecColumn.email = request.args.get('keyCol')
        elif (keyCol.lower() == 'password'):
            updateUserPerSpecColumn.password = request.args.get('keyCol')
        elif (keyCol.lower() == 'fullname'):
            updateUserPerSpecColumn.fullname = request.args.get('keyCol')
        # elif (keyCol.lower() == 'statusenabled'):
        #     user.status_enabled = bool(request.args.get('keyCol'))
        ## tambahin updated_on nanti hahahhh
        else:
            return "No column related exist"

        db.session.commit()
        return "User updated. User-d = " + str(updateUserPerSpecColumn.user_id) + " updated"

    except Exception as e:
        return str(e)

    finally:
        db.session.close()
if __name__=='__main__':
    app.run()