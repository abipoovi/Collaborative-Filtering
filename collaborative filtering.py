import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.DataFrame({
    'Item1': [5, 4, 0, 1],
    'Item2': [3, 0, 0, 1],
    'Item3': [4, 5, 3, 1],
    'Item4': [0, 2, 5, 4]
}, index=['User1','User2','User3','User4'])

# Similarity
sim = cosine_similarity(ratings)
sim_df = pd.DataFrame(sim, index=ratings.index, columns=ratings.index)

# Input
user = input("User: ")
item = input("Item: ")
k = int(input("K: "))

# Remove same user here
scores = sim_df[user].drop(user)
print(scores)

ratings_item = ratings[item]

# Keep valid users
mask = ratings_item > 0
scores = scores[mask]
ratings_item = ratings_item[mask]

# Top K
top_k = scores.sort_values(ascending=False)[:k]

# Prediction
if top_k.sum() == 0:
    pred = 0
else:
    pred = np.dot(top_k, ratings_item[top_k.index]) / top_k.sum()

print("Predicted rating:", round(pred, 1))
