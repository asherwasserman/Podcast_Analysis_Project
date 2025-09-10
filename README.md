The system is divided into three parts.

One part is the publisher, which receives a path to the folder where audio files are stored. To begin processing, the files are transferred to a container where the subscriber will pick them up.

The second part is the subscriber that takes the information from the Kafka topic, extracts the metadata, and publishes it in Elasticsearch to enable quick searching for file details. The file content itself is stored in MongoDB.

The third part is data processing, extracting the text from the audio segment and classifying the information to obtain necessary information about which files should be processed first and which ones are more dangerous.

The reason why text transcription and processing are done separately, is due to the complexity of the processing and the time it takes. It is better to separate it and have all the files stored in the database first and the metadata stored in elasticsearch.

The method for calculating the danger percentage is, the percentage of the most dangerous words in relation to the entire text, and half the percentage of the less dangerous words in relation to the entire text. The reason is that not every text is equal in length, and if the text is longer, then in order to have the same level of danger, it must contain dangerous words with the same frequency.

The threshold for calculating whether the text, is not at all dangerous takes into account the project's goal of saving resources, due to a lack of resources and, on the other hand, the need not to miss dangerous texts. The threshold set is 5%.

The threshold set for the definition of "extremely dangerous" is 20%, a relatively high threshold due to the presence of many link words, in order to prioritize very high-level dangerous texts.
