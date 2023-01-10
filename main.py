import pandas as pd
import numpy as np

df = pd.read_csv("./Final_Assignment.csv")

cn = df.groupby(['bottles_sold','item_description','zip_code'])\
    .sum().sort_values("bottles_sold", ascending=False).head()

df["Total_Sales"] = df["sale_dollars"] / 100

cn1 = df.groupby(['item_description','store_name','sale_dollars'])\
    .sum().sort_values("Total_Sales", ascending=False).head()

print(cn)
print(cn1)







