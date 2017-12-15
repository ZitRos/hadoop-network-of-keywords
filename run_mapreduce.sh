printf "Running TF mapreduce...\n"
printf "Removing old results...\n"
rm tf_output.txt -f
hadoop fs -rm -r /temp

printf "Putting files to HDFS...\n"
hadoop fs -mkdir /temp
hadoop fs -mkdir /temp/input
# /temp/output must not exists beforehand
hadoop fs -put texts/* /temp/input

printf "Running mapreduce on Hadoop...\n"
hadoop jar \
     /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar \
     -mapper tf_mapper.py \
     -reducer tf_reducer.py \
     -file tf_mapper.py \
     -file tf_reducer.py \
     -file utils.py \
     -input /temp/input/* \
     -output /temp/output

printf "Getting results back...\n"
hadoop fs -get "/temp/output/part-00000"
mv "part-00000" tf_output.txt

printf "Results are written to file tf_output.txt\nDone!\n"
