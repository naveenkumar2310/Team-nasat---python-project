import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime as dta
import sqlite3

style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
conn=sqlite3.connect('sensor.db')
c=conn.cursor()
def animate(i):
    dateconv = dta.datetime.fromtimestamp
    c.execute('select temperature,time from sensor')
    conn.commit()
    xs = []
    ys = []
    ''' y axis the date'''
    for row in c.fetchall():
            xs.append(row[0])
            y = dateconv(row[1])
            ys.append(y)
    ax1.clear()
    ax1.plot(ys, xs,label='temperature')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.xlabel('date')
    plt.ylabel('temperature')
    plt.legend()
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.subplots_adjust(left=0.09, bottom=0.23, right=0.93, top=0.90, wspace=0.2, hspace=0)
plt.show()
c.close()
conn.close()

