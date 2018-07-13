Information Extraction project based on twitter data and exploration based on hashtags and use of emojis

In respect to the Twitter licensing, the dataset is not provided, only the files containing Tweet's IDs. The Tweets can, however, be retrieved, provided key authentifications to twitter API.

There are 4 different corpora :

- "data_emoji_2.txt" is a list of IDs for tweets classified according to their use of 3 emojis (refered by the Unicode consortium as 'loudly crying face', 'face with tears of joy' and 'weary face'). Those were chosen based on their high ranking of use on twitter

- "data_emoji_4.txt" is a list of IDs for tweets with 3 other emojis : "unamused face", "face throwing a kiss" and "face with tears of joy" (as named by the Unicode Consortium). Only extended tweets (longer than 140 characters) were kept for the dataset (in order to obtain more features). Those were chosen for the dissimilarity they expressed, and the @usernames where also removed.

- "data_hashtag_fr.txt" is a collection of french tweets organized according to their first hashtag.

- "data_hashtag_en.txt" is a collection of english tweets organized accoridng to their first hahstag.

All data was cleaned from URL and retweets are not included in any part of the different datasets, in order to avoid duplicates.
