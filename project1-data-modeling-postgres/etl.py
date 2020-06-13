import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Processes song data files and insert the resulting
    data into `songs` and `artists` dimensional tables.
    """
    # open song file
#     df = 
    df = pd.read_json(filepath, lines=True)

    # insert song record
#     song_data = 
    song_data = df[["song_id", "title", "artist_id", "year", "duration"]].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
#     artist_data = 
    artists_df = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]]
    # Note: To avoid inserting NaN's on the table a little extra code to replace NaN's with None has been applied. Based on https://www.postgresql.org/message-id/55D6639A.8040503@aklaver.com
    artists_df = artists_df.where(pd.notnull(df), None)
    artist_data = artists_df.values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Processes log data files and insert the resulting
    data into `users` and `time` dimensional tables, and 
    the `songplays` fact table.
    """    
    # open log file
#     df = 
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
#     df = 
    df = df[df.page == 'NextSong']

    # convert timestamp column to datetime
#     t = 
    t = pd.to_datetime(df.ts, unit='ms')
    
    # insert time data records
#     time_data = 
#     column_labels = 
#     time_df = 
    time_data = (df.ts.values, t.dt.hour.values, t.dt.day.values, t.dt.week.values, t.dt.month.values, t.dt.year.values, t.dt.weekday.values)
    column_labels = ('timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday')    
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
#     user_df = 
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
#         songplay_data = 
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Look for data files recursevely based on the filepath,
    then uses the function passed as paramenter to processs
    them.
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()