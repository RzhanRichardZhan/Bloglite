from flask import Flask, render_template, request
import sqlite3, datetime, csv
#let this be the main file

app = Flask(__name__)

conn = sqlite3.connect('test.db')

c = conn.cursor()
q="drop table blogs"
c.execute(q)
conn.commit()
q="create table blogs (title text UNIQUE, post text)"
c.execute(q)
conn.commit()
    


@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        form = request.form
        if form['submit'] == 'yes':
            title = form['title']
            text = form['text']
            f=open('content.csv','a')
            now = datetime.datetime.now()
            f.write("%d,%d,%d,%d,%d,%s,%s\n"%(title,text,now.month,now.day,now.year,now.hour,now.minute))
            f.close()
    f=open('content.csv').readlines()
    #print [x[5] for x in f]
    q = "INSERT INTO blogs VALUES(%(title)s,%(text)s,%(month)s,%(day)s,%(year)s,%(hour)s,%(minute)s)"
    for x in csv.DictReader(open('content.csv')):
        q1 = q%x
        print q1
        c.execute(q1)

    query = "SELECT * titles FROM blogs"

    q2=c.execute(query)
    conn.commit()
    
    return render_template("index.html", titles =q2)

@app.route('/titles/<title>')
def individual_title(title):
    return render_template("title.html", title = title)

if __name__ == '__main__':
    app.debug = True
    app.run()
