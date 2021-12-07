import pandas as pd
import plotly.express as px
import csv
import statistics
import plotly.figure_factory as ff


df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/projects/c108/data.csv")

fig = ff.create_distplot([df ["AvgRating"].tolist()],["avgrating"] , show_hist=False)
fig.show()