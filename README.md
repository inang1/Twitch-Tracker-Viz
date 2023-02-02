# Twitch Tracker Viz

Included in this repo are recreations of the Statistics page on Twitch Tracker, all made using the csv export from my Twitch Tracker Scraper. Two versions of the visualizations are available: one using Python and another using PowerBI.

The code is messy, and needs to be organized/changed to match style guidelines, but I built this just to work on visualization skills, so please bear with me :)

The data import must be in the following format (first column is an index column):


||Date|Time|Day|Duration (hrs)|avgCCV|maxCCV|Followers|Views|Title|
|-|----|----|----|----|----|----|----|----|----|
|0|6/1/2022|00:53:00|Wednesday|2.5|64|85|-1|0|StreamTitle|

I may come back to this and make a Tableau version eventually when I decide to practice Tableau more, but that's for future me.

## Known Issues
 * The WordCloud feature only works in Python 3.7 or below due to the library being incompatible with more recent versions of Python. Due to this, the code has been commented out.

## List of functions
#### Day of Week Analysis Plots

  1. ActiveDaysOfWeek(df)
  2. HoursStreamedDaysOfWeek(df)
  3. numActiveDaysByYear(df)
  4. avgNumViewersDaysOfWeek(df)
  5. avgNumFollowersDaysOfWeek(df)

#### All Day of Week Plots
  1. DayOfWeekViz(df)

#### Month Analysis
  1. HoursStreamedMonth(df)
  2. avgCCVMonth(df)
  3. followersMonth(df)

#### All Month visualizations
  1. monthViz(df)

#### Wordcloud (currently does not work)
  1. TitleWordCloud(df)

#### Statistics
  1. totalFollowers(df)
  2. totalViews(df)
  3. avgStreamTime(df)
  4. totalDuration(df)
  5. activeDaysPerWeek(df)
  6. avgNumFollowersPerStream(df)
  7. avgViewsPerStream(df)
  8. avgFollowersGainedPerHour(df)
  9. avgViewsPerHour(df)

#### Stat Tables
  1. variousMetrics(df)
  2. perStreamMetrics(df)
  3. perHourMetrics(df)

## Things to Do
### Python:
  1. Day of the Week Analysis:
    * Number of Active Days by Year (Need to figure out how to do this dynamically instead of having a list for each and every day of the week)
  2. Day of Week Viz:
   * A function to generate all Day of Week Analysis plots at once
  3. Month Analysis:
    * Need to add labels to each bar for all Month Analysis
      * Hours Streamed
      * Average Concurrent Viewers
      * Followers Gained
  4. Month Viz:
    * Add labels to each bar like above
  5. Refactor code to be object oriented (every single function requires the dataframe to be an input, which looks awful)
  6. Reformat comments/change function naming to match conventions

### PowerBI
  1. Day of the Week Analysis:
    * Reorder columns in all charts
  2. Statistics by Month: Hours Streamed, Concurrent Viewers, Followers Gained
    * Need to create a new table that indexes using Month Year
    * Need to create a columns that have a running total of number of Followers (for the line graph)
    * Hours Streamed by Month
    * Average Concurrent Viewers by Month
    * Average Followers Gained by Month
  3. Visualization combining total followers, total views, hours streamed, hours watched, average viewers, and active days
  4. Create PowerQuery function to format any TwitchTracker dataset to reformat all datasets to work with the visualizations.
