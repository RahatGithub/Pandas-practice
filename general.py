import pandas as pd

data = pd.read_csv("Data/data.csv")

data.to_excel(r'C:\PYTHON CODE\pandas_codes\Pandas practice\Data\data_xl.xlsx', index=None, header=True)

except:

    print("Something wrong happened")
