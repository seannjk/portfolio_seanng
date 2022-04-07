
## Background and Introduction
========================================

*The SAT, which is administered by the College board, is a standardized test that is used for college admissions in the U.S. As part of the data scientist team on the Educational Testing Services under the College Board, we assert that participation in SAT test may likely translate to fair evaluations on students' readiness for college/career, increase their chances of gaining admission to good schools and subsequent upward social mobility in the long-term.*

*In this project, we will be taking a deeper dive into the SAT data we gathered for 2017, 2018 and 2019. We will then dive into SAT data in the state of California specifically, and identify key trends in the participation rates amongst different counties. Lastly, we will provide recommendations to increase the SAT participation rates based on our findings and insights*


## Problem Statement
=============================

*As part of the data scientist team, we examine possible explanations for declining/low SAT participation rates 
across counties in California, U.S. More specifically, we would like to investigate if SAT participation rates is indeed correlated with household median income levels across counties in California, U.S. Based on the data, we would like to propose best practices to improve SAT participation amongst these counties.*


## My Data Dictionary 
============================

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**county**|*object*|SAT 2019 California New|County in the state of California, US| 
|**enroll11**|*float*|SAT 2019 California New|The total number of grade 11 enrollments in SAT 2019| 
|**numtsttakr11**|*float*|SAT 2019 California New|Number of actual Test Takers of Grade 11 | 
|**numerwbenchmark11**|*float*|SAT 2019 California New|The number of grade 11 students who met or exceeded the benchmark for Evidence-Based Reading & Writing (ERW)| 
|**pcterwbenchmark11**|*float*|SAT 2019 California New|The percentage of grade 11 students who met or exceeded the benchmark for Evidence-Based Reading & Writing (ERW)| 
|**nummathbenchmark11**|*float*|SAT 2019 California New|The number of grade 11 students who met or exceeded the benchmark for Math| 
|**pctmathbenchmark11**|*float*|SAT 2019 California New|The percentage of grade 11 students who met or exceeded the benchmark for Math| 
|**totnumbothbenchmark11**|*float*|SAT 2019 California New|The total number of grade 11 students who met or exceeded the benchmark for both ERW and Math| 
|**pctbothbenchmark11**|*float*|SAT 2019 California New|The total percentage of grade 11 students who met or exceeded the benchmark for both ERW and Math| 
|**participation_rate_grade11**|*float*|SAT 2019 California New|The percentage of actual test takers out of all grade 11 SAT enrollees (value is shown as approximate decimals e.g. 0.32 = 32% )| 
|**enroll12**|*float*|SAT 2019 California New|The total number of grade 12 enrollments in SAT 2019| 
|**numtsttakr12**|*float*|SAT 2019 California New|Number of actual Test Takers of Grade 12| 
|**numerwbenchmark12**|*float*|SAT 2019 California New|The number of grade 12 students who met or exceeded the benchmark for Evidence-Based Reading & Writing (ERW)| 
|**pcterwbenchmark12**|*float*|SAT 2019 California New|The percentage of grade 12 students who met or exceeded the benchmark for Evidence-Based Reading & Writing (ERW)| 
|**nummathbenchmark12**|*float*|SAT 2019 California New|The number of grade 12 students who met or exceeded the benchmark for Math| 
|**pctmathbenchmark12**|*float*|SAT 2019 California New|The percentage of grade 12 students who met or exceeded the benchmark for Math| 
|**totnumbothbenchmark12**|*float*|SAT 2019 California New|The total number of grade 12 students who met or exceeded the benchmark for both ERW and Math| 
|**pctbothbenchmark12**|*float*|SAT 2019 California New|The total percentage of grade 12 students who met or exceeded the benchmark for both ERW and Math| 
|**medianhouseholdincome**|*int*|SAT 2019 California New|The median household income (in USD) based on county (based on 2015 to 2019 American Community Survey 5 years estimates)| 
|**participation_rate_grade12**|*float*|SAT 2019 California New|The percentage of actual test takers out of all grade 12 SAT enrollees (value is shown as approximate decimals e.g. 0.32 = 32% )| 


## Exploratory Data Analysis 
====================================

#### *Step 1 - Import and identify abnormalities in the data.*
- `Import libraries`: *scipy.stats, pandas, numpy, matplotlib.pyplot, seaborn as sns*
- `Import CSV files`: 
    - *Participation rates and scores in 2017, 2018 and 2019 SAT administration by US states* (sat_2017, sat_2018, sat 2019)
    - *2019 Participation rate and scores of counties for SATs in the various counties in California, US* (sat_2019_ca)
    - *2019 Household median income by county* (median household income by county)


#### *Step 2 - Clean the data*
- `sat_2017, sat_2018, sat_2019`:
    - *Columns names changed to lowercase*
    - *Fix any individual values to the appropriate type, e.g. participation rate is int*
    - *All spaces in column names removed*
    - *Ensure column names should be unique and informative.*
    
- `sat_2019_ca`: 
    - *Renamed file to `sat2019cali`*
    - *Displayed the data types of each feature.*
    - *Columns names changed to lowercase*
    - *Check for missing values, and replace weird/undesirable values "-" instead of NaN.* 
    - *Fix any individual values to the appropriate type, e.g. TotNumBothBenchmark12  is int*
    - *Ensure column names should be unique and informative.*
    - *Dropped unwanted columns*
    - *Additional data needed to answer Problem Statement*
    
- `2019 Household median income by county`: 
    - *Additional data added to answer Problem Statement*
    - *Renamed file to `hhincome2019`*
    - *Dropped unwanted columns*
    - *Made values more readable by removing unnecessary words e.g.'county* under the column "county*
    - *Columns names changed to lowercase*
  

#### *Step 3 - Merge the data*
- `sat_2017, sat_2018, sat_2019`:
    - *Merged all 3 files to create a new file `sat_2017_18_19`*
    - *New merged dataframe `sat_2017_18_19` saved as CSV in code folder*
    
- `sat2019cali`& `hhincome2019`: 
    - *Dataframes merged so statistical analysis can be done*
    - *New merged dataframe `sat2019calinew` saved as CSV in code folder*


#### *Step 4 - Data exploration*
- `sat_2017_18_19`:
    - *Generate descriptive statistics, which include those that summarize the central tendency, dispersion, shape of a dataset’s distribution (e.g. df.describe() to find mean value of participation rates in 2017, 2018 and 2019)*
    - Generated Bar Chart (Fig 1) to discover data trends, 
    - Sort by states with highest SAT participation rate and compare to California, the largest US state. 
    - This helps us to determine the reason to get curious about exploring California's participation rates.
  
- `sat2019calinew`: 
    - *Generate descriptive statistics, which include those that summarize the central tendency, dispersion, shape of a dataset’s distribution (e.g. df.describe() to find mean value of participation rates across counties in grade 11 and 12 respectively)*
    - *Sorted values to find the top 10 counties with highest SAT participation rates in grade 11 and 12, and bottom 10 counties with lowest SAT participation rates in grade 11 and 12*
    - *Sorted values to find the top 10 counties with best overall SAT performances in grade 11 and 12, and bottom 10 counties with lowest overall SAT performance in grade 11 and 12*


#### *Step 5 - Visualize the data*
- `boxplot` *created to understand the spread of household median income across counties*. **See Fig 2**.
- `Heatmap` *created to discover data trends and correlations between variables of interest.* **See Fig 3**.
- `Scatter plot` and `regression line` *created to observe if household median income has impacts on both participation rate and scores.* **See figs 4 and 5**. 
- `Bar chart` *created to illustrate how the SAT participation rates are reflected in the bottom 10 poorest and top 10 richest counties (based on median household income) across grade 11 and 12 in California.* **See Figs 6, 7, 8 and 9**. 


#### *Step 6 - Describe any findings*
- `sat_2017_18_19`:
    - *Based on the descriptive statistics above, an increase in the participation rate is noted from year 2017 to 2019 (from 38% in 2017, to 45% in 2018 and 49% in 2019).The largest state is California, and comprises 1.95 million students enrolled in public high schools in California, the highest figure in the United States. Lets take a look at whether California is in the top 15 participation rate in 2019.*
    - *California is not even in the top 15 states with highest participation rates in SAT if we filter the . As the largest state in the US in 2019-2020, California  still did not have high participation rates. 
    - *It is even more surprising to note that California, being ranked the largest US state, comprise of 1.95 million students enrolled in public high schools in California, the highest figure in the United States.*
    - *We are curious to examine the state of California to understand participation rates and see what factors contribute to lower SAT participation rates. We can propose best practices to improve SAT participation rates based on these contributing factors.*
    
- `sat2019calinew`: 
    - *Based on the heatmap (**Fig 3**), which maps correlation between variables, we found that Median household income and participation rates amongst grade 12 is positively correlated, with a number of 0.68. Similarly, median household income and participation rates amongst grade 11 is positively correlated as well, with a number of 0.57.*
    - *Surprisingly, there is a low correlation between median household income and total percentage of grade 12 students who met or exceeded the benchmark for both ERW and Math (number of 0.38), as well as total percentage of grade 11 students who met or exceeded the benchmark for both ERW and Math (number of 0.36).*
    - *Let's visualize this correlation between median household income and participation rates, and between median household income and performance a bit better.*

- *Based on a scatterplot/regression line plot (**Fig 4**), we can observe that counties with lower median household incomes are correlated with lower SAT participation rates for both grades. The converse is true for counties with higher median household incomes.*

- *We also observed that median household income and performance are somewhat correlated (**Fig 5**). However, the data in this relatioship appears more spread out as compared to when measuring median household income and participation rate data. The linear relationship between the two appears to be weaker than the linear relationship between participation rates and income level. Hence, we decided not to investigate this particular correlation.* 

- *Based on the bar charts (**Figs 6, 7, 8, 9**), we can see that the the percentage of participation amongst grade 11 and grade 12 students in the poorest 10 counties in California fall below the overall participation rates across the state of California. However, we can see that the the percentage of participation amongst grade 11 and grade 12 students in the richest 10 counties in California are close to/exceed the overall participation rates across the state of California*

- **Given our data above, there is a strong, positive correlation between median household income and SAT participation rates in counties across California. More specifically, the lower the median household income in a county, the more likely it is for that county to have a lower SAT participation rate be it grade 11 or 12.**

#### *Step 7 - Recommendations & Conclusion *

- *We would like to make various recommendations based on our findings above.*

`Recommendation 1`: 
- `Increase access to SAT participation by removing financial barriers` Given that the ability to pay for SAT fees might likely be a barrier to SAT participation, we propose offering SAT free of charge for all grade 11 students to ensure universal SAT participation. This would also boost their confidence in the event they wish to re-attempt SAT in grade 12. 

`Recommendation 2`: 
- `Offer SAT during regular school hours` SAT are conducted mostly on Saturdays, which may likely deter low-income individuals from participating in SAT since they are more likely to have part-time jobs, family responsibilities, etc. We propose offering SAT to be conducted during regular school hours to increase their access to SAT participation. 

`Recommendation 3`: 
- `Offer free access to extra learning materials` Students from lower-income counties, unlike their richer counterparts, may likely have less access to additional learning materials such as SAT online courses and prep classes. Consequently, these students may become less motivated to participate in SAT. We propose offering free access to these learning materials to low-income students to increase their motivation and readiness to take SAT. 

`Recommendation 4`: 
- `Create a college-going culture` Students from lower-income counties are more likely than their higher-income counterparts to have social and language barriers, less access to information on college, less exploration because of low expectations and underestimation of the amount of financial help available in college. These factors may possibly deter participation in SAT. We propose 1) training to school staff on how to begin promoting high standards and expectations for students and families to achieve at a higher level, as well as 2) academic planning for college and career readiness and college, career exploration and selection processes. 


## *References*
- https://www.census.gov/search-results.html q=california+median+income&page=1&stateGeo=none&searchtype=web&cssp=SERP&_charset_=UTF-8
- https://files.eric.ed.gov/fulltext/ED561029.pdf
- https://ifs.org.uk/bns/bn133.pdf
- https://thermtide.com/10448/uncategorized/sat-battles-claim-of-socioeconomic-discrimination/
- https://www.statista.com/statistics/183497/population-in-the-federal-states-of-the-us/ 
- https://www.statista.com/statistics/1036120/public-high-school-enrollment-state-us/)



