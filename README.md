I added a class called metadata to get metadata from a file path
I added a manager that will build json for each file in a folder using the metadata class and send the data to kafka
I added a folder called kafka inside which I added a captive producer class to publish data to kafka
I ran a local Kafka container to receive the information.