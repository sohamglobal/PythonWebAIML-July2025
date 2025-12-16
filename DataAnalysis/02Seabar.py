import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")

sns.barplot(data=df,x="Product",y="Units_Sold")
plt.title("Units sold per product")
plt.show()

