# Script for å demonstrere hvordan abstractmethod fungerer i kafka/message_processor.py

from typing import List
from abc import ABC, abstractmethod

# Mock class to simulate confluent_kafka.Message
class MockMessage:
    def __init__(self, topic: str, value: bytes, partition: int, offset: int, key: bytes = None):
        self._topic = topic
        self._value = value
        self._partition = partition
        self._offset = offset
        self._key = key

    def topic(self):
        return self._topic

    def value(self):
        return self._value

    def partition(self):
        return self._partition

    def offset(self):
        return self._offset

    def key(self):
        return self._key


# The abstract base class defines a consistent interface:
class MsgProcessor(ABC):
    @abstractmethod
    def __call__(self, msg: MockMessage) -> dict:
        pass

# Two different concrete implementations:
class TextMsgProcessor(MsgProcessor):
    def __call__(self, msg: MockMessage) -> dict:
        # Simple text-based processing
        return {
            "topic": msg.topic(),
            "data": msg.value().decode('utf-8'),
            "offset": msg.offset(),
        }

class AvroMsgProcessor(MsgProcessor):
    def __init__(self, key_deserializer, value_deserializer):
        self.key_deserializer = key_deserializer
        self.value_deserializer = value_deserializer

    def __call__(self, msg: MockMessage) -> dict:
        key = self.key_deserializer(msg.key(), None) if msg.key() else None
        value = self.value_deserializer(msg.value(), None)
        return {
            "topic": msg.topic(),
            "deserialized_key": key,
            "deserialized_value": value,
            "offset": msg.offset(),
        }

# A simple function that uses the processors:
def process_messages(messages: List[MockMessage], processor: MsgProcessor):
    """
    This function doesn't need to know what kind of processing happens inside
    the processor. It just calls it. Because the processor is guaranteed
    to implement __call__, we can rely on it returning a dictionary.
    """
    results = []
    for msg in messages:
        processed = processor(msg)  # Same interface for any processor!
        results.append(processed)
    return results

# Example usage:
fake_messages = [
    MockMessage(topic="text_topic", value=b"hello world", partition=0, offset=100),
    MockMessage(topic="avro_topic", value=b"\x00\x01...", partition=1, offset=200),
]

# We can easily switch out processors:
text_processor = TextMsgProcessor()
avro_processor = AvroMsgProcessor(
    key_deserializer=lambda k, ctx: "deserialized_key",
    value_deserializer=lambda v, ctx: {"foo": "bar"},
)

# Using the text processor
text_results = process_messages(fake_messages, text_processor)
print("Text Results:", text_results)

# Using the Avro processor on the same messages:
avro_results = process_messages(fake_messages, avro_processor)
print("Avro Results:", avro_results)
