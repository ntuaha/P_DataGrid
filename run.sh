cd kafka
docker-compose up -d --scale kafka=3
cd ../docker-spark
docker-compose up -d
cd ../kafka_out
docker-compose up -d --scale kafka=3
cd ..
python3 producer.py 


# 啟動
# docker exec -it dockerspark_master_1 ./bin/spark-submit --jars /tmp/data/spark-streaming-kafka-0-8-assembly_2.11-2.2.0.jar /tmp/data/test.py 192.168.2.168:2181 test
# docker exec -it dockerspark_master_1 bash
# 更新所有子模組
# git submodule update --recursive --remote
