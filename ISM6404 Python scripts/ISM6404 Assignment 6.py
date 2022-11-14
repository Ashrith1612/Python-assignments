import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv ("USCovidData.csv")


# six lists

Dates = []
for row in df['Date']:
    Dates.append(row)
print(Dates)

Daily_new_cases = []
for row in df['daily_new_cases']:
    Daily_new_cases.append(row)
print(Daily_new_cases)

Cum_total_cases = []
for row in df['cum_total_cases']:
    Cum_total_cases.append(row)
print(Cum_total_cases)

Active_cases = []
for row in df['active_cases']:
    Active_cases.append(row)
print(Active_cases)

Daily_new_deaths = []
for row in df['daily_new_deaths']:
    Daily_new_cases.append(row)
print(Daily_new_deaths)

Cum_total_deaths = []
for row in df['cum_total_deaths']:
    Cum_total_deaths.append(row)
print(Cum_total_deaths)

#sum of daily new cases
def sum_of_all_elements(Daily_new_cases):
    the_sum = 0
    for i in Daily_new_cases:
        the_sum += i
        return the_sum
    
myCsvFile = pd.read_csv("USCovidData.csv")
print (myCsvFile)


print("Cumulative cases computed by summing daily new cases is = ",df['daily_new_cases'].sum())
 
last_element = Cum_total_cases[-1]   
print('Cumulative cases as per the last value in the list of cum total cases is: ', last_element)

print("Cumulative deaths computed by summing daily new deaths is = ",df['daily_new_deaths'].sum())

last_element = Cum_total_deaths[-1]   
print('Cumulative deaths as per the last value in the list of cum total deaths is: ', last_element)




dates = df['Date']
daily_new_cases = df['daily_new_cases']
plt.plot(dates, daily_new_cases)
plt.title('Number of Daily new cases of COVID from Feb 2020 to Mar 2021')
plt.xlabel('Dates')
plt.ylabel('Daily new cases')
plt.plot_date(dates, daily_new_cases, linestyle='solid',color='red' )
plt.show()

dates = df['Date']
cum_total_cases = df['cum_total_cases']
active_cases = df['active_cases']
plt.plot(dates, cum_total_cases, label = "Total number of COVID cases")
plt.plot(dates, active_cases, label = "Number of active COVID cases", color='red' )
plt.title('Total and active number of COVID cases from Feb 2020 to Mar 2021')
plt.xlabel('Dates')
plt.ylabel('COVID cases')
plt.legend()
plt.show()

dates = df['Date']
daily_new_deaths = df['daily_new_deaths']
plt.bar(dates, daily_new_deaths, color='green')
plt.title('Number of Daily new deaths of COVID from Feb 2020 to Mar 2021')
plt.xlabel('Dates')
plt.ylabel('Daily new deaths')
plt.show()

dates = df['Date']
cum_total_deaths = df['cum_total_deaths']
plt.plot(dates, cum_total_deaths)
plt.title('Number of Total new deaths of COVID from Feb 2020 to Mar 2021')
plt.xlabel('Dates')
plt.ylabel('Total number of deaths')
plt.show()


daily_new_cases = df['daily_new_cases']
daily_new_deaths = df['daily_new_deaths']
plt.title('Number of Daily new COVID cases and deaths from Feb 2020 to Mar 2021')
plt.xlabel('Daily new cases')
plt.ylabel('Daily new deaths')
plt.scatter(daily_new_cases,daily_new_deaths)
plt.show()


                