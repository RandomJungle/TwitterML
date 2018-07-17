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

WORLDCUP = ['worldcup','worldcup2018','worldcup2018Finals','FIFAWorldCup','worldcupfever','worldcuprussia',
            'worldcuprussia2018','FIFA','soccer','futbol','worldcupfinal','worldcupsoccer','worldcupwinner',
            'wc2018','France','bleublancrouge','equipedefrance','allezlesbleus','fiersdetrebleus','Croatia',
            'Hrvatska','cro','hns','croatianpride','volimhravatsku','croatiavsfrance','francevscroatia','FRACRO',
            'CROFRA', 'vivelafrance','championsdumonde','paris','final','mbappe','pogba','finale','griezmann', 
            'umtiti','matuidi','giroud','fifa18','champions','coupe','coupedumonde','lesbleus']

try:
    from private import *
except Exception:
    pass