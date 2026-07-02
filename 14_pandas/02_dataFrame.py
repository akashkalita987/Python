import pandas as pd

data = {
    'name':['alice','bob','charlie'],
    'age':[25,30,26],
    'city':['guwahati','mumbai','delhi']
}

df = pd.DataFrame(data)
print(df)