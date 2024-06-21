# task2.py

# Define a list of test scores
test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]

# Sort the list of scores in descending order (highest scores first)
test_scores.sort(reverse=True)

# Print the top three scores
print("Top three scores:")
for score in test_scores[:3]:
  print(score)
