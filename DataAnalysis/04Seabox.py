import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("salesfordv.csv")

sns.boxplot(data=df,x="Product",y="Profit")
plt.title("Profit distribution by product")
plt.show()