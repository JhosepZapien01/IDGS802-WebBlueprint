from flask import Blueprint

alumno = Blueprint('alumnos',__name__)

@alumno.route('/gealum',methods=['GET'])
def getalum():
    return {'key':'Alumnos'} 