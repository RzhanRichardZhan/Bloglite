from flask import Flask, render_template, request
import sqlite3, datetime, csv
#let this be the main file

app = Flask(__name__)

conn = sqlite3.connect('test.db')


@app.route('/', methods=["POST","GET"])
def index():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    if request.method == "POST":
        form = request.form
        if form['submit'] == 'yes' and form['title']!='' and form['text']!='':
            title = form['title']
            text = form['text']
            f=open('content.csv','a')
            now = datetime.datetime.now()
            f.write("%s,%s,%d,%d,%d,%d,%d\n"%(title,text,now.month,now.day,now.year,now.hour,now.minute))
            c.execute("INSERT INTO blogs VALUES ('%s','%s',%d,%d,%d,%d,%d);"%(title,text,now.month,now.day,now.year,now.hour,now.minute))
            f.close()
    query = "SELECT * FROM blogs"

    q=[x for x in c.execute(query)]
    #print q

    #to get the number of comments
    q2 = {}
    for x in reversed(q):
        query = "SELECT title FROM comments WHERE title =\'" + x[0] +"\'"
        qtemp = [y for y in c.execute(query)]
        q2[x[0]] = len(qtemp)
    conn.commit()
    print q2

    return render_template("index.html", titles =reversed(q),lengths = q2)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/title/<title>', methods=["POST","GET"])
def individual_title(title):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    if request.method == "POST":
        form = request.form
        if form['submit'] == 'yes' and form['comment']!='':

            comment = form['comment']
            f=open('comment.csv','a')
            now = datetime.datetime.now()
            f.write("%s,%s,%d,%d,%d,%d,%d\n"%(title,comment,now.month,now.day,now.year,now.hour,now.minute))
            c.execute("INSERT INTO comments VALUES ('%s','%s',%d,%d,%d,%d,%d);"%(title,comment,now.month,now.day,now.year,now.hour,now.minute))
            conn.commit()
            f.close()
    query = "SELECT * FROM blogs WHERE title =\'" + title +"\'"
    q=[x for x in c.execute(query)]
    #print q
    query = "SELECT * FROM comments WHERE title =\'" + title +"\'"
    q2=[x for x in c.execute(query)]
    #print q2
    return render_template("title.html", titles = q, comments = reversed(q2))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
