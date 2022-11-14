# Series - one dimensional collection of numbers of variables

import pandas as pd

#say I want to convert a python list to a pandas series
a_list = [5,10,15]
print(a_list[0],a_list[1],a_list[2])

my_pandas_series_1 = pd.Series(a_list)  #converting a python list to a pandas series
print(my_pandas_series_1)

print(my_pandas_series_1[0], my_pandas_series_1[1],my_pandas_series_1[2])

#by default, the index values for series elements are 0,1,2...
#by if we want to override the default index values with new index values, we can

my_pd_series_2 = pd.Series(a_list, index = ['x','y','z'])
print(my_pd_series_2)
print(my_pd_series_2['x'])

# converting a Python Dictionary to a Pandas series
#let's first create a Python dictionary

my_dict = {"day1":1200,"day2":1000,"day3":1500}
my_pd_series_3 = pd.Series(my_dict)

print(my_pd_series_3)

#DataFrames in Pandas
#DataFrame - two dimensional table (Rows and columns)
#While a series is one-dimensional, a dataframe is two dimensional

# We can convert a Python Dictionary to a dataframe
dict_calories_data = {"calories":[1200,1000,1500],"duration":[50,40,45]}
my_pd_df = pd.DataFrame(dict_calories_data)

print(my_pd_df)
print(my_pd_df['calories'])
print(my_pd_df['duration'])

my_pd_df_2 = pd.DataFrame(dict_calories_data, index = ['day1','day2','day3'])
print(my_pd_df_2)

print(my_pd_df_2.loc['day2'])

#Read a csv file as a dataframe
calories_csv_df = pd.read_csv('CaloriesData.csv')
print(calories_csv_df)
print(calories_csv_df.info())

#Read a json file as a dataframe
calories_json_df = pd.read_json('CaloriesData.json')
print(calories_json_df)
print(calories_json_df.info())

calories_data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}


Calories_text_df = pd.DataFrame(calories_data)
print(Calories_text_df)
print(Calories_text_df.info())

print("The mean of Calories = ",calories_csv_df['Calories'].mean())
print("The stdev of Calories = ",calories_csv_df['Calories'].std())
print("The min of Calories = ",calories_csv_df['Calories'].min())


      
      
      








# Dataframe - two dimensional table (Rows and columns)