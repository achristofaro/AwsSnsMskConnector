#!/bin/bash -i

aws kafka create-connector \
    --cluster-arn ARN_DO_CLUSTER_MSK \
    --connector-name custom-connector \
    --current-version '{
        "name": "custom-connector",
        "config": {
            "connector.class": "com.example.CustomConnector",
            "tasks.max": "3",
            "key.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
            "value.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
            "topics": "sns-topic",
            "sns.topic.arn": "ARN_DO_TÓPICO_DO_AMAZON_SNS",
            "sns.region.name": "REGIÃO_DO_AMAZON_SNS",
            "bootstrap.servers": "ENDEREÇO_DO_BOOTSTRAP_SERVER_DO_AMAZON_MSK",
            "kafka.topic": "NOME_DO_TÓPICO_DO_AMAZON_MSK",
            "s3.bucket": "NOME_DO_BUCKET_S3",
            "s3.key": "CAMINHO_PARA_O_ARQUIVO_ZIP_NO_BUCKET_S3",
            "batch.size": "16384",
            "max.poll.records": "1000",
            "max.partition.fetch.bytes": "1048576",
            "retry.backoff.ms": "500",
            "request.timeout.ms": "30000",
            "security.protocol": "SSL",
            "ssl.truststore.location": "/path/to/truststore.jks",
            "ssl.truststore.password": "truststore_password",
            "ssl.keystore.location": "/path/to/keystore.jks",
            "ssl.keystore.password": "keystore_password",
            "ssl.key.password": "key_password",
            "ssl.endpoint.identification.algorithm": "https",
            "ssl.protocol": "TLSv1.2",
            "ssl.enabled.protocols": "TLSv1.2",
            "ssl.truststore.type": "JKS",
            "ssl.keystore.type": "JKS",
            "vpc": "ID_DA_VPC",
            "securityGroups": "ID_DO_GRUPO_DE_SEGURANÇA_1,ID_DO_GRUPO_DE_SEGURANÇA_2",
            "subnets": "ID_DA_SUBNET_1,ID_DA_SUBNET_2"
        }
    }'
