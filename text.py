import pandas as pd
import plotly.graph_objects as gh 
df=pd.read_csv('C:/Users/khada/Downloads/python/c107/data.csv')
particularstudent=df.loc[df['student_id']=='TRL_abc']
data=particularstudent.groupby('level')['attempt'].mean()

graph=gh.Figure(gh.Bar(x=data,y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
graph.show()
