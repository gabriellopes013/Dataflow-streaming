from google.cloud import pubsub_v1
import time

topico = 'projects/gcp-dataflow-beam/topics/MeusVoos'
publisher = pubsub_v1.PublisherClient()

entrada = r'/Users/gabrielalmeida/Desktop/Dataflow-streaming/voos_sample.csv'

with open(entrada,'rb') as file:
    for row in file:
        print('Publicando o topico')
        publisher.publish(topico,row)
        time.sleep(2)

