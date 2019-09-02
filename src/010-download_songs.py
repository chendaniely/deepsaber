import warnings

import pandas as pd
import requests
import numpy as np

from pyprojroot import here

def get_song_id(string):
    parts = string.split('/')
    return parts[-1]

@np.vectorize
def download_file(url, fpth, song_id=None, use_here=True):
    if song_id is None:
        song_id = get_song_id(url)
    if use_here:
        fpth = str(here(fpth))

    r = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        with open(fpth, 'wb') as f:
            f.write(r.content)
    else:
        warnings.warn(f"URL Failed: {url}")



songs = pd.read_csv(here('./data/original/songs.tsv'), sep='\t')

songs['song_url'] = "https://beatsaver.com/beatmap/" + songs['id']
songs['song_dl_url'] = "https://beatsaver.com/api/download/key/" + songs['id']
songs['song_dl_pth'] = "./songs/" + songs['id'] + ".zip"

songs

download_file(songs['song_dl_url'], songs['song_dl_pth'])

songs.to_csv(here('./data/processed/songs.tsv'), sep='\t', index=False)
