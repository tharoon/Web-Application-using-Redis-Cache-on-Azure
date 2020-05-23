import pypyodbc
from flask import Flask, request, render_template
import json
from json import loads, dumps

app = Flask(__name__)

conn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=mysqlservertrodj.database.windows.net;'
                        'PORT=1443;'
                        'DATABASE=trodjDB;'
                        'UID=trodj;'
                        'PWD=Tharoon123')
# Enter Server, UID and PWD. Deleted for security purposes
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz1', methods=["POST", "GET"])
def quiz1():
    range1 = int(request.form.get('range', ''))
    result = range1 + 1
    return render_template('quiz1.html', result=result, range1=range1)

@app.route('/quiz2', methods=["POST", "GET"])
def quiz2():
    range1 = request.form.get('range', '')
    query1 = "select * from vegetables where category = '" +str(range1)+ "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()
    return render_template('quiz2.html', r1=r1)

@app.route('/quiz2b', methods=["POST", "GET"])
def quiz2b():
    query1 = "select * from vegetables where category ='veg'"
    cursor.execute(query1)
    r1 = cursor.fetchall()
    query2 = "select * from vegetables where category ='notveg'"
    cursor.execute(query2)
    r2 = cursor.fetchall()
    rows = ([
        ['Item', 'Quantity'],
        [r1[0][0], r1[0][2]],
        [r1[1][0], r1[1][2]],
        [r1[2][0], r1[2][2]]
    ])
    rows2 = ([
        ['Item', 'Quantity'],
        [r2[0][0], r2[0][2]],
        [r2[1][0], r2[1][2]]
    ])
    return render_template('quiz2b.html', rows=rows, rows2=rows2)

@app.route("/list", methods=["POST", "GET"])
def list():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()
    return render_template('list.html', rows1=r1, rows2=r2, rows3=r3)


@app.route("/showpie", methods=["POST", "GET"])
def showpie():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of quakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]

    ])

    return render_template('showpie.html', rows=rows)


@app.route("/pie", methods=["POST", "GET"])
def pie():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows1 = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    query8 = "select count(*) from Earthquake where mag > 5.0 and deptherror > 5"
    cursor.execute(query8)
    r8 = cursor.fetchall()
    query9 = "select count(*) from Earthquake where mag > 5.0 and deptherror < 5"
    cursor.execute(query9)
    r9 = cursor.fetchall()

    rows2 = ([
        ['Magnitude and Depth Error', 'Number of Earthquakes'],
        ['Depth Error > 5', r8[0][0]],
        ['Depth Error < 5', r9[0][0]]

    ])

    return render_template('pie.html', rows=[rows1, rows2])


@app.route("/bar", methods=["POST", "GET"])
def bar():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    return render_template('bar.html', rows=rows)

@app.route("/scatter", methods=["POST", "GET"])
def scatter():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    return render_template('scatter.html', rows=rows)


@app.route("/line", methods=["POST", "GET"])
def line():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM Earthquake WHERE locationsource = '" + str(locationsrc) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    return render_template('line.html', rows=rows)
#-------------------------------------------------------------------------

#Quiz 5
@app.route("/quiz5list", methods=["POST", "GET"])
def quiz5list():
    query1 = "select * from voting where totalpop between 2000 and 8000 order by totalpop"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "select * from voting where totalpop between 8000 and 40000 order by totalpop"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    return render_template('quiz5list.html', rows1=r1, rows2=r2)

#Quiz6
@app.route('/quiz6', methods=['POST', 'GET'])
def quiz6():
    range1 = int(request.form.get('m1', ''))
    range2 = int(request.form.get('m2', ''))
    m1 = range1 * 1000
    m2 = range2 * 1000
    sql1 = "SELECT sum(registered) FROM voting WHERE totalpop BETWEEN '"+str(m1)+"' AND '"+str(m2)+"'"
    cursor.execute(sql1)
    s1 = cursor.fetchall()
    rows = ([['Population Range', 'Registered Population'],[str(m1)+'-'+str(m2), s1[0][0]]])
    return render_template('quiz6.html', sc1=rows)

#Quiz8
@app.route("/quiz8", methods=["POST", "GET"])
def quiz8():
    r1 = []
    r2 = []
    range1 = int(request.form.get('range', ''))
    range1 = range1 + 1
    for i in range(0, range1):
        modulo = (i**3)%10
        r1.append(modulo)
    for i in range(0, range1):
        count=r1.count(r1[i])
        r2.append(count)
    rows = []
    rows.append(['Range Value', 'Number of Times'])
    for i in range(0,range1):
        rows.append([r1[i],r2[i]])
    return render_template('quiz8.html', rows=rows)

#Quiz 7
@app.route("/quiz7", methods=["POST","GET"])
def quiz7():
    range1 = int(request.form.get('range',''))
    rangeStart = 0
    rangeEnd = range1
    maxQuery = "Select max(totalpop) from voting"
    cursor.execute(maxQuery)
    maxResult = cursor.fetchall()
    maxPopulation = maxResult[0][0]
    storeResult = []
    start = []
    end = []
    counter = 0
    while rangeStart <= maxPopulation:
        query = "Select count(statename) from voting where totalpop between '" +str(rangeStart)+ "' and '" +str(rangeEnd)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(rangeStart)
        end.append(rangeEnd)
        rangeStart = rangeEnd
        rangeEnd = rangeEnd + range1
        counter = counter + 1
    list_a = []
    list_a.append(['Population Range','Number of States'])
    for i in range(0, counter):
        list_a.append([str(start[i]) + '-' + str(end[i]),storeResult[i]])
    return render_template('quiz7.html', rows=list_a)

#---------------------------------------------------------------------------
@app.route("/practise1", methods=["POST", "GET"])
def practise1():
    startRange = int(request.form.get('range1',''))
    lastRange = int(request.form.get('range2',''))
    endRange = startRange + 10
    storeResult = []
    start = []
    end = []

    while startRange < lastRange:
        query = "Select count(*) from Earthq where latitude between '"+str(startRange)+"' and '"+str(endRange)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(startRange)
        end.append(endRange)
        startRange = endRange
        endRange = endRange + 10
    return render_template('practise1.html', start=start, end=end, storeResult=storeResult)

@app.route("/practise2", methods=["POST", "GET"])
def practise2():
    startRange = int(request.form.get('range1',''))
    lastRange = int(request.form.get('range2',''))
    net = str(request.form.get('net',''))
    endRange = startRange + 1
    storeResult = []
    start = []
    end = []

    while startRange < lastRange:
        query = "Select count(*) from Earthquake where mag between '"+str(startRange)+"' and '"+str(endRange)+"' and net = '"+str(net)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(startRange)
        end.append(endRange)
        startRange = endRange
        endRange = endRange + 1
    return render_template('practise2.html', start=start, end=end, storeResult=storeResult)

@app.route("/practise1pie", methods=["POST", "GET"])
def practise1pie():
    startRange = int(request.form.get('range1',''))
    lastRange = int(request.form.get('range2',''))
    endRange = startRange + 10
    storeResult = []
    start = []
    end = []
    counter = 0

    while startRange < lastRange:
        query = "Select count(*) from Earthquake where latitude between '"+str(startRange)+"' and '"+str(endRange)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(startRange)
        end.append(endRange)
        startRange = endRange
        endRange = endRange + 10
        counter = counter + 1
    list_a = []
    list_a.append(['Latitude Range', 'Number of Earthquakes'])
    for i in range(0, counter):
        list_a.append([str(start[i]) + '-' + str(end[i]),storeResult[i]])
    return render_template('practise1pie.html', start=start, end=end, storeResult=storeResult, rows = list_a)

@app.route("/practise2pie", methods=["POST", "GET"])
def practise2pie():
    startRange = int(request.form.get('range1',''))
    lastRange = int(request.form.get('range2',''))
    net = str(request.form.get('net',''))
    endRange = startRange + 1
    storeResult = []
    start = []
    end = []
    counter = 0

    while startRange < lastRange:
        query = "Select count(*) from Earthquake where mag between '"+str(startRange)+"' and '"+str(endRange)+"' and net = '"+str(net)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(startRange)
        end.append(endRange)
        startRange = endRange
        endRange = endRange + 1
        counter = counter + 1
    list_a = []
    list_a.append(['Latitude Range', 'Number of Earthquakes'])
    for i in range(0, counter):
        list_a.append([str(start[i]) + '-' + str(end[i]),storeResult[i]])
    return render_template('practise2pie.html', start=start, end=end, storeResult=storeResult, rows = list_a)

@app.route("/practise1vert", methods=["POST", "GET"])
def practise1vert():
    startRange = int(request.form.get('range1',''))
    lastRange = int(request.form.get('range2',''))
    endRange = startRange + 10
    storeResult = []
    start = []
    end = []
    counter = 0

    while startRange < lastRange:
        query = "Select count(*) from Earthquake where latitude between '"+str(startRange)+"' and '"+str(endRange)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(startRange)
        end.append(endRange)
        startRange = endRange
        endRange = endRange + 10
        counter = counter + 1
    list_a = []
    list_a.append(['Latitude Range', 'Number of Earthquakes'])
    for i in range(0, counter):
        list_a.append([str(start[i]) + '-' + str(end[i]),storeResult[i]])
    return render_template('practise1vert.html', start=start, end=end, storeResult=storeResult, rows = list_a)

@app.route("/practise2vert", methods=["POST", "GET"])
def practise2vert():
    startRange = int(request.form.get('range1',''))
    lastRange = int(request.form.get('range2',''))
    net = str(request.form.get('net',''))
    endRange = startRange + 1
    storeResult = []
    start = []
    end = []
    counter = 0

    while startRange < lastRange:
        query = "Select count(*) from Earthquake where mag between '"+str(startRange)+"' and '"+str(endRange)+"' and net = '"+str(net)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(startRange)
        end.append(endRange)
        startRange = endRange
        endRange = endRange + 1
        counter = counter + 1
    list_a = []
    list_a.append(['Mag Range', 'Number of Earthquakes'])
    for i in range(0, counter):
        list_a.append([str(start[i]) + '-' + str(end[i]),storeResult[i]])
    return render_template('practise2vert.html', start=start, end=end, storeResult=storeResult, rows = list_a)

@app.route("/practise3", methods=["POST", "GET"])
def practise3():
    net = request.form.get('net','')
    maxNst = int(request.form.get('range1',''))
    minNst = int(request.form.get('range2',''))

    query = "Select nst, gap from Earthquake where net = '"+str(net)+"' and nst between '"+str(minNst)+"' and '"+str(maxNst)+"'"
    cursor.execute(query)
    result = cursor.fetchall()
    maxQuery = "Select count(*) from Earthquake where net = '"+str(net)+"' and nst between '"+str(minNst)+"' and '"+str(maxNst)+"'"
    cursor.execute(maxQuery)
    countResult = cursor.fetchall()
    count = countResult[0][0]
    list_a = []
    list_a.append(['nst','gap'])
    for i in range(0, int(count)):
        list_a.append([result[i][0], result[i][1]])
    return render_template('practise3.html', list_a=list_a, count=count)










if __name__ == '__main__':
    app.run()
