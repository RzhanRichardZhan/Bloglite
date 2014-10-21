import sqlite3,csv
def creat():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    q=""
    try:
        c.execute("create table blogs (title text UNIQUE, post text)")
        
    except:
        c.execute("drop table blogs")
        c.execute("create table blogs (title text UNIQUE, post text)")
        
    conn.commit()
    f=open('content.csv').readlines()
    q = "INSERT INTO blogs VALUES(%(title)s,%(text)s,%(month)s,%(day)s,%(year)s,%(hour)s,%(minute)s)"
    for x in csv.DictReader(open('content.csv')):
        q1 = q%x
        print q1
        c.execute(q1)
    conn.commit()

if __name__ == '__main__':
    creat()

