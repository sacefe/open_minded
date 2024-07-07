import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby("sell_date")
    
    stats = groups.agg(
        num_sold=('product', 'nunique'), 
        products=('product', lambda x: ','.join(sorted(set(x))))
        ).reset_index()

    stats.sort_values('sell_date', inplace=True)

    return stats

a= {"headers":{"Activities":["sell_date","product"]},
    "rows":{"Activities":[["2020-05-30","Headphone"],["2020-06-01","Pencil"],
                          ["2020-06-02","Mask"],["2020-05-30","Basketball"],
                          ["2020-06-01","Bible"],["2020-06-02","Mask"],
                          ["2020-05-30","T-Shirt"]]}}
df= pd.DataFrame(a)
print(df)
categorize_products(df)

 