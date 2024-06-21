# Example for AnnoyANN
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.metrics import recall_score
from annime.annoy_int import AnnoyANN

# Load MNIST data
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data.to_numpy()
y = mnist.target.astype(int).to_numpy()

# Split the data
num_train = int(0.9 * len(X))
X_train, X_test = X[:num_train], X[num_train:]
y_train, y_test = y[:num_train], y[num_train:]

# Create and fit AnnoyANN
annoy_ann = AnnoyANN(dim=X_train.shape[1], metric='euclidean')
annoy_ann.fit(X_train)

# Transform the data
y_pred_indices = annoy_ann.transform(X_test)

# Flatten the indices and calculate recall
y_pred_indices = y_pred_indices.flatten()
y_pred = [y_train[idx] for idx in y_pred_indices]
recall = recall_score(y_test, y_pred, average='macro')
print(f"AnnoyANN Recall: {recall}")
