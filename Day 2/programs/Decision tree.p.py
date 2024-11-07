import math

# Calculate the entropy of a dataset
def entropy(data):
    class_counts = {}
    for row in data:
        label = row[-1]  # The class label is the last element in the row
        if label not in class_counts:
            class_counts[label] = 0
        class_counts[label] += 1

    total = len(data)
    entropy_value = 0
    for count in class_counts.values():
        probability = count / total
        entropy_value -= probability * math.log2(probability)
    
    return entropy_value

# Calculate the information gain of a split
def information_gain(data, feature_index):
    # Total entropy of the dataset before the split
    total_entropy = entropy(data)
    
    # Split data based on the feature
    feature_values = {}
    for row in data:
        value = row[feature_index]
        if value not in feature_values:
            feature_values[value] = []
        feature_values[value].append(row)

    # Calculate the weighted entropy after the split
    weighted_entropy = 0
    total_rows = len(data)
    for value, subset in feature_values.items():
        subset_entropy = entropy(subset)
        weighted_entropy += (len(subset) / total_rows) * subset_entropy

    # Information Gain = Entropy(before split) - Entropy(after split)
    return total_entropy - weighted_entropy

# Find the best feature to split on
def best_feature(data):
    best_info_gain = -1
    best_feature_index = -1
    num_features = len(data[0]) - 1  # excluding the class label

    for feature_index in range(num_features):
        info_gain = information_gain(data, feature_index)
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_index = feature_index
    
    return best_feature_index

# Create the decision tree recursively
def build_tree(data):
    # If all labels are the same, return that label
    labels = [row[-1] for row in data]
    if len(set(labels)) == 1:
        return labels[0]
    
    # If no more features, return the most common label
    if len(data[0]) == 1:
        return max(set(labels), key=labels.count)
    
    # Find the best feature to split on
    best_feature_index = best_feature(data)
    best_feature_values = set([row[best_feature_index] for row in data])

    tree = {best_feature_index: {}}
    
    # Recursively build a subtree for each value of the best feature
    for value in best_feature_values:
        subset = [row for row in data if row[best_feature_index] == value]
        subtree = build_tree([row[:best_feature_index] + row[best_feature_index+1:] for row in subset])
        tree[best_feature_index][value] = subtree
    
    return tree

# Function to make predictions based on the decision tree
def predict(tree, row):
    if isinstance(tree, dict):
        feature_index = list(tree.keys())[0]
        feature_value = row[feature_index]
        subtree = tree[feature_index].get(feature_value)
        if subtree is None:
            return None  # If no subtree, return None or a default class
        return predict(subtree, row)
    else:
        return tree

# Example dataset: [Feature1, Feature2, ..., FeatureN, Label]
# This dataset is for a simple binary classification problem.
# In this example, we're classifying weather data into "Yes" or "No" (for playing tennis)

# Each row is [Outlook, Temperature, Humidity, Wind, PlayTennis]
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

# Build the decision tree
tree = build_tree(data)

# Print the tree
print("Decision Tree:")
print(tree)

# Example of making a prediction
example = ['Sunny', 'Cool', 'High', 'Weak']  # Example input
prediction = predict(tree, example)

print(f"Prediction for {example}: {prediction}")
