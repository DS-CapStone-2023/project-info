# Week 3 - Twitter Firehose

## Topics

This week we will be setting up basic functions for Astra Streaming
* get set up with [Astra streaming](https://astra.datastax.com/registerStreaming)

## Tasks

Please read the following requierement up your basic functions in Astra Streaming:

### Requirement:
- Able to start a python virtual environment with the latest Pulsar Python Client 2.10.1 following this [tutorial]{https://pulsar.apache.org/docs/client-libraries-python/#install}

|Platform |Supported Python Versions|
|-|-|
|MacOS 10.13 (High Sierra), 10.14 (Mojave) | 2.7, 3.7, 3.8, 3.9|
|Linux|	2.7, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9|

### Setting up python environment:
1. Get the code from our [repository]{https://github.com/ucsd-capstone-datastax/prototypes}  
  
  ```
  $ gh repo clone DS-CapStone-2023/project-info
  ```

2. Go to start-stream-py

  ```
  $ cd project-info/start-stream-py
  ```

3. Create your python virtual environment here

  ```
  $ python3.9 virtualenv <env_name>
  ```

4. Activate your newly created environment

  ```
  $ source <env_name>/bin/activate
  ```

5. If you have not installed Pulsar Python client, you should do so in your virtualenv.  
  
  * From requirements.txt:  
  ```
  $ pip install pulsar-client==2.10.1  
  ```

### Instructions:

https://docs.google.com/document/d/1VS31dXTIAmEkIh9o_9FcAhD-rVvcmnTo_Zm1zSMgCmY/edit


## Discussion Questions

Participation questions are due 24 hours before next week discussion meeting.  

Project Proposal are due on Week 5 so I would like to get a sense of how far you are on the reading. 

With respect to our **main paper**, answer the following questions:
* Describe one thing you found interesting in the reading. Describe what it is in your own words and why you found it interesting.
* Describe one thing that you found difficult to understand. Try to be specific about what you don’t think you understand.
* In preparation for your Week 5 proposal, describe and justify in detail, the context and objective of your prediction regarding remote work sentiment. Some of the questions to help structure your answer:
  * What are your sentiment labels (happy, unhappy, mixed, neutral, strong dislike, etc) and why do you decide to use these labels
  * How would you label your dataset using the labels above ? 
  * How would you construct your training dataset ?
  * How would you measure accuracy of your model ?
  * Can you think of the biases you are introducing to your dataset and prediction model ? (demographics, keywords)
