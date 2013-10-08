########
# Before you do this, paste following command into your terminal:
# export ECHO_NEST_API_KEY='Your API Key'
########

import json
import urllib2
import random
import os

key = os.environ['ECHO_NEST_API_KEY']

request = 'http://developer.echonest.com/api/v4/song/search?api_key={api_key}&format=json&results=1&min_danceability=0.{dance}&song_min_hotttnesss=0.{hotness}'.format(api_key = key,dance = random.randint(5,9),
           hotness = random.randint(4,9))

response = urllib2.urlopen(request)
songdata = json.load(response)['response']

#if a song isn't picked, play Creed. Yuck.
if not songdata['songs']:
  print "The song playing on the jukebox is 'Higher' by Creed. It makes you a bit stabby."
else:
  #print the song that's playing
  print "The song playing on the jukebox is {song} by {artist}".format(song = songdata['songs'][0]['title'],artist = songdata['songs'][0]['artist_name'])