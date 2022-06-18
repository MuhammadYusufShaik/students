import pandas as pd
import plotly.graph_objects as gh 
df=pd.read_csv('C:/Users/khada/Downloads/python/c107/data.csv')
data=df.groupby('level')['attempt'].mean()
print(data)
# graph=gh.Figure(gh.Bar(x=data,y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
# graph.show()