import feedparser
import os
import pandas as pd
import pickle

# Parse the RSS feed at the first URL
feed = feedparser.parse("http://www.spotternetwork.org/feeds/rss-reports.xml")

# Create a pandas dataframe from the RSS feed data
df = pd.DataFrame(feed.entries)

# Parse the RSS feed at the second URL
feed2 = feedparser.parse("http://www.spotternetwork.org/feeds/rss-positions.xml")

# Create a pandas dataframe from the RSS feed data
df2 = pd.DataFrame(feed2.entries)

# Save the pandas dataframe as a pickled file in the /data/ folder

with open('data/spotternetwork_reports_{}.pkl'.format(len(os.listdir('data/'))), 'wb') as file:
    pickle.dump(df, file)
with open('data/spotternetwork_positions_{}.pkl'.format(len(os.listdir('data/'))), 'wb') as file:
    pickle.dump(df2, file)