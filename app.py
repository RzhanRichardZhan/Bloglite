from flask import Flask, render_template, request
import sqlite3, datetime
#let this be the main file

app = Flask(__name__)
'''
conn = sqlite3.connect('test.db')
c = conn.cursor()
'''


@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        form = request.form
        if form['submit'] == 'yes':
            title = form['title']
            text = form['text']
            f=open('content.csv','a')
            now = datetime.datetime.now()
            f.write("%d,%d,%d,%d,%d,%s,%s\n"%(now.month,now.day,now.year,now.hour,now.minute,title,text))
            f.close()
    
    return render_template("index.html")

@app.route('/<title>')
def individual_title(title):
    return render_template("title.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
