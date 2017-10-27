from flask import Flask, Response
from pykafka import KafkaClient
from pykafka.common import OffsetType

ip = "127.0.0.1:9092"
client = KafkaClient(hosts=ip)
topic = client.topics[b'test']

consumer = topic.get_balanced_consumer(consumer_group=b'aha3',auto_commit_enable=True,zookeeper_connect='localhost:2181')


app = Flask(__name__)
#https://zhuanlan.zhihu.com/p/27401175
@app.route('/1234')
def index():
    # return a multipart response
    return Response(kafkastream(),mimetype='text/txt')

def kafkastream():
    while True:
      for message in consumer:
        if message is not None:
          yield (str.encode('%d,%s\n'%(message.offset,message.value)))
      consumer.commit_offsets()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



# https://www.ibm.com/developerworks/cn/opensource/os-cn-spark-practice2/index.html