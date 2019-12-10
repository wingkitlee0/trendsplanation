"""
Some useful functions for analyzing Trending Tweets data
"""
import pandas as pd
import datetime

DEFAULT_DATA_DIR = '../TwitterTrends_data'

class TTUtil:
    """
    A class for useful functions
    """
    def __init__(self, datadir=DEFAULT_DATA_DIR):
        self.datadir = datadir
        self.trends = pd.read_csv(self.datadir+'/trends.csv')

        # create a dictionary {topic : hash_value}
        self.trend2hash = dict( [(row[4], row[2]) for row in self.trends.itertuples()])
        # reverse dictionary
        self.hash2trend = {v: k for k, v in self.trend2hash.items()}

    def get_full_tweets_file(self, topic='Indiana Jones'):
        """
        return the filename (with relative path) for an topic 
        """
        hash_ = self.trend2hash[topic]
        filename = self.datadir + '/full_tweets/' + hash_ + '.csv'
        return filename

    def convert2datetime(self, str_input):
        """
        convert the string (e.g., in the 'created_at' column) into a datetime object
        """
        return datetime.datetime.strptime(str_input.replace(' +0000', ''), '%a %b %d %H:%M:%S %Y')

    def get_hash_from_filename(self, fname):
        """
        return the hash from the filename with path
        """
        return fname.split('/')[-1][:-4]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

if __name__ == "__main__":
    myutil = TTUtil()

