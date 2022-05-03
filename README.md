# Machine Learnings in the Brave New World of Living with Covid-19 

![image](https://user-images.githubusercontent.com/89948865/166318657-9897e176-9e28-4de7-9e0d-440d46380d58.png) 

![image](https://user-images.githubusercontent.com/89948865/166318967-e6316df7-7d36-4654-b5da-db85c0008cac.png)
 
## 1.	How We Arrived at Our Learnings

This report details how we arrived at our learnings and includes:
1. Project Overview / Requirements
2. Team Members
3. Brief Project Description
4. Project Rationale
5. Literature Review
6. Evaluation of Machine Learning Models
7. Evaluation of Machine Learning Models – Results and Conclusions
8. Technologies Used
9. Project Datasets
10. Database QuickDB Code
11. Database Schema – Entity Relationship Diagram
12. Database Description
13. Database Meta Data
14. Data Transformation

## 1.	Project Overview /Requirements:  

This project was initiated to satisfy the requirements of the “Final Project” assignment for the Monash Data Analytics Bootcamp.
These requirements are as follows.

![image](https://user-images.githubusercontent.com/89948865/166320429-4e8b0ce3-a305-48cd-b705-56118f29b5a6.png) 

![image](https://user-images.githubusercontent.com/89948865/166320483-549ce343-ef56-45b4-885e-0f9d5c528e36.png) 
 
![image](https://user-images.githubusercontent.com/89948865/166320580-c7d4ece0-2ec6-4417-8a64-d527f1dbb850.png) 

## 2.	Team Members: 

* Megan Greenhill 
* Hesh Kuruppuge
* Jacqueline Xia 
* Mike Murphy

## 3.	Brief Project Description: 

The project uses the machine learning approach to create a model for analysing and forecasting the Covid-19 Pandemic.
The project:
* evaluates various regression model techniques to find the optimal regression model for analysing and forecasting Covid-19 - Confirmed Cases, Active Cases, Recovered Cases and Deaths from the John Hopkins University (JHU) time series data sets which are published daily,
* uses the optimal regression model identified above to produce forecasts of Covid-19 Hospitalisations (the Dependent Variable) based on: - Confirmed Cases, Active Cases, Recovered Cases and Deaths(the Independent Variables),
* uses Tableau to apply its exponential smoothing for forecasting and plotting visualisations of Covid-19 - Confirmed Cases, Active Cases, Recovered Cases and Deaths,
* compares the results of the optimal regression model to the results produced by Tableau,
* summarises the project results / conclusions,
* performs Extract, Transform and Load to extract Covid-19 data from the John Hopkins University (JHU) Time Series data sets, 
* combines the data sets into a single integrated table in a PostGreSQL data base,
* uses a Python Flask-powered API to access the integrated PostgreSQL database table and:
  * use a Python library called “psycopg2” to extract the table and create a JSON file,
  * assign each column of the database table to a dictionary,
  * JSONify the dictionary,
  * return the JSON dictionary through the app, 
  * the app is then called in the Java Script to create visualisations;

## 4.	Project Rationale:
The project:
* satisfies the requirements for the Final Project for the Monash Data Analytics Bootcamp,
* provides an approach for fine tuning the optimal regression model identified as future data becomes available,
* provides a model for visualising current and future Covid forecasts, and 
* provides a useful tool for further development of analysis and forecasting capability.

## 5.	Literature Review: 

* **Literature Review:** 

An extensive literature review was conducted to identify work that may have done in the area of analysis and forecasting Covid-19 time series analysis data.
* **Citations** 

From the reviewed literature three articles in particular were chosen for detailed analysis and citation purposes. 
They are:
  * **[1]	“Analysis and Prediction of Covid-19 using Regression Models and Time Series Forecasting”** –  which can be found at the following link:
  * https://ieeexplore.ieee.org/document/9377137 
  * [S. Shaikh, J. Gala, A. Jain, S. Advani, S. Jaidhara and M. Roja Edinburgh, "Analysis and Prediction of COVID-19 using Regression Models and Time Series Forecasting," 2021 11th International Conference on Cloud Computing, Data Science & Engineering (Confluence), 2021, pp. 989-995, do: 10.1109/Confluence51648.2021.9377137.]

This article describes the evaluation of Linear and Polynomial Regression Models for 
forecasting future Covid-19 cases from a historical data set of some 7 months cases in India. 

  * **[2]	“Polynomial Regression”** – Author:  - Animesh Agarwal
https://towardsdatascience.com/polynomial-regression-bbe8b9d97491
				
This article is part of a series of blogs published by the author  describing Polynomial 
Regression and ways of achieving the best fit of the Regression line to the data. It provides sample code to demonstrate how to minimise the effects of over-fitting and under-fitting the Regression line to the data.

  * **[3]	“Lasso , Ridge & Elastic Net Regression: A Complete Understanding (2021)”**
– Author:  - Rohit Bhadauriya
https://medium.com/@creatrohit9/lasso-ridge-elastic-net-regression-a-complete-understanding-2021-b335d9e8ca3

This article provides an excellent explanation of Regression and ways of achieving the best fit of the Regression line to the data sets. It also provides sample code to demonstrate how to minimise the effects of over-fitting and under-fitting the Regression line to the data.

## 6.	Evaluation of Machine Learning Models 

* **Evaluation of LinearRegression Models**
  * LinearRegression
  * Lasso
  * Ridge
  * ElasticNet
  * Lasso, Ridge and ElasticNet are models used to minimise the errors of **overfitting** and **underfitting** which can occur when applying regression to data sets.
  * **There are two methods of overcoming overfitting:**
  * **reducing the model complexity,** and, 
  * **regularisation** which  tries to improve the accuracy of the model.
-	**Regularisation is where Lasso, Ridge and ElasticNet come into play.**
-	**Lasso** – the **Least Absolute Shrinkage and Selection** model aims to overcome overfitting by applying the penalty L1 which is the sum of the absolute value of the beta coefficients of the quadratic equation that describes the line of best fit. 
-	**Ridge** - the model aims to overcome overfitting by applying penalty L2 which is the sum of the square of the magnitude of beta coefficients of the quadratic equation that describes the line of best fit.
-	**ElasticNet** – combines the techniques of Lasso and Ridge to get the best of both worlds.
-	[Please refer to: - [3] -  “Lasso , Ridge & Elastic Net Regression: A Complete Understanding (2021)” for a detailed explanation of these concepts.] 

* **Evaluation of Polynomial Regression Models**
The “Polynomial Regression” article [2] deals with the issue of choosing an optimal model. To answer this question, we needed to understand the **bias** vs **variance** trade-off. 

* **Bias** refers to the error due to the model’s simplistic assumptions in fitting the data. A high bias means that the model is unable to capture the patterns in the data and this results in under-fitting the model to the data points.

* **Variance** refers to the error due to the complex model trying to fit the data. High variance means the model passes through most of the data points and it results in over-fitting the data to the data points.

**Ideally, a machine learning model should have low variance and low bias.** 

**But practically it’s impossible to have both. Therefore, to achieve a good model that performs well both on the training and unseen data, a trade-off is made between Bias and Variance.**
 
## 7.	Evaluation of Machine Learning Models – Results and Conclusions 

The machine Learning models were run with **differing combinations of Independent Variables** and the results are tabulated below showing combinations of variables, **Mean Square Error** values and **R Squared values**.

**7.1	Machine Learning models using Linear Regression**
The results  show that the best outcomes were obtained using 4 variables – Confirmed Cases, Active Cases, Recovered Cases and Deaths (yellow highlight). 
The next best results were obtained using any combination of 3 variables (green highlight). 
 
**7.2	Machine Learning model using Polynomial Regression with X in the 5th Degree**
The results  show that the best outcomes were obtained using 4 variables – Confirmed Cases, Active Cases, Recovered Cases and Deaths (yellow highlight). 
The next best results were obtained using the combination of Confirmed Cases and Recovered Cases (green highlight). 
	
**7.3	Machine Learning using Tableau Exponential smoothing** 
 
![image](https://user-images.githubusercontent.com/89948865/166322728-cf558d03-c986-4d8a-8e24-57f8ac66c8fa.png) 

## 8.	Technologies Used: 

The project used the following technologies:
*  Linear Regression Evaluation:
*  Linear Regression
*  Lasso Regression
*  Ridge Regression
*  ElasticNet Regression
*  Polynomial Regression Evaluation:
*  Polynomial Regression with X in the Nth degree
*  Polynomial Regression Analysis Code from [2] -  Blog by Animesh Agarwal
*  Regression Execution
*  Scikit-Learn
*  Tableau
*  PostGreSQL Data Base
*  Python / Pandas
*  Python Flask Powered API
*  Python Library - psycopg2
*  Java Script D3.js
*  HTML
*  CSS
*  Bootstrap
* GitHub

## 9.	Project Datasets: 

The datasets for the project can be found at the following link.
  * “JHU – Time Series Daily Reports”
  * https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

  * The hospitalisation dataset for the project can be found at the following link.
  * https://ourworldindata.org/covid-hospitalizations

## 10.	Database QuickDB Code 

country_codes
-
country_id VARCHAR(255)
country_name VARCHAR(255)
continent_name VARCHAR(255)

covid_cases
-
country_id VARCHAR(255) FK - country_codes.country_id
date VARCHAR(255)
confirmed INT
deaths INT
recovered INT
active INT
case_fatality VARCHAR(255)
new_cases INT
new_deaths INT
new_recovered INT

population
-
country_id VARCHAR(255) FK - country_codes.country_id
population INT

vaccinations
-
country_id VARCHAR(255) FK - country_codes.country_id
date VARCHAR(255)
fully_vaccinated_per_hundred INT
not_fully_vaccinated_per_hundred INT
boosted_per_hundred INT

full_covid_table
-
country_id VARCHAR(255) FK - country_codes.country_id
country_name VARCHAR(255)
continent_name VARCHAR(255)
date VARCHAR(255)
confirmed INT
deaths INT
recovered INT
active INT
case_fatality VARCHAR(255)
new_cases INT
new_deaths INT
new_recovered INT
population INT
vaccinated_per_hundred INT
fully_vaccinated_per_hundred INT
not_fully_vaccinated_per_hundred INT
boosted_per_hundred INT
hospital_occupancy INT

## 11.		Database Schema – Entity Relationship Diagram  

![image](https://user-images.githubusercontent.com/89948865/166323124-32f0dab0-7632-4b1d-afd2-bd3e37345bbe.png) 

## 12.	Database Description 

The  key to the data base was to use the **International Standards Organisation (iso_code: ISO 3166-1 alpha-3 – three-letter country code)** henceforth referred to as “iso-code”, to create relationships between the tables. 
The “country-codes” table contains the  “iso-code” and matching “country-name” for all countries covered by the “iso-code” and was generated during the Extraction phase of the project.
The “covid-cases” table contains the basic cleansed data from the JHU Data Sets which form the basis of the global view of Covid-19 cases.
The “vaccinations” table contains vaccination status from the Our World in data Vaccination data set.
The "full-covid-table" contains all of the information required to drive our visualisations via the Flask powered API.

## 13.	Database Meta Data 

“country” table
  * country-id: 	the iso_code: ISO 3166-1 alpha-3 – three-letter country code
  * country-name: 	the name of the country in the ISO data set

“covid-cases” table
  * country-id: 	the iso_code: ISO 3166-1 alpha-3 – three-letter country code
  * date: 		date of the observation
  * confirmed:	        the total number of cumulative confirmed Covid-19 cases regardless of the variant
  * deaths:	        the total number of cumulative deaths attributed to Covid-19 regardless of the variant
  * recovered:	        the total number of cumulative recovered Covid-19 cases
  * active:		the total number of cumulative active Covid-19 cases
  * new_cases:	        the total number of incremental new  Covid-19 cases
  * new_deaths:	        the total number of incremental new Covid-19 deaths
  * new_ recovered:     the total number of incremental new recovered Covid-19 cases

“population” table
  * country-id: 	the iso_code: ISO 3166-1 alpha-3 – three-letter country code
  * population: 	the population of the country at 31/12/2020

“vaccinations” table
  * country-id: 	the iso_code: ISO 3166-1 alpha-3 – three-letter country code
  * date: 		date of the observation
  * vaccinated_per_hundred:
  *                     total number of people who received at least one vaccine dose. If a person receives the first dose of a 2-dose vaccine, 
  *                     this metric goes up by 1. If they receive the second dose, the metric stays the same i.e., 1.
  * fully_vaccinated_per_hundred:
  *                     people vaccinated per 100 people in the total population of the country. If a person receives the first dose of a 2-dose vaccine, 
  *                     this metric stays the same. If they receive the second dose, the metric goes up by 1. 
  * not_fully_vaccinated_per_hundred:
   *                    people not vaccinated per 100 people in the total population of the country
  * boosted_per_hundred:
  *                     people who have received their booster dose per 100 people in the total population of the country
 
## 14.	Data Extract, Transformation, Load: 

  * **Extracting the Data**
The Extract phase  uses urls / wget downloads in place of API calls are APIs are not available for the datasets needed. The JHU time series data sets were retrieved using this method. 

  * **Transforming the Data**
The detailed description of the Data Transformation is covered in the end of this section. It covers both data cleansing and data transformation and does the typical:
  * removing unwanted or duplicate data,
  * fixing structural issues,
  * handling missing data,
  * removing outliers,
  * providing a quality assurance check on the data prior to regression analysis. 

  *  **Loading the Data** 
The code for the PostGreSQL data base load is as follows: 

**Create database connection**
rds_connection_string = "postgres:meg221196@localhost:5432/integrated_covid_view_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

**Confirm database tables**
engine.table_names()
  
**Load dataframes to database tables**
full_covid_table.to_sql(name='full_covid_table', con=engine, if_exists='append', index=False)
country_codes.to_sql(name='country_codes', con=engine, if_exists='append', index=False)
covid_cases.to_sql(name='covid_cases', con=engine, if_exists='append', index=False)
population.to_sql(name='population', con=engine, if_exists='append', index=False)
vaccinations.to_sql(name='vaccinations', con=engine, if_exists='append', index=False)
 
**The detailed Data Transformation steps are as follows:**
1)	Save DFs to CSVs to do exploratory data analysis.
2)	Conduct exploratory data analysis.
3)	Use melt() to unpivot DataFrames from current wide format 265 rows × 749 columns into long  format 208600 rows × 6 columns.
4)	Remove recovered data for Canada due to mismatch issue. Canada recovered data is counted for the whole Country instead of by Province/State which is how Canada and the rest of the world count data for "Confirmed Cases" and "Deaths".
5)	 Merge the three JHU dataframes, Confirmed Cases, Deaths, Recovered Cases.
a.	merge confirmed_df_long and deaths_df_long into full_table
b.	merge full_table and recovered_df_long
6)	Check Canada data in "full_table" - "recovered" should be 0 and check of CSV file confirms that it is.
7)	Convert date from string to datetime.
8)	Detect missing values NaN.
9)	Replace 'recovered' NaNs with zero.
10)	Three cruise ships need to be treated differently to the rest of the cases.So extract and remove data for these ships.
11)	Calculate active cases = confirmed cases - deaths – recovered cases.
12)	Aggregate data into Country/Region and group by Date and Country/Region.
13)	Calculate daily New cases, New deaths and New recovered by deducting the corresponding accumulative data on the previous day
14)	Use pd.merge to group the final data frame on Country/Region / Date.
15)	Fix the new data types as integer.
16)	The final data frame is sorted by Date and Country/Region ascending where: Confirmed Cases, Deaths, Recovered and Active are cumulative data 
17)	for the entire period, and, New cases, New deaths and New Recovered are daily incremental data.
18)	Convert data frame to a csv file for backup.
19)	Read the Vaccination dataset - csv file into a data frame.
20)	Derive the “people_not_vaccinated” from the “people_fully_vaccinated”.
21)	Detect missing values NaN 
22)	Replace NaNs with zero
23)	Data cleansing replace ”United States” with “US” to standardise data.
24)	Save cleansed vaccination data to a CSV for backup.
25)	Read the Population data set - csv file into a data frame.
26)	Detect missing values NaN 
27)	Replace NaNs with zero
28)	Save cleansed Population data to a CSV for backup.
29)	Copy OWID Vaccination data frame, as we want to use OWID country codes.
30)	Add Africas to match population data frame.
31)	Edit “full_grouped” covid case data frame to include country ID.
32)	Change structure of data frames to match structure of tables created in the database.
33)	Set index of country codes data frame and remove null index row.
34)	Covid Cases table - copy only the columns needed into a new Data Frame.
35)	Rename columns to fit the tables created in the database.
36)	Vaccinations table - copy only the columns needed into a new Data Frame.
37)	Rename columns to fit the tables created in the database.
38)	Create PostgreSQL database connection.
39)	Confirm database tables.
40)	Load data frames to the database tables
_______________________________________________________________________________________________________________________________________________________________
