import pandas as pd
import zipfile
import numpy as np

from pyprojroot import here

@np.vectorize
def zipfile_extractall_vec(zip_file, extract_path=None, use_here=True):
    if use_here:
        zip_file = here(zip_file)
        extract_path = here(extract_path)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_path)

songs = pd.read_csv(here('./data/processed/songs.tsv'), sep='\t')

songs['song_zip_extract_pth'] = './songs/' + songs['id']

zipfile_extractall_vec(songs['song_dl_pth'], songs['song_zip_extract_pth'])
