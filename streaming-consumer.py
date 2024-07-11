from google.cloud import pubsub_v1
import time

subscription = 'projects/gcp-dataflow-beam/subscriptions/MeusVoos-sub'
subscriber = pubsub_v1.SubscriberClient()

def mostrar_msg(mensagem):
    print((f'Mensagem: {mensagem}'))
    mensagem.ack()

subscriber.subscribe(subscription, callback=mostrar_msg)

while True:
    time.sleep(3)