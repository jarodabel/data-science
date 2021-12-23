
from pandas import read_csv

data = read_csv('./main/data.csv')
res = data.loc[data['environment'] == 'prod']
df = res.groupby(['version', 'environment', 'path_group','date']).sum()

print(df)