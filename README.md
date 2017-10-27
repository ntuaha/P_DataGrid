# RMS_DATA_GRID
資料搜集

## 設定本機IP
```
export DOCKER_MAIN_IP=[填入本機IP]
```



## 啟動資料源的Kafka
```
cd kafka
docker-compose up -d  --scale kafka=3
```

## 輸出資料源的Kafka
```
cd kafka_out
docker-compose up -d  --scale kafka=3
```

## Start Spark 
```
cd docker-spark
docker-compose up -d
```

## Start Spark Structure Streaming
```
docker exec -it dockerspark_master_1 ./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.0 /tmp/data/test3.py $DOCKER_MAIN_IP
```

## Start comsumer
建議在另外一個termial開啟
```
cd [專案目錄]
python3 comsumer.py
```


## Start producer
```
cd [專案目錄]
python3 producer.py
```

## 傳送資料
```
curl -X POST \
  http://localhost:6003/collect \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 73920c24-879a-a845-f75b-2144f967739e' \
  -d '{"123":345}'
```  


## 終止服務
```
docker rm -f $(docker ps -a -q)
```

