import pandas as pd
import datetime as dt
import collections
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
# from wordcloud import WordCloud

# Function to import TwitchTrackerScraper data
# csvPath must be of the format r'csvPath\TwitchTrackerExport.csv' (including the r)
def importCSV(csvPath):

    # Read in the csv
    df = pd.read_csv(csvPath)

    # Drops automatically generated index column
    df.drop('Unnamed: 0', axis=1, inplace=True)

    # Convert Date, Time, and Day columns to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'])

    return df

def ActiveDaysOfWeek(df):
    # Dictionary to hold number of streams by Day of Week
    numDays = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}

    # Populate dictionary
    for day in df['Day']:
        numDays[day] += 1

    # Split dictionary into lists for plotting
    days = list(numDays.keys())
    values = list(numDays.values())

    # Set title and labels of plot
    fig, ax = plt.subplots()
    plt.title('Number of Active Days by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Active Days')

    # Plot values
    ax.barh(days, values, color='grey')

    # Add values to the bars
    for i, value in enumerate(values):
        ax.text(value, i, str(value), color='black')
        xmin, xmax = ax.get_xlim()
        ax.set_xlim(xmin, 1.1*xmax)

    # Display plot
    plt.tight_layout()
    plt.show()

def HoursStreamedDaysOfWeek(df):
    days = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
    values = df.groupby(['Day'])['Duration (hrs)'].sum()

    # Set title and labels of the plot
    fig, ax = plt.subplots()
    plt.title('Hours Streamed by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Hours Streamed')

    # Plot values
    plt.barh(days, values, color = 'red')

    # Add values to the bars
    for i, value in enumerate(values):
        ax.text(value, i, str(value), color='black')
        xmin, xmax = ax.get_xlim()
        ax.set_xlim(xmin, 1.1*xmax)

    # Display plot
    plt.tight_layout()
    plt.show()

def numActiveDaysByYear(df):
    df['Year'] = df['Date'].dt.strftime('%Y')
    firstYear = min(df['Year'])
    lastYear = max(df['Year'])
    allYears = list(range(int(firstYear), int(lastYear)+1))
    days = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday']

    # Initialize plot
    fig, ax = plt.subplots()
    ax.set_xticks(allYears)

    # Start counting Mondays for each year so that bottom bar stays static
    mondays = []
    for year in allYears:
        dfYear = df[(df['Year'] == str(year))]
        dfYearDay = dfYear[dfYear['Day'] == 'Monday']
        mondays.append(len(dfYearDay))

    # Plot Monday bars
    plt.bar(allYears, mondays, label='Mondays')
    plt.show()

def avgNumViewsDaysOfWeek(df):

    # Dictionary to hold number of viewers by Day of Week

    numViews = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}
    numStreams = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}

    # Populate dictionary
    for i in range(len(df)):
        day = df['Day'][i]
        view = df['Views'][i]
        numViews[day] += view
        numStreams[day] += 1

    avgViews = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}
    for key in numViews:
        avgViews[key] = numViews[key]//numStreams[key]

    # Split dictionary into lists for plotting
    days = list(avgViews.keys())
    values = list(avgViews.values())

    # Set title and labels of the plot
    fig, ax = plt.subplots()
    plt.title('Average Number of Views by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Views')

    # Plot values
    plt.barh(days, values, color = 'darkseagreen')

    # Add values to the bars
    for i, value in enumerate(values):
        ax.text(value, i, str(value), color='black')
        xmin, xmax = ax.get_xlim()
        ax.set_xlim(xmin, 1.1*xmax)

    # Display plot
    plt.tight_layout()
    plt.show()

def avgNumFollowersDaysOfWeek(df):

    # Dictionary to hold number of viewers by Day of Week
    numFollowers = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}
    numStreams = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}

    # Populate dictionary
    for i in range(len(df)):
        day = df['Day'][i]
        follower = df['Followers'][i]
        numFollowers[day] += follower
        numStreams[day] += 1

    avgFollowers = {'Sunday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Wednesday': 0, 'Tuesday': 0, 'Monday': 0}
    for key in numFollowers:
        avgFollowers[key] = numFollowers[key]//numStreams[key]

    # Split dictionary into lists for plotting
    days = list(avgFollowers.keys())
    values = list(avgFollowers.values())

    # Set title and labels of the plot
    fig, ax = plt.subplots()
    plt.title('Average Number of Followers by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Followers')

    # Plot values
    plt.barh(days, values, color = 'dodgerblue')

    # Add values to the bars
    for i, value in enumerate(values):
        ax.text(value, i, str(value), color='black')
        xmin, xmax = ax.get_xlim()
        ax.set_xlim(xmin, 1.1*xmax)

    # Display plot
    plt.tight_layout()
    plt.show()

# A function to generate all Day of Week plots
# Includes: Number of Active Days, Number of Active Days by Year, Hours Streamed on Average, Average Number of Viewers, Average number of Followers

def DayOfWeekViz(df):
    return df


def HoursStreamedMonth(df):

    # Create new column containing just months and years
    df['MonthYear'] = df['Date'].dt.strftime('%b-%Y')

    # Get all unique Month Year combinations
    allMonthYears = df.MonthYear.unique()

    # Reverse allMonthYear list so it's ordered from oldest to most recent MonthYear
    allMonthYears = allMonthYears[::-1]

    # Initialize durations list
    durations = []

    for monthyear in allMonthYears:
        # Slice df to only have Month Year combination
        dfMY = df[df['MonthYear'] == monthyear]
        durations.append(dfMY['Duration (hrs)'].sum())

    # Initialize plot
    fig, ax = plt.subplots()
    plt.title('Total Hours Streamed per Month-Year')
    plt.xlabel('Month-Year')
    plt.xticks(rotation = 45)
    plt.ylabel('Hours Streamed')

    # Plot values
    plt.bar(allMonthYears, durations, color = 'red')

    plt.tight_layout()
    plt.show()

def avgCCVMonth(df):

    # Create new column containing just months and years
    df['MonthYear'] = df['Date'].dt.strftime('%b-%Y')

    # Get all unique Month Year combinations
    allMonthYears = df.MonthYear.unique()

    # Reverse allMonthYear list so it's ordered from oldest to most recent MonthYear
    allMonthYears = allMonthYears[::-1]

    # Initialize durations list
    avgCCV = []

    for monthyear in allMonthYears:
        # Slice df to only have Month Year combination
        dfMY = df[df['MonthYear'] == monthyear]
        numStreams = len(dfMY)
        avgCCV.append(dfMY['avgCCV'].sum()/numStreams)

    # Initialize plot
    fig, ax = plt.subplots()
    plt.title('Average Concurrent Viewers per Month')
    plt.xlabel('Month-Year')
    plt.xticks(rotation = 45)
    plt.ylabel('Average Concurrent Viewers')

    # Plot values
    plt.bar(allMonthYears, avgCCV, color = 'darkseagreen')

    plt.tight_layout()
    plt.show()

def followersMonth(df):
    # Create new column containing just months and years
    df['MonthYear'] = df['Date'].dt.strftime('%b-%Y')

    # Get all unique Month Year combinations
    allMonthYears = df.MonthYear.unique()

    # Reverse allMonthYear list so it's ordered from oldest to most recent MonthYear
    allMonthYears = allMonthYears[::-1]

    # Initialize durations list
    followers = []
    for monthyear in allMonthYears:
        # Slice df to only have Month Year combination
        dfMY = df[df['MonthYear'] == monthyear]
        followers.append(dfMY['Followers'].sum())

    # Initialize plot
    fig, ax = plt.subplots()
    plt.title('Followers Gained per Month')
    plt.xlabel('Month-Year')
    plt.xticks(rotation = 45)
    plt.ylabel('Followers Gained')

    # Plot values
    plt.bar(allMonthYears, followers, color = 'dodgerblue')
    plt.tight_layout()
    plt.show()


# Wordcloud library does not work--keep commented out unless working with Python 3.7 or below

#def TitleWordCloud(df):
#    text = " ".join(title for title in df['Title']).lower()
#    wordcloud = WordCloud().generate(text)
#    plt.imshow(wordcloud, interpolation='bilinear')
#    plt.axis("off")
#    plt.tight_layout(pad = 0)
#    plt.show()

# Returns total number of followers
def totalFollowers(df):
    print("Number of followers to date: " + str(df['Followers'].sum()))
    return df['Followers'].sum()

# Returns the total number of views
def totalViews(df):
    print("Number of views to date: " + str(df['Views'].sum()))
    return df['Views'].sum()

# Returns the average time broadcast per stream
def avgStreamTime(df):
    numStreams = len(df)
    avgDuration = df['Duration (hrs)'].sum() // numStreams
    print('Average broadcast time per stream: ' + str(avgDuration))
    return avgDuration

# Returns the total hours streamed
def totalDuration(df):
    print('Total hours streamed: ' + str(df['Duration (hrs)'].sum()))
    return (df['Duration (hrs)'].sum())

# Returns the average number active days per week
def activeDaysPerWeek(df):
    numStreams = len(df)
    first = min(df['Date'])
    last = max(df['Date'])
    numDays = abs(first - last).days
    numWeeks = numDays//7
    print('Average active days per week: ' + str(numStreams/numWeeks))
    return (numStreams/numWeeks)

# Returns average number of followers per stream
def avgNumFollowersPerStream(df):
    numStreams = len(df)
    totalFollowers = df['Followers'].sum()
    print("Average number of followers per stream: " + str(totalFollowers/numStreams))
    return (totalFollowers/numStreams)

# Returns the average number of views per stream
def avgViewsPerStream(df):
    numStreams = len(df)
    totalViews = df['Views'].sum()
    print("Average number of views per stream: " + str(totalViews/numStreams))
    return (totalViews/numStreams)

# Returns the average number of followers gained per hour streamed
def avgFollowersGainedPerHour(df):
    totalHours = df['Duration (hrs)'].sum()
    totalFollowers = df['Followers'].sum()
    print("Average number of followers gained per hour streamed: " + str(totalFollowers/totalHours))
    return(totalFollowers/totalHours)

# Returns the average number of views gained per hour streamed
def avgViewsPerHour(df):
    totalHours = df['Duration (hrs)'].sum()
    totalViews = df['Views'].sum()
    print("Average number of views per hour streamed: " + str(totalViews/totalHours))
    return(totalViews/totalHours)

# Prints all various metrics on Twitch Tracker's statistics page as a table
# Included are: total followers, total views, total duration, and number of active days per week
def variousMetrics(df):

    # Get data for table
    followers = totalFollowers(df)
    views = totalViews(df)
    duration = totalDuration(df)
    days = activeDaysPerWeek(df)

    # Combine metrics for table
    data = [
            ['Total Followers', followers],
            ['Total Views', views],
            ['Total time streaming (hrs)', duration],
            ['Active days per week', days]
    ]

    # Display table
    print(tabulate(data, tablefmt="grid"))

# Prints various per stream metrics as a table
# Included are: average number of followers per stream, average stream time, and average views per stream
def perStreamMetrics(df):

    # Get data for table
    followers = avgNumFollowersPerStream(df)
    streamTime = avgStreamTime(df)
    views = avgViewsPerStream(df)

    # Combine metrics for table
    data = [
            ['Average followers per stream', followers],
            ['Average broadcast time per stream (hrs)', streamTime],
            ['Average views per stream', views]
    ]

    # Display table
    print(tabulate(data, tablefmt="grid"))

# Prints various per hour metrics as a table
# Included are:
def perHourMetrics(df):

    # Get data for table
    followers = avgFollowersGainedPerHour(df)
    views = avgViewsPerHour(df)

    # Combine metrics for table
    data = [
            ['Average followers gained per hour streamed', followers],
            ['Average views per hour', views],
    ]

    # Display table
    print(tabulate(data, tablefmt="grid"))

if __name__ == '__main__':
    df = importCSV(r'C:\Users\Isabella\Documents\Projects\Twitch Tracker Visualizations\TwitchTrackerExport.csv')

# Day of Week Analysis Plots
    #ActiveDaysOfWeek(df)
    #HoursStreamedDaysOfWeek(df)

    #TODO
    #numActiveDaysByYear(df)

    #avgNumViewersDaysOfWeek(df)
    #avgNumFollowersDaysOfWeek(df)

# Month Analysis
    #HoursStreamedMonth(df)
    #avgCCVMonth(df)
    #followersMonth(df)

# All Month visualizations
    monthViz(df)

# Wordcloud (currently does not work)
    # TitleWordCloud(df)

# Statistics
    #totalFollowers(df)
    #totalViews(df)
    #avgStreamTime(df)
    #totalDuration(df)

    #activeDaysPerWeek(df)
    #avgNumFollowersPerStream(df)
    #avgViewsPerStream(df)

    #avgFollowersGainedPerHour(df)
    #avgViewsPerHour(df)

# Stat Tables
    #variousMetrics(df)
    #perStreamMetrics(df)
    #perHourMetrics(df)
