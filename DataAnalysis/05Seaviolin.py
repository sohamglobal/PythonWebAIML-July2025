import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")

sns.violinplot(data=df,x="Product",y="Profit")
plt.title("Profit density by Product")
plt.show()