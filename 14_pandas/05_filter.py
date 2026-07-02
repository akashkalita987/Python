import pandas as pd

data = {
    'Name': ['Anna', 'Ben', 'Ciara', 'David'],
    'Grade': [88, 55, 92, 45]
}
df = pd.DataFrame(data)

# Filter rows where Grade is greater than or equal to 60 (Passing)
passing_students = df[df['Grade'] >= 60]

print("Passing Students:")
print(passing_students)