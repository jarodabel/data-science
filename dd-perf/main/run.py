from pandas import read_csv
from matplotlib import pyplot as plt

data = read_csv("./main/data.csv")
prod_data = data.loc[data["environment"] == "prod"]
prod_data_grouped = (
    prod_data.filter(items=["date", "version", "total_locks"])
    .groupby(["version", "date"])
    .agg(["sum", "count"])
)

ax = prod_data_grouped.plot()

fig = ax.get_figure()
fig.savefig('/main/figure.png')