########
# Before you do this, paste following command into your terminal:
# export ECHO_NEST_API_KEY='Your API Key'
########

from pyechonest import config
from pyechonest import playlist
from pyechonest import song
import os

config.ECHO_NEST_API_KEY=os.environ['ECHO_NEST_API_KEY']
p = playlist.Playlist(type='artist-radio', artist_pick='song_hotttnesss-desc', artist="The New Pornographers", mood=None, min_danceability=0.4, min_energy=0.4, adventurousness=0.600001, key='3', limit=False)
print p.get_current_songs()
print p.get_next_songs()

club_dance = song.search(results=1,description='dance',mood='club',min_danceability=0.4,song_min_hotttnesss=0.5,buckets=['id:7digital-US'])
print club_dance[0].id

print club_dance[0].title + " - " + club_dance[0].artist_name


