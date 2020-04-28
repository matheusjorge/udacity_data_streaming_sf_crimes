from kafka import KafkaConsumer

consumer = KafkaConsumer('com.udacity.spark.v1',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(message)