import pandas as pd

dirty_df = pd.read_csv('dirtydata.csv')
print(dirty_df)
print(dirty_df.info())

#Drop Na

clean_df = dirty_df.dropna()
print(clean_df)
print(clean_df.info())

#If we do not have the luxury of dropping all rows with NaN, then
#We try to impute the missing values with either the mean or the median or the mode
#So, hiw to impute?

#We first calculate the mean
mean_calories = dirty_df['Calories'].fillna(mean_calories,inplace= True)
clean_imputed_df
print(clean_imputed_df)
print(clean_imputed_df.info())

#add the data for row 22
#Replace Nan date for location 22 as 2020/12/22
dirty_of.loc[22, 'Date']= '2020/12/22'
print(dirty_df)
print(dirty_df.info())

#Fix the formatting of the date
dirty_df['Date']=pd.to_datetime(dirty_df['Date'])
print(dirty_df)

#fix the duration in row 7 from 450 to 34
dirty_df.loc[7,'Duration']=45

print(dirty_df)
print(dirty_df.info())

dirty_df.drop_duplicates(ignore_index)
print(dirty_df)
