import sqlite3,csv
def creat():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    q1=""
    try:
        c.execute("create table blogs (title text UNIQUE, post text, month integer, day integer, year integer, hour integer, minute integer)")
    except:
        c.execute("drop table blogs")
        c.execute("create table blogs (title text UNIQUE, post text, month integer, day integer, year integer, hour integer, minute integer)")
    try:
        c.execute("create table comments (title text, comment text, month integer, day integer, year integer, hour integer, minute integer)")
    except:
        c.execute("drop table comments")
        c.execute("create table comments (title text, comment text, month integer, day integer, year integer, hour integer, minute integer)")
        
    conn.commit()
    f=open('content.csv').readlines()
    q = "INSERT INTO blogs VALUES(%(title)s,%(post)s,%(month)s,%(day)s,%(year)s,%(hour)s,%(minute)s)"
    
    for x in csv.DictReader(open('content.csv')):
        #print "I WORK"
        q1 = q%x
        c.execute(q1)
    conn.commit()

    
    f=open('comment.csv').readlines()
    q = "INSERT INTO comments VALUES(%(title)s,%(comment)s,%(month)s,%(day)s,%(year)s,%(hour)s,%(minute)s)"
    
    for x in csv.DictReader(open('comment.csv')):
        #print "I WORK"
        q1 = q%x
        c.execute(q1)
    conn.commit()

if __name__ == '__main__':
    creat()

