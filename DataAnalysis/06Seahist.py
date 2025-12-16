import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")

sns.histplot(data=df,x="Revenue",bins=5)
plt.title("Revenue Distribution")
plt.show()