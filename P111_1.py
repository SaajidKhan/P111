import random
import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("P111.csv")
Id=df["id"].tolist()
print(statistics.mean(Id))
print(statistics.stdev(Id))

def randomSetOfMean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(Id)-1)
        value=Id[random_index]
        data_set.append(value)

    mean=statistics.mean(data_set)
    return mean

i_list=[]
for j in range(0,100):
    set_mean=randomSetOfMean(30)
    i_list.append(set_mean)
m=statistics.mean(i_list)
s=statistics.stdev(i_list)

print(statistics.mean(i_list))

fsds,fsde=m-s,m+s
ssds,ssde=m-(2*s),m+(2*s)
tsds,tsde=m-(3*s),m+(3*s)

fig=ff.create_distplot([i_list],["Id"],show_hist=False)
fig.add_trace(go.Scatter(x=[m,m],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode='lines',name='fsds'))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode='lines',name='fsde'))
fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode='lines',name='ssds'))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode='lines',name='ssde'))
fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode='lines',name='tsde'))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode='lines',name='tsde'))

fig.show()






