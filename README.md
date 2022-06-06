# Twitch Tracker Viz

Included in this repo are recreations of the Statistics page on Twitch Tracker, all made using the csv export from my Twitch Tracker Scraper. Two versions of the visualizations are available: one using Python and another using PowerBI.

The data import must be in the following format (first column is an index column):


||Date|Time|Day|Duration (hrs)|avgCCV|maxCCV|Followers|Views|Title|
|-|----|----|----|----|----|----|----|----|----|
|0|6/1/2022|00:53:00|Wednesday|2.5|64|85|-1|0|StreamTitle|

I may come back to this and make a Tableau version eventually when I decide to practice Tableau more, but that's for future me. :)

## Known Issues
 * The WordCloud feature only works in Python 3.7 or below due to the library being incompatible with more recent versions of Python. Due to this, the code has been commented out.

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
    * A function to generate all Month plots at once
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
