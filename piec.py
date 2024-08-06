import matplotlib.pyplot as plt

labels = ['en','ma','sc','hi']
sizes = [45,30,15,10]

plt.clf()

plt.pie(sizes,labels=labels,autopct='%1.1f%%',
        startangle=140,colors=['lightgreen','lightcoral','b','r'])
plt.title('su')

plt.show()