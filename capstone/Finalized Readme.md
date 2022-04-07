# Using NLP to detect COVID-19 anti-vaccine tweets on Twitter

### Introduction & Problem Statement  
- The introduction of COVID-19 vaccines provided a glimmer of hope and a pathway to recovery. However, owing to misinformation being spread on social media and other platforms, there has been a rise in vaccine hesitancy which can lead to a negative impact on vaccine uptake in the population.

The World Health Organization said anti-vaccine views were a "top 10 global health threat" in 2019.

- Twitter has employed us with the goal of
  - A) Evaluating the performance of different natural language processing models to identify anti-vaccination tweets that were published during the COVID-19 pandemic
  - B)  Deriving a minimum viable product by use of the most effective machine learning model to create a preliminary vaccine misinformation detection framework
  - C) identify and analyse key barriers to vaccine uptake



### Dataset
- Check the frequency of retweets?
Texts were changed to lowercase. Twitter handles, URLs, hyphens, hashtags (with attached words), numbers, and special characters were removed. A list of English stop words
(e.g., is, that, has, a, do, etc.) from the NLTK library (https://www.nltk.org, accessed on 10
April 2021) were used to remove stop words from the tweets (negations including “not”
and “no” were not removed given the purpose was to identify anti-vaccination tweets).
Lemmatization, a process of generating the canonical form of a word, was implemented
for words in all tweets.
Tweets with no content after being processed were removed.
A total of 1,474,276 remained.
A systematic random sampling method was used to select 20,854 tweets from 1,474,276
tweets for labeling. This sampling method ensures that tweets across the different times
during the pandemic were selected.

### Procedure

1. The sentiments of people regarding vaccines of all sorts were assessed using the natural language processing (NLP) tool, Valence Aware Dictionary for sEntiment Reasoner (VADER).
2.  In addition, we included our analysis of the timeline of the tweets in this research, as sentiments fluctuated over time.
3. A recurrent neural network- (RNN-) oriented architecture, including long short-term memory (LSTM) and bidirectional LSTM (Bi-LSTM), was used to assess the performance of the predictive models,

### Reference
- Hayawi, Kadhim & Shahriar, Sakib & Serhani, Mohamed & Taleb, Ikbal & Mathew, Sujith. (2021). ANTi-Vax: a novel Twitter dataset for COVID-19 vaccine misinformation detection. Public Health. 203. 10.1016/j.puhe.2021.11.022.
- Documenting the Now. (2020). Hydrator [Computer Software]. Retrieved from https://github.com/docnow/hydrator



### Q&A (Questions I had during the process)
