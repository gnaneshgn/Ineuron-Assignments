from flask import Flask,request,jsonify
import psycopg2
import pymongo

app=Flask(__name__)


@app.route('/sqldata',methods=['POST','GET'])
def fetchSqlData():
    """
    returns data from postgresql
    :return: json type of data
    """
    data_list=[]
    if request.method=='POST':
        conn=psycopg2.connect(database="lamas",host="localhost",user="postgres",password="Postgresql@009")
        cur=conn.cursor()
        cur.execute("Select * from email_registration")
        db_version = cur.fetchall()
        for i in db_version:
            data_list.append(i[1])
        return jsonify(data_list)


@app.route('/mongodata',methods=['POST'])
def fetchMongoData():
    """
    returns data from mongoDb data base
    :return: json type of data
    """
    mongo_data=[]
    if request.method=='POST':
        client = pymongo.MongoClient(
            "mongodb+srv://mongodb:mongodb@cluster0.fvpmh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client.test1
        cursor = db.ineuron_db.find()
        for i in cursor:
            mongo_data.append(i)
        return jsonify(mongo_data)







if __name__=='__main__':

    app.run(debug=True)