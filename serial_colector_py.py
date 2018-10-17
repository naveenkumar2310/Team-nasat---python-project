from serial import Serial
import time
import sqlite3
ser =Serial(
    port='COM4',
    baudrate = 115200,
    timeout=None)
conn=sqlite3.connect('sensor.db')
c=conn.cursor()
c.execute('create table sensor(temperature number(20,20),time number(20,20))')
def adddata(data):
    
    date=time.time()
    h=str(data)
    g=str(date)
    c.execute('insert into sensor(temperature,time) values(?,?)',(h,g,))
    conn.commit()
    #fh = open('example.txt', 'a')
    #fh.write(h) 
    #fh.close 
while 1:
    
    while(ser.inWaiting()==0):
        
        pass
    a=float(ser.readline().decode('utf-8'))
    adddata(a)

c.close()
conn.close()
