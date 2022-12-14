# DataStax 2022-2023 Capstone

Welcome to the 2022-2023 Capstone project. Here, you will find all
the basic details you need to build a working example of sentiment
analysis with Astra DB and Astra Streaming.

Developed by Jonathan Shook, Derrick Cosmas, Justin Eldridge, DataStax team

## Weekly Discussion and  Office Hours

Discussions and office hours will be conducted online via zoom. The schedule are as follows:
* Discussions: **Thursdays 12:30PM - 1:30PM** via [Zoom]()
* Office hours: **Thursdays 1:30PM - 2:00PM** via [Zoom]()

If you'd like to schedule another time to meet, feel free to send either one of us an email. 

## Teaching Staff

* Jonathan Shook - jshook@datastax.com
* Derrick Cosmas - derrick.cosmas@datastax.com
* Justin Eldrdige - jeldridge@ucsd.edu

## Resources

### Papers

* Main paper to replicate: [Employee Sentiment Analysis Towards Remote Work during COVID-19 Using
Twitter Data](https://inass.org/wp-content/uploads/2021/12/2022022808.pdf)
* [Sentiment Analysis Based on Deep Learning: A Comparative Study](https://arxiv.org/ftp/arxiv/papers/2006/2006.03541.pdf)
* [Recent Papers on Sentiment Analysis](https://www.paperdigest.org/2020/05/recent-papers-on-sentiment-analysis/)

### Tools

* Machine Learning Tools: [Huging Face](https://huggingface.co/docs/transformers/index)
* Visualization samples: [Observable (samples of D3.js)](https://observablehq.com/explore)
* Twitter API in POSTMAN: [POSTMAN Twitter API Samples](https://t.co/twitter-api-postman)
* HTTP requests in Python: [Python Request Library](https://realpython.com/python-requests/#the-get-request)
* Feature Store: [Feast](https://feast.dev/blog/what-is-a-feature-store/)

## Quarter 1 Requirement

For Quarter 1 you are replicating [Employee Sentiment Analysis Towards Remote Work during COVID-19 Using
Twitter Data](https://inass.org/wp-content/uploads/2021/12/2022022808.pdf) 

While you can take various creative liberties with the project, essential **requirements** for the Quarter 1 paper replication are specifically:

* Project objective is framed around remote work within the context of Covid-19.
* Demonstrate the sentiment analysis methods described in the research paper. You can use a sentiment analysis model from HuggingFace
* Your results must answer your defined objective, i.e. what is the sentiment of the population you are analyzing towards remote work within your own Covid-19 context.
* Use the Twitter API for your raw input stream.
* Use a streaming function for your classification pipeline.

What is OPTIONAL for Quarter 1:
* Training or modifying a baseline sentiment analysis model to improve accuracy or results

Quarter 1 Checkpoint which consists of a Working Title, Abstract and Introduction should drive the content of your replication and report.

### Quarter 1 Project Submission

Due to the streaming nature of our project, **code** submission criteria for DataStax industry capstone are different than what is outlined in DSC 180 course website. Your submission will be a code repo containing:

1. Minimum of 3 Python files code: message producer, pulsar function and the ML classifier as consumer.

2. README.
   * Should contain requirements and how the code pieces fit together as a pipeline.
   * Recommended to put a diagram of your architecture design.

3. Video recording of end to end sentiment analysis demonstration using Astra Streaming. 
   * Explain how the machineries are set up and working as a pipeline. 
   * Overall, demonstrate to the audience how your code are generating results.
   * Recording should only be 10 to 20 minutes.

For the **report** there are some cosiderations to guide your writing:
 
1. Report should follow similar format of the replication paper. 
2. Results of your work must answer the initial question or hypothesis outlined in the preamble / problem statement.
3. Double column format common in reserach publications are allowed.
4. Approximately 4 to 8 pages long.

## Quarter 2 Requirement and Proposal

For Quarter 2, your project is more open ended than quarter 1. The objective topic is no longer limited to remote work and sentiment analysis.

While you can continue with the same topic frame regarding remote work sentiment inside the context of Covid-19, we encouraged you to be more creative and explore other topics of interest.

What is required for Quarter 2 Project:

- Demonstrate the use of Astra Streaming features (producer, consumer and functions) as the tools to stream data within your pipeline

We encouraged you to integrate more features to your project such as:

- Hosting your visualization results on a website 
- Collecting data streams to a feature store / database

With quarter 2 project potentially larger in scope and requirements, you can utilize some code of what you have already built such as:

- Tweets / message producer (Project do not have to involve analyzing tweets)
- NLP preprocessing i.e. discarding irrelevant inputs, tokenizing, lemmatizing

It will be beneficial for you to submit a thorough Quarter 2 proposal so that the teaching staff can provide timely and constructive feedback.

## Introduction

Hello students! Welcome to industry Capstone with DataStax. Your Data Science Capstone industry mentors for the next two terms will be Derrick Cosmas and Jonathan Shook, both from DataStax. We will also have Justin Eldrdige from UCSD to assist during discussion and office hours.

The project will focus on using Machine Learning to do sentiment analysis on the Twitter firehose. A good paper for background is [Sentiment Analysis Based on Deep Learning: A Comparative Study](https://arxiv.org/ftp/arxiv/papers/2006/2006.03541.pdf).

This capstone program is designed to mentor you, the students in building real world projects. We expect you to to drive the direction of your own project and excellence will come from the planning and execution you put into the project. 

The best way for the staffs to help you succeed will be by answering your questions during discussion and office hours. These questions should be regarding blockers that you might encounter throughout all phases of the project. Having those questions answered should give you the clarity to move your project forward throughout the quarters. Come prepared with questions for every session as they are designed to help you, rather than the staffs.

## Section Participation

Participation in the weekly discussion section is *mandatory*. Each
week, you are responsible for doing the reading/task assigned in the
schedule. Come to section prepared to ask questions about
and discuss the results of these tasks. Think of these questions as problems 
you need help with in moving your project forward.

Each week, turn in answers to the weekly questions to Canvas. These
questions are meant to focus your work for the week and help prepare
you for discussion. If you have questions about your work, please ask
them in section or office hours (We will rarely comment on your
submission).

You are responsible for the entire weekly reading/task, even if
portions are not covered in the weekly questions. The weekly tasks are
the building blocks for the project proposals/assignments due at the
end of the quarter.

## Schedule

**No participation questions are required to be completed before Week 1. 
First set of Participation Questions are due on Week 2**

|Week|Topic|
|--|--|
|1|[Introduction]({{ "weeks/01-Introduction" | absolute_url }})|
|2|[Streaming]({{ "/weeks/02-Streaming" | absolute_url }})|
|3|[Twitter Firehose ]({{ "/weeks/03-Firehose" | absolute_url }})|
|4|[Streaming Demo Pt 2 ]({{ "/weeks/04-Streaming-Demo" | absolute_url }})|
|5|[Structured Data ]({{ "/weeks/05-Structured-Data" | absolute_url }})|
|6|[Scaling ]({{ "/weeks/06-Scaling" | absolute_url }})|
|7|[Integration Check ]({{ "/weeks/07-Progress-1" | absolute_url }})|
|8|[Iteration and Integration]({{ "/weeks/08-Iteration" | absolute_url }})|
|9|Thanksgiving Break - No Class|
|10|[Last Working Session]({{ "/weeks/10-Work-Session" | absolute_url}})|
