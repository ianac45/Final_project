import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://en.wikipedia.org/wiki/Demographics_of_the_world"
dfs = pd.read_html(url,)
#looks for the third graph 
df = dfs[3]

# removes all spaces from the colum so it can be entered into a graph
df["World population (in thousands)"] = df["World population (in thousands)"].str.replace(' ', '')
#plots these colums into the graph 
df = df[["Year", "World population (in thousands)"]].astype("int")
# defines the x and y axis 
df.plot(x = "Year", y = "World population (in thousands)", kind = "bar")
# creates a bar graph 
df.plot()
plt.show()

# prints the info being graphed 
print(df.info())
