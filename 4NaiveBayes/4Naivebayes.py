#pip install openpyxl
import pandas as pd

dataset = pd.read_excel('DATASET.xlsx')
print("Dataset:\n", dataset)

totalrecords=len(dataset)

def calculate_conditional_probabilities(data, feature_column, class_column):
    return data.groupby([class_column, feature_column]).size() / totalrecords

def classify_new_tuple(new_tuple, class_probabilities, conditional_probs):
    max_class, max_prob = None, -1

    for class_value, class_prob in class_probabilities.items():
        product = class_prob
        for feature, feature_value in new_tuple.items():
            cond_prob = conditional_probs.get((class_value, feature_value), 1e-6)
            product *= cond_prob
        if product > max_prob:
            max_prob, max_class = product, class_value

    return max_class

class_column = 'STOLEN'
class_probabilities = dataset[class_column].value_counts(normalize=True)
print("\nProbability of Individual Events:")
print(class_probabilities)

features = ['COLOR', 'TYPE', 'ORIGIN']
for feature_column in features:
    conditional_probs = calculate_conditional_probabilities(dataset, feature_column, class_column)
    print(f"\nConditional Probabilities for {feature_column}:")
    print(conditional_probs)

new_tuple = {'COLOR': 'RED', 'TYPE': 'SUV', 'ORIGIN': 'DOMESTIC'}
predicted_class = classify_new_tuple(new_tuple, class_probabilities, conditional_probs)
print("\nClassification for tuple:", new_tuple)
print("Predicted Class:", predicted_class)