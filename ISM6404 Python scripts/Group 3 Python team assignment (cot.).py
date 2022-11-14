import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv ("international-tourism-number-of-arrivals.csv")


#Bar chart for country arrivals

countries = df['Entity']
arrivals = df['International tourism, number of arrivals']
plt.bar(['AR','AT','BM','China','Egypt','Guam','Italy','Japan','Nepal','Spain'],
[6942,30816,7660,158606,11346,1549,932286,31192,11730,124456], color = 'green')
plt.title('Number of International travels of countries in 2018 in hundreds and thousands')
plt.xlabel('Countries')
plt.ylabel('Arrivals')
plt.show()
