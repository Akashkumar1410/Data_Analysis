import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv("machine-readable-business-employment-data-mar-2023-quarter.csv")
print(df)
profile=ProfileReport(df)
profile.to_file(output_file="machine.html")