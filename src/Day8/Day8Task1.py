import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
mean_scores = scores.mean(axis=0)
centered_scores = scores - mean_scores
print("Original Scores:\n", scores)
print("\nSubject-wise Mean:\n", mean_scores)
print("\nCentered (Normalized) Scores:\n", centered_scores)