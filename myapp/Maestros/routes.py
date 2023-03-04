from flask import Blueprint

maestros = Blueprint('maestros',__name__)

@maestros.route('/gemaes',methods=['GET'])
def getmaes():
    return {'key':'Maestros'} 