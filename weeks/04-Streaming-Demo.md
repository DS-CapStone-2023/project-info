# Week 4 - Streaming Demo Pt. 2

## Quarter 1 Project Checkpoint

Checkpoint is due on **October 30th**.  

Submit a working title, abstract, and introduction for their Quarter 1 Project, which is a replication of our main paper.

While you can take various creative liberties with the project, essential **requirements** for the replication are specifically:

1. Project objective is framed around remote work within context of Covid-19.
2. Demonstrate the sentiment analysis methods described in the research paper.
3. Use the Twitter API for your raw input stream.
4. Use a streaming function for your classification pipeline.


## Topics

This week we will be continuing the demo from where we left off setting up authentication as environment variables

## Tasks

Please read the following requirement to set up your basic functions in Astra Streaming:

### Requirement:
- Created a python virtual environment with the latest Pulsar Python Client 2.10.1 following this [tutorial](https://pulsar.apache.org/docs/client-libraries-python/#install)

|Platform |Supported Python Versions|
|-|-|
|MacOS 10.13 (High Sierra), 10.14 (Mojave) | 2.7, 3.7, 3.8, 3.9|
|Linux|	2.7, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9|

- Imported Astra streaming authentication as environment variables in your shell system

### Instructions:

[Google Docs](https://docs.google.com/document/d/1VS31dXTIAmEkIh9o_9FcAhD-rVvcmnTo_Zm1zSMgCmY/edit)


## Discussion Questions

Participation questions are due 24 hours before next week discussion meeting.  

Quarter 1 Project checkpoint are due on Week 5, specifically October 30th. I want to encourage you to start thinking more of your project via the following questions.

Describe in detail:

1. How do you plan to use the twitter API? What endpoints and request method will you be using ? 
2. What type of filtering do you think is appropriate for your API requests? What header labels will you be using ?
3. Are you planning on doing any model training? If so, what methods will you be using to create your labeled dataset?

## Homework

You do not have to submit this at Gradescope, but you should attempt doing these items to get started on your project:

1. Start consuming data from the twitter API and see hook it up the feed into a Pulsar streaming topic via a Python script or some other methods.
2. Start sketching out your classification (or training) pipelines. Document this in a way that can be useful for your proposal. Visual narratives are powerful and should be part of any good presentation. Clarity around active processing elements, data flows, and key responsibilities is crucial.

When designing and coding your solution, always keep in mind the **4 project requirements** outlined above:

1. Project objective is framed around remote work within context of Covid-19.
2. Demonstrate the sentiment analysis methods described in the research paper.
3. Use the Twitter API for your raw input stream.
4. Use a streaming function for your classification pipeline.
