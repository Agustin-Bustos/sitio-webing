import os
from flask import Flask
from flask import render_template, redirect, request
from flaskext.mysql import MySQL
from flask import send_from_directory



app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sitio'

mysql.init_app(app)

@app.route('/img/<imagen>')
def imagenes(imagen):
    print(imagen) 
    return send_from_directory( os.path.join('templates/sitio/img'),imagen)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/notas')
def notas1():
    conexion=mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `juegos`")
    notas = cursor.fetchall()
    conexion.commit()
    return render_template('sitio/notas.html', lista_notas=notas)

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/notas')
def notas():
    conexion=mysql.connect
    print(conexion)
    return render_template('sitio/notas.html')

@app.route('/login')
def login():
    return render_template('sitio/login.html')
 

@app.route('/admin/inicio')
def admin_inicio():
    return render_template('admin/index.html')

@app.route('/admin/notas')
def admin_notas():
    conexion=mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM juegos")
    notas = cursor.fetchall()
    conexion.commit()
    print(notas)
    return render_template('admin/notas.html', lista_notas= notas)


@app.route('/admin/notas/guardar', methods=['post'])
def admin_notas_guardar():
    _nombre=request.form['txtNombre']
    _archivo=request.files['txtImagen']
    _subtitulo=request.form['Subtitulo']
    print(_nombre)
    print(_archivo)
    print(_subtitulo)
    if _archivo!="":
        _archivo.save('templates/sitio/img/' + _archivo.filename)
    
    sql = "INSERT INTO `juegos` (`ID`, `TITULO`, `SUBTITULO`, `IMAGEN`) VALUES (NULL, %s, %s, %s);"
    datos = (_nombre,_subtitulo, _archivo.filename)
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return redirect('/admin/notas')

@app.route('/admin/notas/borrar', methods=['post'])
def admin_ropas_borrar():
    _Id=request.form['txtId']
    datos=_Id
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT Imagen FROM `juegos`WHERE `id` = %s;",(_Id))
    ropas=cursor.fetchall
    conexion.commit()
    print(ropas)
    #if os.path.exist("templates/sitio/img/"+str(notas[0],[0])):
    #   os.unlink("tem")("templates/sitio/img/"+str(notas[0],[0]))
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM juegos WHERE `juegos`.`id` = %s;",(_Id))
    conexion.commit()
    return redirect('/admin/notas')

#@app.route('/admin/notas/guardar', methods=['post'])
#def admin_notas_guardar():
 #   _nombre=request.form['txtNombre']
  #  _archivo=request.files['txtImagen']
   # _subtitulo=request.form['Subtitulo']
    #print(_nombre)
    #print(_archivo)
    #print(_subtitulo)
    #if _archivo="":
     #   _archivo.save("templates/")
    
    #return render_template  ('/admin/notas.html')

@app.route('/admin/logueado', methods=['post'])
def admin_login():
    return render_template('/admin/index.html')

if __name__=="__main__":
    app.run(debug=True)