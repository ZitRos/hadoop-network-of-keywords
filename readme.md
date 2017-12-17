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
Calculating TF-IDF for tech/ink-helps-drive-democracy-in-asia.txt
Running TF mapreduce...
Removing old results...
Deleted /temp
Putting files to HDFS...
Counting files...
Running TF mapreduce on Hadoop...
packageJobJar: [tf_mapper.py, tf_reducer.py, utils.py, /tmp/hadoop-training/hadoop-unjar7892492009998614173/] [] /tmp/streamjob4399530855769057884.jar tmpDir=null
17/12/16 21:15:56 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
17/12/16 21:15:56 WARN snappy.LoadSnappy: Snappy native library is available
17/12/16 21:15:56 INFO snappy.LoadSnappy: Snappy native library loaded
17/12/16 21:15:56 INFO mapred.FileInputFormat: Total input paths to process : 2095
17/12/16 21:15:58 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
17/12/16 21:15:58 INFO streaming.StreamJob: Running job: job_201712162108_0001
17/12/16 21:15:58 INFO streaming.StreamJob: To kill this job, run:
17/12/16 21:15:58 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201712162108_0001
17/12/16 21:15:58 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201712162108_0001
17/12/16 21:15:59 INFO streaming.StreamJob:  map 0%  reduce 0%
17/12/16 21:16:23 INFO streaming.StreamJob:  map 1%  reduce 0%
17/12/16 21:16:57 INFO streaming.StreamJob:  map 2%  reduce 0%
17/12/16 21:17:34 INFO streaming.StreamJob:  map 3%  reduce 0%
17/12/16 21:18:08 INFO streaming.StreamJob:  map 4%  reduce 0%
17/12/16 21:18:45 INFO streaming.StreamJob:  map 5%  reduce 0%
17/12/16 21:19:12 INFO streaming.StreamJob:  map 5%  reduce 2%
17/12/16 21:19:22 INFO streaming.StreamJob:  map 6%  reduce 2%
17/12/16 21:20:01 INFO streaming.StreamJob:  map 7%  reduce 2%
17/12/16 21:20:42 INFO streaming.StreamJob:  map 8%  reduce 2%
17/12/16 21:20:43 INFO streaming.StreamJob:  map 8%  reduce 3%
17/12/16 21:21:22 INFO streaming.StreamJob:  map 9%  reduce 3%
17/12/16 21:21:57 INFO streaming.StreamJob:  map 10%  reduce 3%
17/12/16 21:22:31 INFO streaming.StreamJob:  map 11%  reduce 3%
17/12/16 21:22:32 INFO streaming.StreamJob:  map 11%  reduce 4%
17/12/16 21:23:08 INFO streaming.StreamJob:  map 12%  reduce 4%
17/12/16 21:23:42 INFO streaming.StreamJob:  map 13%  reduce 4%
17/12/16 21:24:19 INFO streaming.StreamJob:  map 14%  reduce 4%
17/12/16 21:24:24 INFO streaming.StreamJob:  map 14%  reduce 5%
17/12/16 21:24:55 INFO streaming.StreamJob:  map 15%  reduce 5%
17/12/16 21:25:34 INFO streaming.StreamJob:  map 16%  reduce 5%
17/12/16 21:26:08 INFO streaming.StreamJob:  map 17%  reduce 5%
17/12/16 21:26:09 INFO streaming.StreamJob:  map 17%  reduce 6%
17/12/16 21:26:46 INFO streaming.StreamJob:  map 18%  reduce 6%
17/12/16 21:27:21 INFO streaming.StreamJob:  map 19%  reduce 6%
17/12/16 21:27:57 INFO streaming.StreamJob:  map 20%  reduce 6%
17/12/16 21:27:59 INFO streaming.StreamJob:  map 20%  reduce 7%
17/12/16 21:28:32 INFO streaming.StreamJob:  map 21%  reduce 7%
17/12/16 21:29:08 INFO streaming.StreamJob:  map 22%  reduce 7%
17/12/16 21:29:42 INFO streaming.StreamJob:  map 23%  reduce 7%
17/12/16 21:29:45 INFO streaming.StreamJob:  map 23%  reduce 8%
17/12/16 21:30:19 INFO streaming.StreamJob:  map 24%  reduce 8%
17/12/16 21:30:53 INFO streaming.StreamJob:  map 25%  reduce 8%
17/12/16 21:31:30 INFO streaming.StreamJob:  map 26%  reduce 8%
17/12/16 21:31:33 INFO streaming.StreamJob:  map 26%  reduce 9%
17/12/16 21:32:04 INFO streaming.StreamJob:  map 27%  reduce 9%
17/12/16 21:32:41 INFO streaming.StreamJob:  map 28%  reduce 9%
17/12/16 21:33:15 INFO streaming.StreamJob:  map 29%  reduce 9%
17/12/16 21:33:22 INFO streaming.StreamJob:  map 29%  reduce 10%
17/12/16 21:33:52 INFO streaming.StreamJob:  map 30%  reduce 10%
17/12/16 21:34:27 INFO streaming.StreamJob:  map 31%  reduce 10%
17/12/16 21:35:01 INFO streaming.StreamJob:  map 32%  reduce 11%
17/12/16 21:35:38 INFO streaming.StreamJob:  map 33%  reduce 11%
17/12/16 21:36:12 INFO streaming.StreamJob:  map 34%  reduce 11%
17/12/16 21:36:48 INFO streaming.StreamJob:  map 35%  reduce 11%
17/12/16 21:36:50 INFO streaming.StreamJob:  map 35%  reduce 12%
17/12/16 21:37:23 INFO streaming.StreamJob:  map 36%  reduce 12%
17/12/16 21:37:59 INFO streaming.StreamJob:  map 37%  reduce 12%
17/12/16 21:38:34 INFO streaming.StreamJob:  map 38%  reduce 12%
17/12/16 21:38:36 INFO streaming.StreamJob:  map 38%  reduce 13%
17/12/16 21:39:08 INFO streaming.StreamJob:  map 39%  reduce 13%
17/12/16 21:39:45 INFO streaming.StreamJob:  map 40%  reduce 13%
17/12/16 21:40:19 INFO streaming.StreamJob:  map 41%  reduce 13%
17/12/16 21:40:23 INFO streaming.StreamJob:  map 41%  reduce 14%
17/12/16 21:40:56 INFO streaming.StreamJob:  map 42%  reduce 14%
17/12/16 21:41:29 INFO streaming.StreamJob:  map 43%  reduce 14%
17/12/16 21:42:06 INFO streaming.StreamJob:  map 44%  reduce 14%
17/12/16 21:42:08 INFO streaming.StreamJob:  map 44%  reduce 15%
17/12/16 21:42:44 INFO streaming.StreamJob:  map 45%  reduce 15%
17/12/16 21:43:20 INFO streaming.StreamJob:  map 46%  reduce 15%
17/12/16 21:43:53 INFO streaming.StreamJob:  map 47%  reduce 15%
17/12/16 21:43:57 INFO streaming.StreamJob:  map 47%  reduce 16%
17/12/16 21:44:30 INFO streaming.StreamJob:  map 48%  reduce 16%
17/12/16 21:45:16 INFO streaming.StreamJob:  map 49%  reduce 16%
17/12/16 21:45:51 INFO streaming.StreamJob:  map 50%  reduce 16%
17/12/16 21:45:54 INFO streaming.StreamJob:  map 50%  reduce 17%
17/12/16 21:46:25 INFO streaming.StreamJob:  map 51%  reduce 17%
17/12/16 21:46:59 INFO streaming.StreamJob:  map 52%  reduce 17%
17/12/16 21:47:36 INFO streaming.StreamJob:  map 53%  reduce 17%
17/12/16 21:47:39 INFO streaming.StreamJob:  map 53%  reduce 18%
17/12/16 21:48:11 INFO streaming.StreamJob:  map 54%  reduce 18%
17/12/16 21:48:47 INFO streaming.StreamJob:  map 55%  reduce 18%
17/12/16 21:49:21 INFO streaming.StreamJob:  map 56%  reduce 18%
17/12/16 21:49:25 INFO streaming.StreamJob:  map 56%  reduce 19%
17/12/16 21:49:57 INFO streaming.StreamJob:  map 57%  reduce 19%
17/12/16 21:50:32 INFO streaming.StreamJob:  map 58%  reduce 19%
17/12/16 21:51:08 INFO streaming.StreamJob:  map 59%  reduce 19%
17/12/16 21:51:11 INFO streaming.StreamJob:  map 59%  reduce 20%
17/12/16 21:51:43 INFO streaming.StreamJob:  map 60%  reduce 20%
17/12/16 21:52:18 INFO streaming.StreamJob:  map 61%  reduce 20%
17/12/16 21:52:55 INFO streaming.StreamJob:  map 62%  reduce 20%
17/12/16 21:52:57 INFO streaming.StreamJob:  map 62%  reduce 21%
17/12/16 21:53:29 INFO streaming.StreamJob:  map 63%  reduce 21%
17/12/16 21:54:06 INFO streaming.StreamJob:  map 64%  reduce 21%
17/12/16 21:54:40 INFO streaming.StreamJob:  map 65%  reduce 21%
17/12/16 21:54:43 INFO streaming.StreamJob:  map 65%  reduce 22%
17/12/16 21:55:17 INFO streaming.StreamJob:  map 66%  reduce 22%
17/12/16 21:55:51 INFO streaming.StreamJob:  map 67%  reduce 22%
17/12/16 21:56:28 INFO streaming.StreamJob:  map 68%  reduce 22%
17/12/16 21:56:29 INFO streaming.StreamJob:  map 68%  reduce 23%
17/12/16 21:57:01 INFO streaming.StreamJob:  map 69%  reduce 23%
17/12/16 21:57:38 INFO streaming.StreamJob:  map 70%  reduce 23%
17/12/16 21:58:12 INFO streaming.StreamJob:  map 71%  reduce 23%
17/12/16 21:58:14 INFO streaming.StreamJob:  map 71%  reduce 24%
17/12/16 21:58:46 INFO streaming.StreamJob:  map 72%  reduce 24%
17/12/16 21:59:24 INFO streaming.StreamJob:  map 73%  reduce 24%
17/12/16 21:59:58 INFO streaming.StreamJob:  map 74%  reduce 24%
17/12/16 22:00:00 INFO streaming.StreamJob:  map 74%  reduce 25%
17/12/16 22:00:35 INFO streaming.StreamJob:  map 75%  reduce 25%
17/12/16 22:01:08 INFO streaming.StreamJob:  map 76%  reduce 25%
17/12/16 22:01:45 INFO streaming.StreamJob:  map 77%  reduce 25%
17/12/16 22:01:49 INFO streaming.StreamJob:  map 77%  reduce 26%
17/12/16 22:02:19 INFO streaming.StreamJob:  map 78%  reduce 26%
17/12/16 22:02:55 INFO streaming.StreamJob:  map 79%  reduce 26%
17/12/16 22:03:30 INFO streaming.StreamJob:  map 80%  reduce 26%
17/12/16 22:03:31 INFO streaming.StreamJob:  map 80%  reduce 27%
17/12/16 22:04:04 INFO streaming.StreamJob:  map 81%  reduce 27%
17/12/16 22:04:40 INFO streaming.StreamJob:  map 82%  reduce 27%
17/12/16 22:05:15 INFO streaming.StreamJob:  map 83%  reduce 27%
17/12/16 22:05:18 INFO streaming.StreamJob:  map 83%  reduce 28%
17/12/16 22:05:51 INFO streaming.StreamJob:  map 84%  reduce 28%
17/12/16 22:06:25 INFO streaming.StreamJob:  map 85%  reduce 28%
17/12/16 22:07:01 INFO streaming.StreamJob:  map 86%  reduce 28%
17/12/16 22:07:03 INFO streaming.StreamJob:  map 86%  reduce 29%
17/12/16 22:07:35 INFO streaming.StreamJob:  map 87%  reduce 29%
17/12/16 22:08:11 INFO streaming.StreamJob:  map 88%  reduce 29%
17/12/16 22:08:45 INFO streaming.StreamJob:  map 89%  reduce 29%
17/12/16 22:08:49 INFO streaming.StreamJob:  map 89%  reduce 30%
17/12/16 22:09:22 INFO streaming.StreamJob:  map 90%  reduce 30%
17/12/16 22:09:55 INFO streaming.StreamJob:  map 91%  reduce 30%
17/12/16 22:10:29 INFO streaming.StreamJob:  map 92%  reduce 30%
17/12/16 22:10:32 INFO streaming.StreamJob:  map 92%  reduce 31%
17/12/16 22:11:05 INFO streaming.StreamJob:  map 93%  reduce 31%
17/12/16 22:11:39 INFO streaming.StreamJob:  map 94%  reduce 31%
17/12/16 22:12:18 INFO streaming.StreamJob:  map 95%  reduce 31%
17/12/16 22:12:20 INFO streaming.StreamJob:  map 95%  reduce 32%
17/12/16 22:12:52 INFO streaming.StreamJob:  map 96%  reduce 32%
17/12/16 22:13:38 INFO streaming.StreamJob:  map 97%  reduce 32%
17/12/16 22:14:12 INFO streaming.StreamJob:  map 98%  reduce 32%
17/12/16 22:14:15 INFO streaming.StreamJob:  map 98%  reduce 33%
17/12/16 22:14:49 INFO streaming.StreamJob:  map 99%  reduce 33%
17/12/16 22:15:23 INFO streaming.StreamJob:  map 100%  reduce 33%
17/12/16 22:15:44 INFO streaming.StreamJob:  map 100%  reduce 74%
17/12/16 22:15:47 INFO streaming.StreamJob:  map 100%  reduce 83%
17/12/16 22:15:50 INFO streaming.StreamJob:  map 100%  reduce 92%
17/12/16 22:15:54 INFO streaming.StreamJob:  map 100%  reduce 100%
17/12/16 22:15:55 INFO streaming.StreamJob: Job complete: job_201712162108_0001
17/12/16 22:15:55 INFO streaming.StreamJob: Output: /temp/output
Running DF mapreduce on Hadoop...
packageJobJar: [df_mapper.py, df_reducer.py, utils.py, /tmp/hadoop-training/hadoop-unjar8254911625928607214/] [] /tmp/streamjob64323986015252274.jar tmpDir=null
17/12/16 22:15:57 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
17/12/16 22:15:57 WARN snappy.LoadSnappy: Snappy native library is available
17/12/16 22:15:57 INFO snappy.LoadSnappy: Snappy native library loaded
17/12/16 22:15:57 INFO mapred.FileInputFormat: Total input paths to process : 1
17/12/16 22:15:57 INFO streaming.StreamJob: getLocalDirs(): [/var/lib/hadoop-hdfs/cache/training/mapred/local]
17/12/16 22:15:57 INFO streaming.StreamJob: Running job: job_201712162108_0002
17/12/16 22:15:57 INFO streaming.StreamJob: To kill this job, run:
17/12/16 22:15:57 INFO streaming.StreamJob: UNDEF/bin/hadoop job  -Dmapred.job.tracker=0.0.0.0:8021 -kill job_201712162108_0002
17/12/16 22:15:57 INFO streaming.StreamJob: Tracking URL: http://0.0.0.0:50030/jobdetails.jsp?jobid=job_201712162108_0002
17/12/16 22:15:58 INFO streaming.StreamJob:  map 0%  reduce 0%
17/12/16 22:16:03 INFO streaming.StreamJob:  map 100%  reduce 0%
17/12/16 22:16:11 INFO streaming.StreamJob:  map 100%  reduce 95%
17/12/16 22:16:13 INFO streaming.StreamJob:  map 100%  reduce 100%
17/12/16 22:16:14 INFO streaming.StreamJob: Job complete: job_201712162108_0002
17/12/16 22:16:14 INFO streaming.StreamJob: Output: /temp/dfoutput
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

