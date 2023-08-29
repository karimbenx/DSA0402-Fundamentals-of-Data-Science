import pandas as pd
import numpy as np
data={"Product1":[1000,950,800],"Product2":[950,800,750],"Product3":[800,750,600]}
sales=pd.DataFrame(data)
sales.index=["Day1","Day2","Day3"]
print(sales)
Product1_mean=np.mean(sales["Product1"])
Product2_mean=np.mean(sales["Product2"])
Product3_mean=np.mean(sales["Product3"])
print(Product1_mean)
print(Product2_mean)
print(Product3_mean)
