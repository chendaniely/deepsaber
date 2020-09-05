import pandas as pd
import soundfile as sf

from pyprojroot import here

import src.beatsaber as bs

pd.set_option('precision', 20)

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
df_map['_events'][0][0]

def list_dict_to_df(df, colname, index_name='_time'):
    df = pd.DataFrame(df[colname][0])
    df.index = df[index_name]
    df = df.drop('_time', axis='columns')
    df.columns = df.columns.str.replace('_', f"{colname.replace('_', '')}_")
    return(df)

events_df = list_dict_to_df(df_map, '_events')
notes_df = list_dict_to_df(df_map, '_notes')
obstacles_df = list_dict_to_df(df_map, '_obstacles')

df_map_tidy = pd.concat([events_df, notes_df, obstacles_df], axis='columns')

df_map_tidy.shape

df_map_tidy.events_type.value_counts(sort=False, dropna=False).sort_index()
df_map_tidy.notes_type.value_counts(sort=False, dropna=False).sort_index()
df_map_tidy.obstacles_type.value_counts(sort=False, dropna=False).sort_index()


import matplotlib.pyplot as plt


plt.plot(data)
plt.show()

df_song = pd.DataFrame(data)
df_song


df_map_tidy.index * samplerate