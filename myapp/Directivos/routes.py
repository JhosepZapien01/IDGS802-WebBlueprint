from flask import Blueprint

dir = Blueprint('dir',__name__)

@dir.route('/geDir',methods=['GET'])
def getDir():
    return {'key':'Directivos'} 