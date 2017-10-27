from pykafka import KafkaClient
from pykafka.common import OffsetType

import os
# export DOCKER_MAIN_IP=192.168.2.168
ip = os.environ['DOCKER_MAIN_IP']
print(ip)


# ip = "192.168.2.168:2182"
ip = "%s:2182"%os.environ['DOCKER_MAIN_IP']
client = KafkaClient(zookeeper_hosts=ip)
topic = client.topics[b'out']


consumer = topic.get_balanced_consumer(consumer_group=b'aha2',auto_commit_enable=True,zookeeper_connect=ip)
while True:
  for message in consumer:
    if message is not None:
      print("offset:%d , message: %s"%(message.offset, message.value))
  consumer.commit_offsets()