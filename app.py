from flask import Flask, render_template, request
import sqlite3, datetime
#let this be the main file

app = Flask(__name__)

conn = sqlite3.connect('test.db')
c = conn.cursor()
q="create table blogs (title UNIQUE text, post text)"
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
            f.write("%d,%d,%d,%d,%d,%s,%s\n"%(title,text,now.month,now.day,now.year,now.hour,now.minute)
            f.close()
    f=open('content.csv').readlines()
    #print [x[5] for x in f]
    q = "INSERT INTO blogs VALUES(%(title)s,%(text)s,)"
    for x in csv.DictReader(open('content.csv')):
        q1 = q%x
    
    
    
    return render_template("index.html", titles = [x.split(",")[5] for x in f])

@app.route('/titles/<title>')
def individual_title(title):
    return render_template("title.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
