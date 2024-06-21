# Copyright (c) Qotto, 2024

from __future__ import annotations

import base64
import json
import logging

from time import sleep

import requests

from eventy.messaging.errors import MessagingError
from eventy.messaging.store import Cursor, RecordStore
from eventy.record import Record
from eventy.serialization import RecordSerializer

__all__ = [
    'Http2KafkaStore',
]


logger = logging.getLogger(__name__)


# HTTP2KafkaStore is based on RecordStore. It implements a class to send events to the service http2kafka and save them permanantly.
# The useful implemented function is
# write(self, record: Record, topic: str, timeout_ms=None)
#
#
# Functions not meant to be used by a user of Http2Kafka:
# Some other functions are also implemented because called on by the eventy app _record_store, and not implemented by RecordStore
# but useless in the case of Http2KafkaStore
# So they are still implemented to not raise NotImplemented error, but empty.
#
# Here are these empty functions:
# write_now() is called by _AppRecordWriteStore.write(), not implemented by RecordStore
# register_topic() is called by EventyApp._initialize()
# write() is called by EventyApp._process_one_record_one_handler()
#
# Not implemented by Http2Kafka functions (Might be used by EventyApp if Guarantee.EXACTLY_ONCE is used):
# start_transaction()
# ack()
# commit()


class Http2KafkaStore(RecordStore):
    """
    Http implementation of a record store, using Http2Kafka
    """

    def __init__(
        self,
        serializer: RecordSerializer,
        api_server: str,
        initial_retry_delay: int = 1,
        max_retries: int = 30,
        retry_factor: float = 1.5
    ) -> None:
        """
        Create a new Http2Kafka record store.

        :param RecordSerializer serializer: Record serializer (read and write)
        :param str api_server: Http2Kafka api servers
        :param initial_retry_delay: The initial waiting time between the first faied http requets and the second one.
        :param max_retries: The maximum number of retries to send a http request to http2kafka. The write function fails if max_retries is exceeded.
        :param retry_factor: The factor by which the waiting time is multiplied by between two retries.
        """
        # Initialize topics to register
        super().__init__()
        # Kafka config
        self.serializer = serializer
        self.api_server = api_server
        # Retry mechanism config
        self.initial_delay = initial_retry_delay  # In seconds
        self.max_retries = max_retries
        self.retry_factor = retry_factor

        logger.info("Http2Kafka_Store initialized with api server:" + self.api_server)

    def register_topic(self, topic: str, cursor: Cursor = Cursor.ACKNOWLEDGED):
        """
        Inherited from CKStore, but no need for Http2KafkaStore.
        """
        return

    def write(self, record: Record, topic: str, timeout_ms=None) -> None:
        """
        Write a record to http2kafka by sending an HTTP request.
        The record is first avro serialized and then encoded as a base64 string before being sent to Http2Kafka
        If the http request is not successful, the function will retry sending it until max_retries is reached, in which case it will raise a MessagingError.

        :raise MessagingError if the record is not stored by http2kafka after max_retries requests
        :param record: can be an event, or any other record.
        :param topic: the topic to store the record in.
        """
        serialized_event = self.serializer.encode(record)
        base64_event = base64.b64encode(serialized_event).decode('utf-8')
        json_data = json.dumps({'data': base64_event})

        # Logs
        url = f'{self.api_server}/api/v1/{topic}'
        header = {'Content-Type': 'application/json'}
        logger.info(f"Sending event data to http2kafka on URL: {url}")
        logger.info(f"Event data: {json_data}")

        # Send Http Request. Retry max_retries times before raising exception
        delay: float = self.initial_delay
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.post(url, data=json_data, headers=header)
                logger.info(f"Http2Kafka service response: {response.text}")

                if response.status_code == 200:
                    logger.info("Request successful! Event stored")
                    return
                else:
                    logger.info(f"Request failed with status code:{response.status_code}")
                    raise MessagingError(f"Max number of requests failed. Http request status code:{response.status_code}")
            except (requests.exceptions.ConnectionError, MessagingError):
                # Check if we retry or raise exception
                if retries == self.max_retries - 1:
                    print(f"Maximum retries ({self.max_retries}) exceeded. Giving up.")
                    raise MessagingError(f"Http2kafka service is unreachable.")
                else:
                    print(f"Retry {retries + 1}/{self.max_retries} failed. Retrying in {round(delay, 2)} seconds...")
                    sleep(delay)
                    delay *= self.retry_factor

                retries += 1

    def write_now(self, record: Record, topic: str, timeout_ms=None) -> None:
        """ Calls write() function """

        self.write(record, topic, timeout_ms)

    def start_transaction(self) -> None:
        """
        This function is implemented because EventApp uses it,
        however in the case of a Http2KafkaStore, it is useless.
        """
        logger.error("Transactions not handled with Http2Kafka")
        raise NotImplementedError

    def ack(self, timeout_ms=None) -> None:
        """
        This function is implemented because EventApp uses it,
        however in the case of a Http2KafkaStore, it is useless.
        """
        logger.error("Ack not handled with Http2Kafka")
        raise NotImplementedError

    def commit(self, timeout_ms=None) -> None:
        """
        This function is implemented because EventApp uses it,
        however in the case of a Http2KafkaStore, it is useless.
        """
        logger.error("Commit not handled with Http2Kafka")
        raise NotImplementedError

    def __del__(self):
        if self.initialized:
            logger.info(f"Waiting poll thread to join.")
            self.cancelled = True
            logger.info(f"Poll thread joined.")
