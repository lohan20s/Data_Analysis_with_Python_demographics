import pandas as pd
import numpy as np 


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
   
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round (df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    count_bachelors=df[df['education']=='Bachelors']['education'].count()
    count_education=df['education'].count()
    percentage_bachelors = round(count_bachelors/count_education*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df_advanced_ed=df[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')]['salary']
    df_advanced_ed_over50k_count=df_advanced_ed[df_advanced_ed=='>50K'].count()
    df_advanced_ed_totalcount=len(df_advanced_ed)

    df_noadvanced_ed=df[(df['education'] !='Bachelors') & (df['education'] !='Masters') & (df['education']!='Doctorate')]['salary']
    df_noadvanced_ed_totalcount=len(df_noadvanced_ed)

    higher_education = df_advanced_ed[df_advanced_ed=='>50K'].count()
    lower_education = df_noadvanced_ed[df_noadvanced_ed=='>50K'].count()

    # percentage with salary >50K
    higher_education_rich = round(higher_education/df_advanced_ed_totalcount*100,1)
    lower_education_rich = round(lower_education/df_noadvanced_ed_totalcount*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week']==min_work_hours])

    rich_percentage = (len(df[(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K')])/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    population_country=df['native-country'].value_counts()
    salary_50K=df[df['salary']=='>50K']['native-country'].value_counts()
    salary_50K = salary_50K.reindex(population_country.index, fill_value=0)
    percentage_bycountry=salary_50K/population_country*100

    highest_earning_country=percentage_bycountry.idxmax()
    highest_earning_country_percentage=round(percentage_bycountry.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary']=='>50K') & (df['native-country']=='India')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
