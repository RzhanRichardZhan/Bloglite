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
        if form['submit'] == 'yes':
            title = form['title']
            text = form['text']
            f=open('content.csv','a')
            now = datetime.datetime.now()
            f.write("%s,%s,%d,%d,%d,%d,%d\n"%(title,text,now.month,now.day,now.year,now.hour,now.minute))
            c.execute("INSERT INTO blogs VALUES ('%s','%s',%d,%d,%d,%d,%d);"%(title,text,now.month,now.day,now.year,now.hour,now.minute))
            f.close()
    query = "SELECT title FROM blogs"

    q=c.execute(query)
    conn.commit()
    
    return render_template("index.html", titles =q)

@app.route('/titles/<title>')
def individual_title(title):
    return render_template("title.html", title = title)

if __name__ == '__main__':
    app.debug = True
    app.run()
