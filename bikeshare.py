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
    print('Hello! Let\'s explore some US bikeshare data!  You will be asked a series of questions, feel free to use upper or lowercase entries for a filtered response to this dataset')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for chicago, new york, or washington?\n')
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print('try again')
        elif city.lower() in ('chicago', 'new york city', 'washington'):
            break
                
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhat month would you like to see? Keep in mind - data is only available until June\n')
        if month.lower() not in ('january','febuary','march','april','may','june'):
            print('try again')
        elif month.lower() in  ('january','febuary','march','april','may','june'):
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhat day of the week?\n')
        if day.lower() not in ('sunday','monday','tuesday','wednesday','thursday','friday','saturday'):
            print('try again')
        elif day.lower() in ('sunday','monday','tuesday','wednesday','thursday','friday','saturday'):
            break

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city.lower()])


        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   # df['Start Time'] = pd.DatetimeIndex(df['Start Time']).month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    
    print('Most Popular Start Month', popular_month)


    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    
    print('Most Popular Start Day', popular_day)


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station']
    start_station_count = start_station.value_counts()
    
    print("Most Commonly Used Start Station", start_station_count[:1])


    # TO DO: display most commonly used end station
    end_station = df['End Station']
    end_station_count = end_station.value_counts()
    
    print("Most Commonly Used End Station",end_station_count[:1])


    # TO DO: display most frequent combination of start station and end station trip
    
    start_stop_stations = []
    
    for stations in zip(df['Start Station'], df['End Station']):
        start_stop_stations.append("{}, {}".format(*stations))
    
    df['Start Stop Stations'] = start_stop_stations

    start_stop_stations_count = df['Start Stop Stations'].value_counts()

    print("Most Frequent Start + End Stations",start_stop_stations_count[:1])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'] 
    print("Total Travel Time Was",sum(trip_duration))

    # TO DO: display mean travel time
    
    print("Mean Travel Time" , sum(trip_duration)/len(trip_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_count = df['User Type'].value_counts()

    print("Count of User Types")
    print(user_count)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print('gender count is', gender)
    else:
        print('Gender does not exist in data')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if "Birth Year" in df.columns:
        earliest_birth_year = int(min(df['Birth Year']))
        print('Earliest Birth Year', earliest_birth_year)
    else:
        print('Birth Year does not exist in data')
        
    if "Birth Year" in df.columns:
        latest_birth_year = int(max(df['Birth Year']))
        print('Most Recent Birth Year', latest_birth_year)
    else:
        print('Birth Year does not exist in data')
        
        
    if "Birth Year" in df.columns:
        most_birth_year = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year', most_birth_year)
    else:
        print('Birth Year does not exist in data')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Added functionality 8.17.20 - displays first 5 rows of data
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #added 8.17.20
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


