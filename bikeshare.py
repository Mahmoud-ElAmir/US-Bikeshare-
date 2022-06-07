import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
print('Hello! Let\'s explore some US bikeshare data!')
months=['january','february','march','april','may','june','all']
days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
filters={'d':'day','m':'month','b':'both','n':'not at all'}

def get_filters():
    city = ''
    month = ''
    day = ''

    cities=['chicago','new york city','washington']
    while True :
        city=input('Enter the name of the city you would analyze (chicago,new york city,washington) ').lower()
        if city in cities:
            break
        else:
            print('PLEASE Choose on this Cities (chicago,new york city,washington)')
    print(city)

    while True:
        try:
            filter_by=input('press (d) to filter with day,(m) for month and (b) for both ').lower()
            own_filter=filters[filter_by]
            if filter_by in filters:
                break
        except KeyError:
            print('PLEASE enter valid Filter')
    if own_filter=='month':
        
        while True:
            month=input('Enter a month ').lower()
            if month in months:
                break
            else:
                print( 'PLEASE pick a month from the first half of the year')
        day = "all"
        
        print(month)    

    elif own_filter=='day':
        while True:
            try:
                day=input('Enter a day ').lower()
                if day in days:
                    break
            except KeyError:
                print('PLEASE Pick a right day')
        month = "all"
        print(day)
    elif own_filter=='both':
        while True:
            month=input('Enter a month ').lower()
            if month in months:
                break
            else:
                print( 'PLEASE pick a month from the first half of the year')
        print(month)
        while True:
            day=input('Enter a day ').lower()
            if day in days:
                break
            else:
                print('PLEASE Pick a right day')
        print(day)   
    elif own_filter=='n':
        month='all'
        day='all'
    else:
        print('please Enter valid filter')

    return city,month,day            
        
print('-'*40)
   


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df =  df[df['month'] == month]
       
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
       

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day=df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    print('Most Popular Start day:', popular_day)
    print('Most Popular Start Hour:', popular_hour)
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station=df['Start Station'].mode()[0]


    common_end_station=df['End Station'].mode()[0]

    df['Trip']=df['Start Station']+"/"+df['End Station']
    
    common_trip=df['Trip'].mode()[0]
    
    print('Most common start station:', common_start_station)
    print('Most common end station:', common_end_station)
    print('Most common trip:', common_trip)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_travel_time=df['Trip Duration'].sum()


    mean_travel_time=df['Trip Duration'].mean()

    print('Total Travel Time ',total_travel_time)
    print('Average Travel Time ',mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types=df['User Type'].value_counts()
    print("Count of user types:\n{0}\n{1}\n{0}\n".format('-'*20,user_types.to_string()))

    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print("Count of gender:\n{0}\n{1}\n{0}\n".format('-'*20,gender.to_string()))
    else:
        print('There is no Gender Data for this City ')
        
        
    if 'Birth Year' in df:   
        earliest_year=df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].mode()[0]
        print( 'The most Earliest Year of Birth ',earliest_year)
        print('The most Recent Year of Birth ',most_recent)
        print('The most common Year of Birth ',most_common)
    else:
        print('There is no Birth Year Data for this City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    row=0
    request=input(' would you like to see the Raw Data ? \n (press y if yes & anything else if no)\n ').lower()
    requests=['y','yes']
   
    while request in requests:
        raw=df.iloc[row:row+5]
        if raw.empty:
            print('There is no more Data :)')
            break
        else:            
            print(raw)
            request2 = input(' Press (y) if you would you like to see more raw data & anything else if no \n ').lower()                
            if request2== 'y' or request2=='yes':
                row+= 5
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        df=display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
