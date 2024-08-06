import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.clf()
plt.hist(data,bins=20,color='skyblue',edgecolor='black')
plt.title('histo')
plt.xlabel('val')
plt.ylabel('fre')
plt.show()