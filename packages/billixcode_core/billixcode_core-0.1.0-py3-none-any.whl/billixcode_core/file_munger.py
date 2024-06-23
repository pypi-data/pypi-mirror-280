import os

from elastic_operations import ElasticOperations
from eventdriven_repository import EventDrivenRepository
from file_handler import FileDataExtractor
from kafka_message_producer import KafkaEventProducer


class FileMunger(EventDrivenRepository):

    def __init__(self, directory, file_handler, elastic_operations, kafka_message_producer):
        super().__init__(db_ops=elastic_operations, message_producer=kafka_message_producer)
        self.directory = directory
        self.file_handler = file_handler

    def traverse_directory(self):

        for root, dirs, files in os.walk(self.directory):

            for file in files:
                file_path = os.path.join(root, file)
                file_details = self.file_handler.extract_text_payload(file, file_path)
                if file_details['payload']['type'] == 'unknown':
                    print(f'skipping : {file_path}')
                else:
                    print(f'sending to elastic: {file_path}')
                    self.upsert(index_name='docs', doc_id=file_details['hash'], document=file_details['payload'])


if __name__ == '__main__':
    munger = FileMunger("/Users/robertschneider/Desktop/",
                        FileDataExtractor(),
                        ElasticOperations('https://192.168.1.158:9200/', 'elastic', '7dlixaFgAj8LYA3xsV65'),
                        KafkaEventProducer(topic='files'))
    munger.traverse_directory()
