# Network of Keywords Builder with Hadoop

Keywords network builder based on TF-IDF with the use of Hadoop platform.

Set Up
------

This repository is intended to work with Cloudera Hadoop technology stack,
but can be easily ported to any other Hadoop stacks.

1. Download [this VM](http://content.udacity-data.com/courses/ud617/Cloudera-Udacity-Training-VM-4.1.1.c.zip) used by Cloudera.
2. Log in to VM using `training/training` login/password.
3. Clone this repository using Git.
4. Run the shell script `run_mapreduce.sh`.

Running Keywords Builder
------------------------

TF-IDF metrics are computed using Hadoop. Further processing and graph building
are done after TF-IDF values are computed.

By running the `run_mapreduce.sh` script, you should get similar output to the
following. Note that you can pass a particular file name to analyze to the shell
script, located at `texts` directory: `run_mapreduce.sh animals/dogs.txt`.

Sample output:

```txt
[training@localhost hadoop-network-of-keywords]$ ./run_mapreduce.sh 
Calculating TF-IDF for animals/dogs.txt
Running TF mapreduce...
Removing old results...
Deleted /temp
Putting files to HDFS...
Counting files...
Running TF mapreduce on Hadoop...
packageJobJar: [tf_mapper.py, tf_reducer.py, utils.py, /tmp/hadoop-training/hadoop-unjar2130576302639398747/] [] /tmp/streamjob3394676718562222984.jar tmpDir=null
17/12/15 20:18:44 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
17/12/15 20:18:44 WARN snappy.LoadSnappy: Snappy native library is available
17/12/15 20:18:44 INFO snappy.LoadSnappy: Snappy native library loaded
17/12/15 20:18:44 INFO mapred.FileInputFormat: Total input paths to process : 5
17/12/15 20:18:45 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
17/12/15 20:18:45 INFO streaming.StreamJob: Running job: job_201712151310_0059
17/12/15 20:18:45 INFO streaming.StreamJob: To kill this job, run:
17/12/15 20:18:45 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201712151310_0059
17/12/15 20:18:45 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201712151310_0059
17/12/15 20:18:46 INFO streaming.StreamJob:  map 0%  reduce 0%
17/12/15 20:18:52 INFO streaming.StreamJob:  map 40%  reduce 0%
17/12/15 20:18:58 INFO streaming.StreamJob:  map 80%  reduce 0%
17/12/15 20:19:00 INFO streaming.StreamJob:  map 100%  reduce 0%
17/12/15 20:19:02 INFO streaming.StreamJob:  map 100%  reduce 100%
17/12/15 20:19:04 INFO streaming.StreamJob: Job complete: job_201712151310_0059
17/12/15 20:19:04 INFO streaming.StreamJob: Output: /temp/output
Running DF mapreduce on Hadoop...
packageJobJar: [df_mapper.py, df_reducer.py, utils.py, /tmp/hadoop-training/hadoop-unjar8014481347708058210/] [] /tmp/streamjob4058546107354394043.jar tmpDir=null
17/12/15 20:19:05 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
17/12/15 20:19:05 WARN snappy.LoadSnappy: Snappy native library is available
17/12/15 20:19:05 INFO snappy.LoadSnappy: Snappy native library loaded
17/12/15 20:19:05 INFO mapred.FileInputFormat: Total input paths to process : 1
17/12/15 20:19:05 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
17/12/15 20:19:05 INFO streaming.StreamJob: Running job: job_201712151310_0060
17/12/15 20:19:05 INFO streaming.StreamJob: To kill this job, run:
17/12/15 20:19:05 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201712151310_0060
17/12/15 20:19:05 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201712151310_0060
17/12/15 20:19:06 INFO streaming.StreamJob:  map 0%  reduce 0%
17/12/15 20:19:09 INFO streaming.StreamJob:  map 100%  reduce 0%
17/12/15 20:19:13 INFO streaming.StreamJob:  map 100%  reduce 100%
17/12/15 20:19:15 INFO streaming.StreamJob: Job complete: job_201712151310_0060
17/12/15 20:19:15 INFO streaming.StreamJob: Output: /temp/dfoutput
Getting results into tf_df_output.txt...
```

The result will go to `tf_df_output.txt` file. Each row in this file is a tuple of
three values (term frequency, document frequency, word), separated by tabs. To
calculate TF-IDF, the number of documents is saved to `files_count.txt` file as a
plain number.

Example of `tf_df_output.txt`:

```txt
3       5       a
1       3       and
1       5       are
1       1       awesome
1       1       best
1       1       can
1       1       dog
5       1       dogs
1       1       everybody
1       1       friend
1       1       high
1       3       is
1       1       jump
2       3       love
1       1       man
1       3       of
1       2       other
```

