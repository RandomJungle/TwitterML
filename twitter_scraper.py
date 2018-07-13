import tweepy
import json
import sys
import re
import codecs
import settings

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class HashtagStreamListener(tweepy.StreamListener):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def on_status(self, status):
        
        # Only interested in french tweets
        lang = status.lang
        if lang == 'en' :

            # And in tweets that have a hashtag (I only use the first one)
            hashtags = status.entities['hashtags']
            if hashtags:

                # Check for presence of attribute extended_tweet, in case tweet is in 280 chars (and delete tabs, newlines and such)
                if hasattr(status, 'extended_tweet'):
                    text = re.sub('[\t\n\r\f\v]', ' ', status.extended_tweet['full_text'])
                else:
                    text = re.sub('[\t\n\r\f\v]', ' ', status.text)

                # This is to avoid retweets, I'm worried about possible noise caused by duplicates
                if not text.startswith('RT'):
                    hashtag = hashtags[0]['text']
                    ID = status.id
                    timestamp = status.timestamp_ms

                    # Deleting the hashtags and urls inside the text of the tweets to not mess up the model
                    text = re.sub("#([\w])*", ' ', text)
                    text = re.sub("https([\S])*", ' ', text)
                    text = re.sub("(\s){2,}", ' ', text)

                    # Write extracted data to csv file
                    with open(self.filename+'.csv', 'a', encoding='utf-8') as datafile, open(self.filename+'.txt', 'a', encoding='utf-8') as idfile:
                        datafile.write("{0}\t{1}\t{2}\t{3}\n".format(ID, timestamp, text, hashtag))
                        idfile.write(str(ID) + '\n')

class EmojiStreamListener(tweepy.StreamListener):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def on_status(self, status):
        
        # Only interested in french tweets
        lang = status.lang
        if lang == 'en' and status.retweeted == False:

            # Check for presence of attribute extended_tweet, in case tweet is in 280 chars (and delete tabs, newlines and such)
            if hasattr(status, 'extended_tweet'):
                text = re.sub('[\t\n\r\f\v]', ' ', status.extended_tweet['full_text'])
            #else:
            #    text = re.sub('[\t\n\r\f\v]', ' ', status.text)

                # This is to avoid retweets, I'm worried about possible noise caused by duplicates
                if not text.startswith('RT'):

                    # Check for presence of requested emoji
                    containsEmoji = False
                    emoji = ''
                    for emo in settings.EMOJIS :
                        if emo in text :
                            containsEmoji = True
                            if emo == '\N{UNAMUSED FACE}':
                                emoji = 'unamused'
                            elif emo == '\N{LOUDLY CRYING FACE}' :
                                emoji = 'loudcry'
                            elif emo == '\N{FACE WITH TEARS OF JOY}' :
                                emoji = 'tearjoy'
                            elif emo == '\N{POUTING FACE}' :
                                emoji = 'pouting'
                            elif emo == '\N{WEARY FACE}' :        
                                emoji = 'weary'
                            elif emo == '\N{PENSIVE FACE}' :        
                                emoji = 'pensive'
                            elif emo == '\N{FACE THROWING A KISS}':
                                emoji = 'kiss'

                    if containsEmoji:
                        ID = status.id
                        timestamp = status.timestamp_ms

                        # Clearing url from tweet's text
                        text = re.sub("https([\S])*", ' ', text)
                        text = re.sub("@([\w])*", ' ', text)
                        text = re.sub("(\s){2,}", ' ', text)

                        # Write extracted data to csv file, and to corresponding idfile
                        with open(self.filename+'.csv', 'a', encoding='utf-8') as datafile, open(self.filename+'.txt', 'a', encoding='utf-8') as idfile:
                            datafile.write("{0}\t{1}\t{2}\t{3}\n".format(ID, timestamp, text, emoji))
                            idfile.write(str(ID) + '\n')

if __name__ == '__main__':

    mode = 'emoji'
    #mode = 'hashtag'

    if mode == 'emoji':
        emoji_stream_listener = EmojiStreamListener('data_emojis_4')
        emoji_stream = tweepy.Stream(auth = api.auth, listener=emoji_stream_listener)
        emoji_stream.filter(track=settings.EMOJIS)

    elif mode == 'hashtag':
        hashtag_stream_listener = HashtagStreamListener('data_hashtags')
        hashtag_stream = tweepy.Stream(auth = api.auth, listener=hashtag_stream_listener)
        hashtag_stream.filter(track=settings.STOPWORDS)