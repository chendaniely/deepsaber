import soundfile as sf

from pyprojroot import here

import src.beatsaber as bs

data, samplerate = sf.read(here("./songs/294c/song.egg")) # manually renamed song.egg


data
samplerate

data.shape
data.shape[0] / samplerate / 60 ## this is 3:41 in time min:sec

df_map_meta = bs.read_info(here("./songs/294c/info.dat"))

df_map_meta

df_map = bs.read_difficulty_map(here("./songs/294c/Normal.dat"))
df_map

#f = here("./songs/294c/Normal.dat")
#f

df_map['_events']
df_map['_events'][0]
