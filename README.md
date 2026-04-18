# Collaborative-Filtering
Developed a user-based collaborative filtering system using Python to predict user preferences for items based on similarity with other users. The system utilizes a ratings matrix where users rate different items, and recommendations are generated using similarity scores.

Cosine similarity was applied to measure the similarity between users based on their rating patterns. For a given user and item, the system identifies the top K most similar users who have rated that item and computes a predicted rating using a weighted average of their ratings.

The model handles missing ratings by ignoring zero values and filtering only valid user-item interactions. The final predicted rating helps determine how likely a user is to prefer a specific item.
