import matplotlib.pyplot as plt

cate = ['apple','banana','orange','strawberry','Grape']
values = [25,30,15,20,35]

plt.clf()
plt.bar(cate,values,color='gold')
plt.title('Fruit Sales')

plt.xlabel('Fruit')
plt.ylabel('Sales')
plt.savefig('./과일.png')
plt.show()