from pykafka import KafkaClient
from flask import Flask
from flask import request
from flask import jsonify
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
import os
# export DOCKER_MAIN_IP=192.168.2.168
ip = os.environ['DOCKER_MAIN_IP']
print(ip)

<<<<<<< HEAD
import os

# ip = "192.168.2.168:2181"
ip = "%s:2181"%os.environ['DOCKER_MAIN_IP']
print(ip)
=======
ip = "%s:2181"%ip
>>>>>>> bf86dfc2855a3fd073c134834672871707b0126e
client = KafkaClient(zookeeper_hosts=ip)
topic = client.topics[b'in']
producer = topic.get_producer()
producer.start()



@app.route('/')
def hello():
    return "HI! This is RMS System"

@app.route('/collect',methods=['POST'])
def collect():        
    producer.produce(request.data)    
    res = jsonify(json.loads(request.data.decode('utf8')))
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    return res





if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=6003)