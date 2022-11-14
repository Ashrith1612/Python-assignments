import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv ("international-tourism-number-of-arrivals.csv")

myCsvFile = pd.read_csv("international-tourism-number-of-arrivals.csv")
print (myCsvFile)
#Bar chart
years = df['Year']
arrivals = df['International tourism, number of arrivals']
plt.bar(['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'],
[5776000,6309000,6578000,6968000,13107000,13284000,14570000,15543000,17423000,17914000], color = 'orange')
plt.title('Number of International travels in India from 2010-2019')
plt.xlabel('Years')
plt.ylabel('Arrivals')
plt.show()

#Line chart
years = df['Year']
arrivals = df['International tourism, number of arrivals']
plt.plot(['1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005'],
[476000,534000,547000,499000,544000,434000,446000,461000,451000,513000,547000], color = 'purple')
plt.title('Number of International travels in Fiji from 1995-2005')
plt.xlabel('Years')
plt.ylabel('Arrivals')
plt.grid(True)
plt.show()


#Scatter chart
countries = df['Entity']
arrivals = df['International tourism, number of arrivals']
countries = ['Angola','CA','CR','Cuba','DR','El Sal','FR','Germany','HT','Mexico']
arrivals = [121,3339,2071,2221,4268,1501,193882,23569,558,97701]
plt.title('Number of International travels of countries in 2006 in hundreds and thousands')
plt.xlabel('Countries')
plt.ylabel('Arrivals')
plt.grid(True)
plt.scatter(countries,arrivals, color = 'black')



