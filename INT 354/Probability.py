import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np 
#LOad the Iris dataset
iris = sns.load_dataset("iris")
#Choose a feature for CDF (eg sepal length)
feature = "sepal_length"
data = iris[feature]

feature = "sepal_length"
data = iris[feature]
#Create cdf using seaborn's ecdfplot
sns.ecdfplot(data,stat="proportion",complementary=True)
#Add labels and title
plt.xlabel(f'{feature}')
plt.ylabel('Cumulative Probability')
plt.title(f'Cumulative Distribution Function (CDF): {feature}')

#Show the plot
plt.show()