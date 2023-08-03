from flask import Flask
from flask import render_template, redirect, request
from flaskext.mysql import MySQL
from flask import send_from_directory

app= Flask(__name__)
@app.route('/')
def inicio():
    return render_template('Sitio/index.html')

app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sitio'

mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/jueguitos')
def jueguitos():
    conexion=mysql.connect
    print(conexion)
    return render_template('sitio/jueguitos.html')

@app.route('/login')
def login():
    return render_template('sitio/login.html')

@app.route('/admin/inicio')
def admin_inicio():
    return render_template('admin/index.html')

@app.route('/admin/jueguitos')
def admin_jueguitos():
    return render_template('admin/jueguitos.html')

@app.route('/admin/jueguitos/guardar', methods=['post'])
def admin_autos_guardar():
    _nombre=request.form['txtNombre']
    _archivo=request.files['txtImagen']
    _precio=request.form['txtPrecio']
    print(_nombre,_archivo,_precio)

    return redirect('/admin/jueguitos')


if __name__=="__main__":
    app.run(debug=True)