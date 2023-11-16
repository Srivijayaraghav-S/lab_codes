# importing the module
import pandas as pd
# importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
# dataset
dataset.head()

# checking for null values
dataset.isnull().sum()

# importing the required modules
import matplotlib.pyplot as plt
import seaborn as sns
# graph size
plt.figure(1 , figsize = (15 , 6))
graph = 0
# for loop
for x in ['Age' , 'Annual Income (k$)' , 'Spending Score (1-100)']:
    graph += 1

    # ploting graph
    plt.subplot(1 , 3 , graph)
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.displot(dataset[x] , bins = 15)
    plt.title('Distplot of {}'.format(x))
# showing the graph
plt.show()

# importing preprocessing
from sklearn import preprocessing
# lable encoders
label_encoder = preprocessing.LabelEncoder()
# converting gender to numeric values
dataset['Genre'] = label_encoder.fit_transform(dataset['Genre'])
# head
dataset.head()

# graph size
plt.figure(1, figsize = (20 ,8))
# creating heatmap
sns.heatmap(dataset)
# showing graph
plt.show()

# importing the required module
import scipy.cluster.hierarchy as sch
# graph size
plt.figure(1, figsize = (16 ,8))
# creating the dendrogram
dendrogram = sch.dendrogram(sch.linkage(dataset, method  = "ward"))
# ploting graphabs
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

# Import ElbowVisualizer
from sklearn.cluster import AgglomerativeClustering
from yellowbrick.cluster import KElbowVisualizer
model = AgglomerativeClustering()
# k is range of number of clusters.
visualizer = KElbowVisualizer(model, k=(2,30), timings=False)
# Fit data to visualizer
visualizer.fit(dataset)
# Finalize and render figure
visualizer.show()


import scipy.cluster.hierarchy as sch
# size of image
plt.figure(1, figsize = (16 ,8))
plt.grid(b=None)
# creating the dendrogram
dend = sch.dendrogram(sch.linkage(dataset, method='ward'))
# theroshold
plt.axhline(y=175, color='orange')
# ploting graphabs
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

import plotly as plt
import plotly.graph_objects as go
# calling the agglomerative algorithm
model = AgglomerativeClustering(n_clusters = 8, affinity = 'euclidean', linkage ='average')
# training the model on dataset
y_model = model.fit_predict(dataset)
# creating pandas dataframe
dataset['cluster'] = pd.DataFrame(y_model)
# creating scattered graph
trace1 = go.Scatter3d(

    # storing the variables in x, y, and z axis
    x= dataset['Age'],
    y= dataset['Spending Score (1-100)'],
    z= dataset['Annual Income (k$)'],
    mode='markers',
     marker=dict(
        color = dataset['cluster'],
        size= 3,
        line=dict(
            color= dataset['cluster'],
            width= 12
        ),
        opacity=0.9
     )
)
# ploting graph
data = [trace1]
layout = go.Layout(
    title= 'Clusters using Agglomerative Clustering',
    scene = dict(
            xaxis = dict(title  = 'Age'),
            yaxis = dict(title  = 'Spending Score'),
            zaxis = dict(title  = 'Annual Income')
        ),
    width=1024, height=512
)
fig = go.Figure(data=data, layout=layout)
plt.offline.iplot(fig)