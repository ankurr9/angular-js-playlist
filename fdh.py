import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#file=pd.read_csv(r"C:\Users\Ankur PC\Desktop\Mall_Customers")
#print(file)

dataset = pd.read_csv(r"C:\Users\Ankur PC\Desktop/Mall_Customers.csv")
print(dataset)
dataset.head(10)
print(dataset.shape)
X= dataset.iloc[:, [3,4]].values

wcss=[]
for i in range(1,11):
    kmeans = KMeans(n_clusters= i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('no of clusters')
plt.ylabel('wcss')
plt.show()
