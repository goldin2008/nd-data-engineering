import configparser
from datetime import datetime
import os
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.types import TimestampType

config = configparser.ConfigParser()
config.read('aws/dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = os.path.join(input_data, "song_data/*/*/*/")
    
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select(["song_id", "title", "artist_id", "year", "duration"]).distinct()
    songs_table.dropDuplicates()
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.parquet(os.path.join(output_data, 'songs'), mode='overwrite', partitionBy=['year','artist_id'])

    # extract columns to create artists table
    artists_table = df.select(["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]).distinct()
    artists_table.dropDuplicates()
    # write artists table to parquet files
    artists_table.write.parquet(os.path.join(output_data, 'artists'), mode='overwrite', partitionBy=['artist_id'])

def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = os.path.join(input_data, 'log_data/*/*/*.json')

    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.where(df.page == 'NextSong')

    # extract columns for users table    
    users_table = df.select(["userId", "firstName", "lastName", "gender", "level"]).distinct()
    users_table.dropDuplicates()
    
    # write users table to parquet files
    users_table.write.parquet(os.path.join(output_data, 'users'), mode='overwrite', partitionBy = ['userId'])

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x: datetime.fromtimestamp(x/1000), TimestampType())
    df = df.withColumn("timestamp", get_timestamp(col("ts")))
    
    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: to_date(x), TimestampType())
    df = df.withColumn("datetime", get_timestamp(col("ts")))
    
    # extract columns to create time table
    time_table = df.select(F.col('datetime').alias('start_time'),
                           F.hour('datetime').alias('hour'),
                           F.dayofmonth('datetime').alias('day'),
                           F.weekofyear('datetime').alias('week'),
                           F.month('datetime').alias('month'),
                           F.year('datetime').alias('year'),
                           F.date_format('datetime', 'E').alias('weekday')
                           )
    time_table.dropDuplicates()
    # write time table to parquet files partitioned by year and month
    time_table.write.parquet(os.path.join(output_data, 'time'), mode='overwrite', partitionBy=['year', 'month'])

    # read in song data to use for songplays table
    song_df = spark.read.json(os.path.join(input_data, 'song_data/*/*/*/*.json'))

    # extract columns from joined song and log datasets to create songplays table 
    song_df = song_df['artist_id', 'artist_name', 'artist_location', 'song_id', 'title']

    songplays_table = log_df.join(song_df, song_df.artist_name == log_df.artist, "inner").distinct() \
                          .select("userId", "timestamp", "song_id", "artist_id", "level", "sessionId", "location", "userAgent") \
                          .withColumn("songplay_id", monotonically_increasing_id()) \
                          .withColumnRenamed("timestamp","start_time") \
                          .withColumnRenamed("userId","user_id") \
                          .withColumnRenamed("sessionId","session_id") \
                          .withColumnRenamed("userAgent","user_agent")
    songplays_table.dropDuplicates()
    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.parquet(os.path.join(output_data, 'songplays'), mode='overwrite', partitionBy=['start_time', 'user_id'])
    
def main():
    input_data = "data/"
    output_data = "output/"
    spark = create_spark_session()
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)

if __name__ == "__main__":
    main()
