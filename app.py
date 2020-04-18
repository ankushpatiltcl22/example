from flask import Flask,request,jsonify
import MySQLdb
from haversine import haversine

app = Flask(__name__)

db = MySQLdb.connect("localhost","root","","handhole") 
cursor = db.cursor() 


@app.route('/api/v1/<string:id>/<float:lat>/<float:lng>',methods=['GET'])
def home(id,lat,lng):
    store = []
    cursor.execute("SELECT * FROM punjab")
    myresult = cursor.fetchall()
    lat,lng = lat,lng
    uid = id
    for x in myresult:
        result = {}
        dist = haversine((lat,lng),(x[2],x[3]))
        if uid!=x[1] and  dist < 10:
            result['Category'] = x[0]
            result['Unique ID'] = x[1]
            result['lat'] = float(x[2])
            result['lng'] = float(x[3])
            result['distance'] = dist

            store.append(result)

    return jsonify({'result':store})

@app.route('/api/v2')
def second():

    cursor.execute('SELECT DISTINCT COUNT(`Nearest BTS Names`),`Nearest BTS Names` FROM punjab GROUP BY `Nearest BTS ID`')
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

    return 'Hellos'

if __name__ == '__main__':
    app.run(debug=True)