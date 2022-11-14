import pandas as pd
import matplotlib.pyplot as plt
df_covid_data = pd.read_csv("covid_19_data.csv")
#create some lists from this dataframe
lst_date = []
for row in df_covid_data['ObservationDate']:
    lst_date.append(row)
print(lst_date)
lst_country = []
for row in df_covid_data['Country/Region']:
    lst_country.append(row)
print(lst_country)
lst_confirmed_cases = []
for row in df_covid_data['Confirmed']:
    lst_confirmed_cases.append(row)
print(lst_confirmed_cases)
lst_recovered_cases = []
for row in df_covid_data['Recovered']:
    lst_recovered_cases.append(row)
print(lst_recovered_cases)
      
lst_deaths = []
for row in df_covid_data['Deaths']:
    lst_deaths.append(row)
print(lst_deaths)
#create a list of unique countries and unique dats
lst_unique_countries = []
for i in lst_country:
    if i in lst_unique_countries:
        pass
    else:
        lst_unique_countries.append(i)
print(lst_unique_countries)
print(len(lst_unique_countries))
lst_unique_dates = []
for i in lst_date:
    if i in lst_unique_dates:
        pass
    else:
        lst_unique_dates.append(i)
print(lst_unique_dates)
print(len(lst_unique_dates))
#create lists for aggregate confirmed and recovered cases
lst_aggr_confirmed_cases_by_country = []
lst_aggr_recovered_cases_by_country = []
lst_aggr_deaths_by_country = []
lst_dates_for_aggr_data_by_country = []
dct_aggr_deaths_by_country = {}
total_global_deaths = 0
#for each country, for each date, capture the number of confirmed & recovered cases
#if a country has no provinces or states, there is nothing to be aggregated
for i in lst_unique_countries:
    print(i)
    for j in lst_unique_dates:
        count_of_same_country_same_date = 0
        for k in range(1, len(lst_country)):
            if i == lst_country[k] and j == lst_date[k]:
                count_of_same_country_same_date += 1
                if count_of_same_country_same_date == 1:
                    
        lst_aggr_confirmed_cases_by_country.append(lst_confirmed_cases[k])
                    
        lst_aggr_recovered_cases_by_country.append(lst_recovered_cases[k])
                    lst_aggr_deaths_by_country.append(lst_deaths[k])
                    lst_dates_for_aggr_data_by_country.append(j)
                else:
                    lst_aggr_confirmed_cases_by_country[-1] += 
int(lst_confirmed_cases[k])
                    lst_aggr_recovered_cases_by_country[-1] += 
int(lst_recovered_cases[k])
                    lst_aggr_deaths_by_country[-1] += int(lst_deaths[k])
    plt.plot(lst_dates_for_aggr_data_by_country, 
lst_aggr_confirmed_cases_by_country)
    plt.plot(lst_dates_for_aggr_data_by_country, 
lst_aggr_recovered_cases_by_country)
    plt.plot(lst_dates_for_aggr_data_by_country, lst_aggr_deaths_by_country)
    plt.title(i)
    plt.legend(['Confirmed','Recovered','Deaths'],loc=2)
    plt.show()
 
    dct_aggr_deaths_by_country[i] = lst_aggr_deaths_by_country
    lst_aggr_confirmed_cases_by_country = []
    lst_aggr_recovered_cases_by_country = []
    lst_aggr_deaths_by_country = []
    lst_dates_for_aggr_data_by_country = []
for i,j in dct_aggr_deaths_by_country.items():
    print(i,j)
    plt.plot(j)
    plt.title(i)
    plt.show()
    
    total_global_deaths = total_global_deaths + j[-1]
print("The total number of deaths as of the last recorded date is", 
total_global_deaths)
