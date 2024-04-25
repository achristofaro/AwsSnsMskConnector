from kafka import KafkaProducer
import boto3
import json
import threading

# Configurações do Amazon SNS
sns_topic_arn = 'ARN_DO_TÓPICO_DO_AMAZON_SNS'
sns_region_name = 'REGIÃO_DO_AMAZON_SNS'
sns_client = boto3.client('sns', region_name=sns_region_name)

# Configurações do Amazon MSK
bootstrap_servers = ['ENDEREÇO_DO_BOOTSTRAP_SERVER_DO_AMAZON_MSK']
kafka_topic = 'NOME_DO_TÓPICO_DO_AMAZON_MSK'

# Configurações do produtor Kafka
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Número de threads para publicação no Kafka (parametrizável)
num_threads = 3


def subscribe_to_sns_topic():
    response = sns_client.subscribe(
        TopicArn=sns_topic_arn,
        Protocol='kafka',
        Endpoint=','.join(bootstrap_servers)
    )
    print("Subscription ARN:", response['SubscriptionArn'])


def receive_sns_messages():
    while True:
        response = sns_client.receive_message(
            TopicArn=sns_topic_arn,
            MaxNumberOfMessages=1
        )
        for message in response.get('Messages', []):
            sns_message = json.loads(message['Body'])
            kafka_message = {
                'message_id': message['MessageId'],
                'message_body': sns_message['Message']
            }
            publish_to_kafka(kafka_message)


def publish_to_kafka(message):
    producer.send(kafka_topic, value=message)
    producer.flush()
    print("Mensagem publicada no Kafka:", message)


def run_publishers():
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=receive_sns_messages)
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    subscribe_to_sns_topic()
    run_publishers()
