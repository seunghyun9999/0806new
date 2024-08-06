import matplotlib.pyplot as plt
시간=(17,18,19,20,21,22,23)
습도 =(65 ,70 ,70 ,75 ,80 ,85 ,85)
plt.plot(시간,습도,marker='o',linestyle='-',color='b',label='humidity')
plt.xlabel('Time')
plt.ylabel('humidity')
plt.legend()
plt.grid(True)
plt.show()