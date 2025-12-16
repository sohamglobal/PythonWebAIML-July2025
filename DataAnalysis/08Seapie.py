import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")
# choose a column to build the pie from: prefer a categorical column, otherwise use the first column
if df.empty:
    raise SystemExit("DataFrame is empty")

cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
col = cat_cols[0] if cat_cols else df.columns[0]

counts = df[col].astype(str).value_counts()
labels = counts.index.tolist()
sizes = counts.values

# use a seaborn palette for colors and plot with matplotlib's pie
colors = sns.color_palette('pastel', len(labels))

plt.figure(figsize=(6, 6))
plt.pie(df["Profit"], labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'k'})
plt.title(f'Pie chart of {col}')
plt.axis('equal')  # keep pie circular
plt.tight_layout()
plt.show()
