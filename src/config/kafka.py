import os

# endereço_do_bootstrap_server_do_amazon_msk
BOOTSTRAP_SERVERS = os.environ.get('BOOTSTRAP_SERVERS')
# nome_do_tópico_do_amazon_msk
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')
