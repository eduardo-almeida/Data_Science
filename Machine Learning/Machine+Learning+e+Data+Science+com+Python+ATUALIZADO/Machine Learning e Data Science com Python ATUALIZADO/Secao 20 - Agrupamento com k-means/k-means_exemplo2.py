import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

x, y = make_blobs(n_samples = 200, centers = 5)
plt.scatter(x[:,0], x[:,1])

kmeans = KMeans(n_clusters = 5)
kmeans.fit(x)

previsoes = kmeans.predict(x)
plt.scatter(x[:,0], x[:,1], c = previsoes)
