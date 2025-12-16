import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")
print(df)

sns.lineplot(data=df,x="Month",y="Revenue",marker="o")
plt.title("Monthly revenue trend")
plt.show()