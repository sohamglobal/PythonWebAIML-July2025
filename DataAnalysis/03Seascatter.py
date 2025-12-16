import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")

sns.scatterplot(data=df,x="Units_Sold",y="Profit",hue="Product")
plt.title("Units sold vs Profit")
plt.show()