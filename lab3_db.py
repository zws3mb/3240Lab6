__author__ = 'zws3mb'
import read_csv as rs
import sqlite3
database='c:/sqlite3/lab3.db'
def readin(filename):
    infile = open(filename,'rU')
    conn = sqlite3.connect(database)
    for line in infile:
        # print line.split(',')
        deptID,courseNum,semester,meetingType,seatsTaken,seatsOffered,instructor=line.split(',')
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
        cur.execute(sql_cmd, (deptID, courseNum,semester,meetingType,seatsTaken,seatsOffered,instructor)) # use ? in command string and a tuple to fill in each ?
    conn.commit()
    conn.close()
def queryDept(department):
    conn = sqlite3.connect(database)
    sql_cmd = 'select * from coursedata where deptID=?'
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    prof=dict()
    course=dict()
    for item in cur.execute(sql_cmd,(department,)).fetchall():
        if item['instructor'] in prof:
            prof[item['instructor']]+=int(item['seatsTaken'])
        else:
            prof[item['instructor']]=int(item['seatsTaken'])
        if item['courseNum'] in course:
            course[item['courseNum']]+=int(item['seatsTaken'])
        else:
            course[item['courseNum']]=int(item['seatsTaken'])
    return (prof,course)
if __name__=='__main__':
    readin('seas-courses-5years.csv')
    deptkey = raw_input('Please enter a department key to search:')
    dict1,dict2=queryDept(deptkey)
    for item in dict1.keys():
        print item.replace('\n','')+' %s'%dict1[item]
    for item in dict2.keys():
        print deptkey+str(item)+' %s'%dict2[item]