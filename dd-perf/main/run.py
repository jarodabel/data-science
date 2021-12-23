from pandas import read_csv
from matplotlib import pyplot as plt

# show the release + date So for Dec 1 to Dec 8, show version X, for Dec 9 to Dec 16 show version Y

def calculate_total_locks_by_field(df, field):
    return df.groupby([field]).agg(["sum", "count"])

def calculate_sessions_by_field(df, field):
    return df.groupby([field]).agg(["count"])


data = read_csv("./main/data.csv")
prod_data = data.loc[data["environment"] == "prod"]

locks_by_version = calculate_total_locks_by_field(prod_data.filter(items=["version", "total_locks"]), "version")
print(locks_by_version.head())

locks_by_date = calculate_total_locks_by_field(prod_data.filter(items=["date", "total_locks"]), "date")
print(locks_by_date.head())

locks_by_session = calculate_total_locks_by_field(prod_data.filter(items=["browser_session_id", "total_locks"]), "browser_session_id")
print(locks_by_session.head())

sessions_by_version = calculate_sessions_by_field(prod_data.filter(items=["version", "browser_session_id"]), "browser_session_id")
print(sessions_by_version.head())
# prod_data_grouped = (
#     prod_data.filter(items=["date", "version", "total_locks"])
#     .groupby(["version", "date"])
#     .agg(["sum", "count"])
# )

# ax = prod_data_grouped.plot()

# fig = ax.get_figure()
# fig.savefig('/main/figure.png')
