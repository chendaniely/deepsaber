import json
import pandas as pd

def read_json(f):
    with open(f, "r") as read_file:
            data = json.load(read_file)
    return(data)

def read_info(f):
    data = read_json(f)

    difficulty_beatmap_sets =  data['_difficultyBeatmapSets'].pop()
    del data['_difficultyBeatmapSets'] # why need to del key here

    df = pd.DataFrame(data).iloc[[0]] ## why I need to index the first row?
    df['_difficultyBeatmapSets'] = [difficulty_beatmap_sets]
    return(df)

def read_difficulty_map(f):
    data = read_json(f)
    events = data.pop('_events')
    notes = data.pop('_notes')
    obstacles = data.pop('_obstacles') # why do not need to del key here

    df = pd.DataFrame.from_dict(data)
    df['_events'] = [events]
    df['_notes'] = [events]
    df['_obstacles'] = [events]

    return(df)
