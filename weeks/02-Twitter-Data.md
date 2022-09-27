# Week 2 - Twitter Firehose

## Topics

This week, we'll be introduced to the paper and prepare to collect a Twitter dataset. We'll:

* get set up to download data from the [Twitter API](https://developer.twitter.com/en/apply-for-access);
* get set up with [Astra streaming](https://astra.datastax.com/registerStreaming)
* start reading the paper that we'll base our work in.

## Readings

Please read the following before our next meeting:

* Read the paper we are replicating [Employee Sentiment Analysis Towards Remote Work during COVID-19 Using
Twitter Data](https://inass.org/wp-content/uploads/2021/12/2022022808.pdf)

* To use the Twitter API, you must be approved for developer access. Read the instructions [here](https://developer.twitter.com/en/apply-for-access) and apply for a single-user developer key.
You will be asked several questions about how you will use the API; 
the approval process is done by humans, so the quality of your answers is very important. 
Here are some tips:
    * Outline what information you are trying to learn from using the API - remote work sentiment during covid-19  
    * Use your UCSD email -- this gives your request more credibility.
    * Mention that this is for a class, DSC 180, at UC San Diego. You can include my name as well.
    * Twitter may send a follow-up email asking for more information. You can reply by paraphrasing the below:
       * The core use case is academic research in social network dynamics. 
         We will be studying sentiment towards remote work during covid 19. This will be part of a senior capstone project at UC San Diego.
         We will analyze the content of tweets only to determine how URLs/hashtags are being shared. We will not be analyzing individual users as such. 
         We will not be posting, retweeting, or otherwise interacting with other user accounts. Our use of the API will be strictly read-only.
         Twitter content itself will not be displayed off twitter. 
         Aggregated information about the dynamics of twitter conversation will be displayed in academic venues only.

* Read about the [Twitter API's restricted use cases](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases)

## Discussion Questions

Participation questions are due 24 hours before next week discussion meeting.  

Answer the following questions for this week (2-3 sentences each task):
  * What is the primary trade-off between real-time and batch modes?
  * When would you opt for real-time, or event-driven processing?
  * When would you use streams vs queries to a data store?


