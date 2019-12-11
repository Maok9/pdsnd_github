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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which name of the city to analyze? New York City, Chicago or Washington?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print('invalid inputs')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which name of the month to filter by? (all, january, february, ... , june)\n").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('invalid inputs')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which name of the day of week to filter by? (all, monday, tuesday, ... sunday)\n").lower()
        if day not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('invalid inputs')
        else:
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
    # load dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert start time into datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from start time  
    df['month'] = df['Start Time'].dt.month
    
    # extract day from start time
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + df['End Station']
    combination_station = df['Combination Station'].value_counts().head(1)
    print('The most frequent combination of start station and end station trip:', combination_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', total_travel_time )
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Total travel mean time is:', mean_time )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user = df['User Type'].value_counts()
    print('count of user types is:', count_user)

    # TO DO: Display counts of gender
    if city != 'washington':
     df['Gender'].fillna('none',inplace=True)
     count_gender = df['Gender'].value_counts()
     print('count of gender is:', count_gender)
    else:
     print('Birth of year is not giving for this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_year = df['Birth Year'].value_counts().idxmax()
        print('earliest year of birth is:', earliest)
        print('recent year of birth is:', recent)
        print('common year of birth is:', common_year)
    else:
        print('Birth of year is not giving for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# to display raw data for the user 
def raw_data(df):
    user_input = input("Do you want to see more raw data? plese enter yes or no.\n").lower()
    line_counter = 0
    while True:
        if user_input.lower() =='yes':
            print(df.iloc[line_counter : line_counter + 5])
            line_counter += 5
            user_input = input("Do you want to see more raw data? plese enter yes or no.\n").lower()
        elif user_input.lower() =='no' :
            break
        else:
            print('invalid inputs')
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
