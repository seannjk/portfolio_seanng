# PROJECT 3
This is the finalized readme file for Project 3.

# Problem Statement
Reddit is a massive collection of forums where people can share social news and content. Essentially, posts are organised according to subject into user-created 'subreddits'. Members submit content (such as images, texts, and links) to subreddits, which can then be voted up ('upvote') or down ('downvote') by other members.

Since the COVID-19 pandemic in 2019, many news reports reveal that there has been a rapidly growing interest in pet ownership.
More people have expressed interest in adopting or fostering dogs and cats for various reasons - such as for companionship during circuit breaker or ease of caring for pets due to work-from-home arrangements.

Introducing “CatDog” - a startup in the Pet Industry created in response to the growing interest in pet ownership. CatDog has outsourced us data scientists to adopt a low-cost strategy to 1) examine the topics of interest/needs of new dog and cat owners and 2) provide relevant suggestions on creating new services for dog and cat owners. Given cost restraints, the goal of our team of data scientists is to conduct a needs analysis of dog & cat redditors by looking at relevant subreddits. We can use the information gained to inform CatDog on possible services/business ideas to develop on. Our team aims to engineer three supervised classification models - namely the Ensemble-based learning algorithm Random Forest Classifier, Naive Bayes Classifier and Logistics Regression Classifier - and to select one model that best predicts the classification of the subreddit for current and future posts submitted by either dog or cat owners. Our team will select the best model based on the initial accuracy score (which tells us its predictive power) of all three models on the test set, and look at the most important word features for that particular model to suggest business ideas for CatDog to create in order to meet the needs of cat and dog owners. The two subreddits are:
- [r/Cats](https://www.reddit.com/r/cats/)
- [r/Dogs](https://www.reddit.com/r/dogs/)

# Executive Summary
The following sections are supported by the respective numbered Jupyter Notebooks.

### 1. API/Webscrapping
- The data used to train and test our model sets comes from Reddit's API, which returns .json dictionaries for data requests. We iterated through and aimed to collect about 10000 posts from each subreddit. However, we obtained 9997 recent posts from r/Cats and 9996 from r/Dogs. These were parsed into post and title content and saved to CSV using a Pandas DataFrame.


### 2. EDA & Pre-Processing Part 1
- A new column, 'clean_title' was created. This column comprised the titles that underwent exploratory data analysis (EDA). These EDA steps included removing null values and tokenizing using Regex to remove punctuation, url components, languages that are not interpretable, emojis and numbers. Additional columns, such as the number of unique words, number of stopwords and number of punctuations, were engineered to understand the initial titles. Initial pre-processing include stemming and lemmatizing as well.
Finally, a new dataframe CSV was created by dropping all columns and leaving only the 'subreddit' and "clean_title" columns.


#### My Data Dictionary
All subreddit titles are collected from Reddit's API. Posts are combined into a single dataframe (DF) and titles are cleaned and reflected as 'clean_title'.  The subreddit has been changed to values 1 (for dogs) and 0 (for cats). The original dataframe created in part 2 of notebook was dropped.

|Columns|Type|Description|
|---|---|---|
|Subreddit|Int64|Subreddit Dogs labelled as '1', Subreddit Cats labelled as '0'|
|Clean_Title|object|Cleaned Data/words from original titles|


### 3. Text Processing Part 2 & Model Selection/Modelling & Optimization
- Pre-processing include vectorizing with Count Vectorizer and TF-IDF (Term Frequency-Inverse Document Frequency) to enhance modeling response. We divide our data into a Train and Test vector to begin modeling. Using a GridSearchCV hyperparameter optimization, we selected 3 models to build and examine: Multinomial Naive-Bayes classifier, Random Forest classifier & Logistic Regression each with CountVectorizer and TFIDF Vectorizer as estimators. I adopted a trial and error method to manually optimize our hyperparameters, and used a Pipeline to batch our pre-processing and model fitting into a single process, which GridSearch can iterate through. Our optimized settings for each model are built into our final models.

#### Model Selection
- In this dataset, I tested a few linear regression models. Below are some of results of the models evaluated on the final data set. Additional details can be found in the project notebook model evaluation.

|Models Used|Estimator|Best Score(Accuracy)|Pipeline Built|Hyperparameter Optimization|Remarks|
|---|---|---|---|---|---|
|Random Forest Classifier|CountVectorizer|0.8956|Yes|Yes, using GridSearch|NA|
|Random Forest Classifier|TFIDFVectorizer|0.8958|Yes|Yes, using GridSearch|NA|
|Naive Bayes Classifier|CountVectorizer|0.8962|Yes|Yes, using GridSearch|NA|
|Naive Bayes Classifier|TFIDFVectorizer|0.8865|Yes|Yes, using GridSearch|NA|
|Logistic Regression|CountVectorizer|0.8947|Yes|Yes,using GridSearch|NA|
|Logistic Regression |TFIDFVectorizer|0.8971|Yes|Yes, using GridSearch|NA|
|Baseline|Nil|0.4987|No|No|NA

- Generally, all models outperformed the baseline (~49.8%) when fitted on test sets.
- When fitted on the test sets, logistic regression with TFIDF Vectorizer received the highest accuracy rating overall of models run, with an accuracy score of ~89.7%. This is followed by Naive Bayes with a CountVectorizer and Random Forest with a TFIDF Vectorizer at ~89.6%
- We will evaluate the model Logistic Regression with TFIDF Vectorizer as it gives the best accuracy score based on testing data.
- Logistic Regression could have outperformed other nonlinear models (e.g. Ensemble-based learning algorithms such as Random Forest) given it's simplicity and interoperability, as well as it being used on a large sample set.

### 4. Model Evaluation
- Logistic Regression with TFIDF Vectorizer shows a training accuracy of ~91.2% and testing accuracy of ~90.5%
- I also generated the top 20 coefficients for each subreddit.

| Cats    | Dogs   |
|------------|-------------|
| <img src="https://github.com/seannjk/ga_projects/blob/790145a435261f31d0c2eedb1618b11cccaa0026/project_3/Images/cats%20coeff.png"> | <img src="https://github.com/seannjk/ga_projects/blob/7bfd5fb2d196175a914e88748efbba8e37df9f82/project_3/Images/dogs%20coeff.png"> |

- While we created a confusion matrix, the goal of our problem statement is mainly to predict the top word features to inform business recommendations. Regardless, our model generally scored well on most metrics.

|Metrics|Scores|
|------------|-------------|
|Accuracy|0.9047|
|Sensitivity|0.8602|
|Specificity|0.9503|
|Precision|0.9466|
|Misclassification rate|0.095|
|F1 Score|0.9014|

| Receiver Operating Characteristic Curve |
<img src="https://github.com/seannjk/ga_projects/blob/82f490d2988a4ab956a1169e14e84f4afc1a32ea/project_3/Images/ROC.png">

 For interpretation, the higher the AUC, the better our model is actually performs. The AUC is more descriptive than accuracy because it is a balance of accuracy and false positive rate.

#### Conclusion on Model Evaluation
- Recalling our problem statement, we aimed to select one model which best predicts the classification of the subreddit for current and future posts submitted by either dog or cat owners. This model chosen is the Logistic Regression with TFIDF Vectorizer, given it's best accuracy score compared with other classification models (e.g. Random Forest, Naive Bayes). The model shows relatively high training (about 91.3% after fit.transform X_train set) and testing accuracy (about 90.5% after transforming X_test set), Our model also shows a high AUC score (~96.6%), which shows good balance between accuracy score and false positive rates.

### 5. Application of Model to New DataFrame
- We pulled another ~1500 posts dated (01 Jan 2010 to 31 Dec 2010) each from subreddits "Dogs" and "cats", and created a new dataframe from these posts.
- After data cleaning, we applied the logistic regression with TFIDF Vectorizer to the dataframe.
- The model still performed well, with relatively high training (about 93.9% after fit.transform X_check_train set) and testing accuracy (about 89.2% after transforming X_check_test set). It appears that there is some overfitting issue.

# Business Recommendations
- Based on the top word features in the subreddit Cats, we may encourage CatDog to:
  1. Start a pet-friendly photoshoot space-cum-cafe targeted mainly at cat owners. Cat owners can bring their cats here, dress them up and take instagram/tiktok-worthy pictures of their cats, or together with their cats. The cafe also can serve as a community gathering space for cat owners, and host monthly photoshoot competitions for their cats.  
  2. Start a photography service for cat owners who enjoy having their photos taken.
  3. Selling affordable pet costumes/apparels for cat owners via e-commerce.
  4. Grooming services for Cat owners.

- Based on the top word features in the subreddit Dogs  + earlier bigram analyzed, we may encourage CatDog to:
  1. Start a business model/app that provides mentorship/consultancy services via tele-advice for new and veteran dog owners. This may help alleviate possible anxieties amongst new dog owners, guide new dog owners on what to look out for (e.g. buying the best insurance) and provide care-related advice for dogs where applicable. Use of the app/business may be chargeable.
  2. Start an ethical/responsible dog/puppy breeding service
  3. A dog training school/program for first time dog owners, as well as training/guidance program for dog owners whose dogs are becoming adults.

# Future recommendations for NLP + Things to Improve
- Plan ahead - we can't build a predictive model without sufficient training data.
- While the highest-performing is logistic regression, I should use ensemble modeling methods like sklearn’s VotingClassifier to improve accuracy.
- For modeling rigor, literal subreddit name references should have been removed as individual words (e.g. "dog", "cat") were left in earlier on.
- Duplicates could have been dropped using inbuilt function .
- POS tagging could have been used to better interpret the data.
- Perhaps this project could be improved by performing a more developed form of sentiment analysis on the data in future studies.


# Reference
- https://www.straitstimes.com/lifestyle/home-design/more-interested-in-adopting-or-fostering-pets-during-covid-19-pandemic-as-they
- https://www.reddit.com/r/cats/
- https://www.reddit.com/r/dogs/
