import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/Merwin S/OneDrive/Desktop/python/Housing.csv")
print(data)
b=data(data['bedrooms']>4)
print(b)
mean_value=b["price"].mean()
print(mean_value)



      
