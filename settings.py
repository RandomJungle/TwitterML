import re

API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

with open('stopwords.txt', 'r', encoding='utf-8') as stopfile:
    STOPWORDS = set([word for word in stopfile.readlines()])

EMOJIS = ['\N{UNAMUSED FACE}', 
        #'\N{LOUDLY CRYING FACE}',
        #'\N{FACE WITH TEARS OF JOY}',
        '\N{FACE THROWING A KISS}']
        #'\N{POUTING FACE}',
        #'\N{WEARY FACE}',]
        #\N{PENSIVE FACE}]

try:
    from private import *
except Exception:
    pass