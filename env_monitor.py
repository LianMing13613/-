import serial,time
ser = serial.Serial('/dev/ttyAMA0', 9600)
def readSerial():
    recv = ""
    dataString = ""
    count = ser.inWaiting
    if count != 0:
        try:
            recv = ser.read(count).decode('utf-8')
        except:
            pass
        if(recv == "["):
            while recv != "]":
                if ser.inWaiting:
                    recv = ser.read(count).decode('utf-8')
                    if(recv!="]"):
                        dataString += recv
                    time.sleep(0.1)
    return dataString

cv2.namedWindow("", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

figure = plot.figure(num=None, figsize=(18, 7), dpi=70, facecolor=’w’, edgecolor=’k’)

fig_temp = figure.add_subplot(2,2,1)
fig_humi = figure.add_subplot(2,2,2)
fig_mois = figure.add_subplot(2,2,3)

t_x = np.array(timeList)
t_y = np.array(tList)
h_x = np.array(timeList)
h_y = np.array(hList)
m_x = np.array(timeList)
m_y = np.array(mList)

fig_temp.cla()
fig_temp.set_title("Temperature (c)")
fig_temp.set_ylim(0, 50)
fig_temp.axes.get_xaxis().set_visible(False)
fig_temp.plot ( t_x, t_y , 'ro')

fig_humi.cla()
fig_humi.set_title("humidity (%)")
fig_humi.set_ylim(0, 1024)
fig_humi.axes.get_xaxis().set_visible(False)
fig_humi.plot ( h_x, h_y , 'bo')

fig_mois.cla()
fig_mois.set_title("Moister (degree)")
fig_mois.set_ylim(0, 1024)
fig_mois.axes.get_xaxis().set_visible(False)
fig_mois.plot ( m_x, m_y , 'go')


figure.canvas.draw()
img = np.fromstring(figure.canvas.tostring_rgb(), dtype=np.uint8, sep=")
img  = img.reshape(figure.canvas.get_width_height()[::-1] + (3,))
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)