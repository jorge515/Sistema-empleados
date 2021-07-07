from flask import  Flask
from flask import redirect,url_for,render_template,request
from flaskext.mysql import MySQL


app=Flask(__name__)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema122'
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def home():
    sql= "INSERT INTO `empleados`()"
    conn= mysql.connet()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    


    if request.method=='POST':
        # Handle POST Request here
        return render_template('empleados/index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)