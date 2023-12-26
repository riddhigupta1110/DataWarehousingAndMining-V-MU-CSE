from apyori import apriori
import pandas as pd

df = pd.read_excel('DS.xlsx', engine='openpyxl')

# Convert the 'Items' column to a list of itemsets
transactions = df['Items'].str.split(', ').tolist()

min_support = 0.5
min_confidence = 0.7

# Apply the Apriori algorithm to find frequent item sets
frequent_item_sets = list(apriori(transactions, min_support=min_support))

# Print frequent item sets
print("Frequent Item Sets:")
for item_set in frequent_item_sets:
    print(f"Items: {list(item_set.items)}, Support: {item_set.support:.2f}")

# Generate association rules
association_rules = list(apriori(transactions, min_support=min_support, min_confidence=min_confidence))

# Print association rules
print("\nAssociation Rules:")
for rule in association_rules:
    items = list(rule.items)
    base_items = list(rule.ordered_statistics[0].items_base)
    confidence = rule.ordered_statistics[0].confidence
    print(f"Rule: {items} => {base_items} with Confidence: {confidence:.2f}")