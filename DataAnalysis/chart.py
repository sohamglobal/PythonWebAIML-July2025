# pip install matplotlib

import matplotlib.pyplot as plt


income=[5700,12900,2300,8210]
sources=['business','consulting','interest','salary']

plt.pie(income,labels=sources,autopct='%1.1f%%')
plt.show()
