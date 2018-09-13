import sklearn
import sklearn.svm                                   
import sklearn.model_selection
import sklearn.linear_model
import sklearn.datasets
import sklearn.cluster
import pandas as pd
import sklearn.tree
import matplotlib.pyplot as plt




#iris data-set
df=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//Iris.csv")
df=df.drop(['Id'],axis=1)
y=df['Species']
df=df.drop(['Species'],axis=1)
x=df

kmeans=sklearn.cluster.KMeans(n_clusters=5)
kmeans.fit(x)
print(kmeans.cluster_centers_)
yn=kmeans.cluster_centers_[0][3]

print(yn)

#scatter plot
xw=df['PetalWidthCm']
xl=df['PetalLengthCm']
ym=kmeans.cluster_centers_[1][2]
plt.scatter(xl,xw)
plt.scatter(kmeans.cluster_centers_[:,2:3],kmeans.cluster_centers_[:,3:],color='black')
plt.show()