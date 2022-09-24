from app import app
from flask import render_template
from flask import jsonify
from flask import request
from app.models.empleado import Empleados


empleados = Empleados()

@app.route('/', methods = ['GET'])
def index():
    items = empleados.listarEmpleados()
    return render_template('empleados.html', items=items)


@app.route('/empleados', methods = ['GET'])
def listar():
    items = empleados.listarEmpleadosJSON()
    return jsonify(items), 200

@app.route('/salarios/total', methods = ['GET'])
def salarios():
    items = empleados.sumarSalario()
    return jsonify(items), 200