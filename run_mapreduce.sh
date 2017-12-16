if [ -z ${1+x} ]
then
	file="animals/dogs.txt"
else
	file="$1"
fi

if [ ! -f "texts/$file" ]; then
	echo "File texts/$file does not exists!"
	exit 1
fi

echo "$file" > file_name.txt

printf "Calculating TF-IDF for $file\n"
printf "Running TF mapreduce...\n"
printf "Removing old results...\n"
rm tf_output.txt -f
hadoop fs -rm -r /temp

printf "Putting files to HDFS...\n"
hadoop fs -mkdir /temp
hadoop fs -mkdir /temp/input
# /temp/output must not exists beforehand
hadoop fs -put texts/* /temp/input

printf "Counting files...\n"
hadoop fs -ls -R /temp/input | grep -E '^-' | wc -l > files_count.txt

printf "Running TF mapreduce on Hadoop...\n"
hadoop jar \
     /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar \
     -mapper "tf_mapper.py $file" \
     -reducer "tf_reducer.py $file" \
     -file tf_mapper.py \
     -file tf_reducer.py \
     -file utils.py \
     -input /temp/input/* \
     -output /temp/output

# printf "Getting results back...\n"
# hadoop fs -get "/temp/output/part-00000"
# mv "part-00000" tf_output.txt

# printf "Results are written to file tf_output.txt\nTF Done! Computing DF...\n"
# printf "Copying from HDFS /temp/output/part-* to /temp/dfinput...\n"
# hadoop fs -mkdir /temp/dfinput
# hadoop fs -cp /temp/output/part-* /temp/dfinput

printf "Running DF mapreduce on Hadoop...\n"
hadoop jar \
     /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar \
     -mapper "df_mapper.py $file" \
     -reducer "df_reducer.py $file" \
     -file df_mapper.py \
     -file df_reducer.py \
     -file utils.py \
     -input /temp/output/part-* \
     -output /temp/dfoutput

printf "Getting results into tf_df_output.txt...\n"
hadoop fs -get "/temp/dfoutput/part-00000"
mv "part-00000" tf_df_output.txt
