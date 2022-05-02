## Machine Learnings in the Brave New World of Living with Covid-19 

![image](https://user-images.githubusercontent.com/89948865/166318657-9897e176-9e28-4de7-9e0d-440d46380d58.png) 

![image](https://user-images.githubusercontent.com/89948865/166318967-e6316df7-7d36-4654-b5da-db85c0008cac.png)
 
## 1.	How We Arrived at Our Learnings

This report details how we arrived at our learnings and includes:
1.1)	  	Project Overview / Requirements
1.2)	  	Team Members
1.3)	  	Brief Project Description
1.4)	  	Project Rationale
1.5)	  	Project Methodology
1.6)	  	Evaluation of Machine Learning Models
1.7)	  	Evaluation of Machine Learning Models – Results and Conclusions
1.8)	  	Technologies Used
1.9)	  	Project Datasets
1.10)	  Database QuickDB Code
1.11)	  Database Schema – Entity Relationship Diagram
1.12)	  Database Description
1.13)	  Database Meta Data
1.14)	  Data Transformation

## 1.	Project Overview /Requirements:  

This project was initiated to satisfy the requirements of the “Final Project” assignment for the Monash Data Analytics Bootcamp.
These requirements are as follows.

![image](https://user-images.githubusercontent.com/89948865/166320429-4e8b0ce3-a305-48cd-b705-56118f29b5a6.png) 

![image](https://user-images.githubusercontent.com/89948865/166320483-549ce343-ef56-45b4-885e-0f9d5c528e36.png) 
 
![image](https://user-images.githubusercontent.com/89948865/166320580-c7d4ece0-2ec6-4417-8a64-d527f1dbb850.png) 

## 2.	Team Members: 

Megan Greenhill 
Hesh Kuruppuge
Jacqueline Xia 
Mike Murphy

## 3.	Brief Project Description: 

The project uses the machine learning approach to create a model for analysing and forecasting the Covid-19 Pandemic.
The project:
•	evaluates various regression model techniques to find the optimal regression model for analysing and forecasting Covid-19 - Confirmed Cases, Active Cases, Recovered Cases and Deaths from the John Hopkins University (JHU) time series data sets which are published daily,
•	uses the optimal regression model identified above to produce forecasts of Covid-19 Hospitalisations (the Dependent Variable) based on: - Confirmed Cases, Active Cases, Recovered Cases and Deaths(the Independent Variables),
•	uses Tableau to apply its exponential smoothing for forecasting and plotting visualisations of Covid-19 - Confirmed Cases, Active Cases, Recovered Cases and Deaths,
•	compares the results of the optimal regression model to the results produced by Tableau,
•	summarises the project results / conclusions,
•	performs Extract, Transform and Load to extract Covid-19 data from the John Hopkins University (JHU) Time Series data sets, 
•	combines the data sets into a single integrated table in a PostGreSQL data base,
•	uses a Python Flask-powered API to access the integrated PostgreSQL database table and:
o	use a Python library called “psycopg2” to extract the table and create a JSON file,
o	assign each column of the database table to a dictionary,
o	JSONify the dictionary,
o	return the JSON dictionary through the app, 
o	the app is then called in the Java Script to create visualisations;

## 4.	Project Rationale:
The project:
•	satisfies the requirements for the Final Project for the Monash Data Analytics Bootcamp,
•	provides an approach for fine tuning the optimal regression model identified as future data becomes available,
•	provides a model for visualising current and future Covid forecasts, and 
•	provides a useful tool for further development of analysis and forecasting capability.

## 5.	Project Methodology: 

•	   Literature Review
An extensive literature review was conducted to identify work that may have done in the area of analysis and forecasting Covid-19 time series analysis data.
•	   Citations
From the reviewed literature three articles in particular were chosen for detailed analysis and citation purposes. 
They are:
•	[1]	“Analysis and Prediction of Covid-19 using Regression Models and Time Series Forecasting” –  which can be found at the following link:
https://ieeexplore.ieee.org/document/9377137 

	[S. Shaikh, J. Gala, A. Jain, S. Advani, S. Jaidhara and M. Roja Edinburgh, "Analysis and Prediction of COVID-19 using Regression Models and Time Series Forecasting," 2021 11th International Conference on Cloud Computing, Data Science & Engineering (Confluence), 2021, pp. 989-995, do: 10.1109/Confluence51648.2021.9377137.]

				This article describes the evaluation of Linear and Polynomial Regression Models for 
forecasting future Covid-19 cases from a historical data set of some 7 months cases in India. 

•	[2]	“Polynomial Regression” – Author:  - Animesh Agarwal
https://towardsdatascience.com/polynomial-regression-bbe8b9d97491
				
				This article is part of a series of blogs published by the author  describing Polynomial 
Regression and ways of achieving the best fit of the Regression line to the data. It provides sample code to demonstrate how to minimise the effects of over-fitting and under-fitting the Regression line to the data.

•	[3]	“Lasso , Ridge & Elastic Net Regression: A Complete Understanding (2021)” 
– Author:  - Rohit Bhadauriya
https://medium.com/@creatrohit9/lasso-ridge-elastic-net-regression-a-complete-understanding-2021-b335d9e8ca3

This article provides an excellent explanation of Regression and ways of achieving the best fit of the Regression line to the data sets. It also provides sample code to demonstrate how to minimise the effects of over-fitting and under-fitting the Regression line to the data.

## 6.	Evaluation of Machine Learning Models 

•	   Evaluation of LinearRegression Models
-	LinearRegression
o	Lasso
o	Ridge
o	ElasticNet

-	Lasso, Ridge and ElasticNet are models used to minimise the errors of overfitting and underfitting which can occur when applying regression to data sets.
-	There are two methods of overcoming overfitting:
o	reducing the model complexity, and, 
o	regularisation which  tries to improve the accuracy of the model.
-	Regularisation is where Lasso, Ridge and ElasticNet come into play.
-	Lasso – the Least Absolute Shrinkage and Selection model aims to overcome overfitting by applying the penalty L1 which is the sum of the absolute value of the beta coefficients of the quadratic equation that describes the line of best fit. 
-	Ridge - the model aims to overcome overfitting by applying penalty L2 which is the sum of the square of the magnitude of beta coefficients of the quadratic equation that describes the line of best fit.
-	ElasticNet – combines the techniques of Lasso and Ridge to get the best of both worlds.
-	[Please refer to: - [3] -  “Lasso , Ridge & Elastic Net Regression: A Complete Understanding (2021)” for a detailed explanation of these concepts.] 

•	 Evaluation of Polynomial Regression Models
The “Polynomial Regression” article [2] deals with the issue of choosing an optimal model. To answer this question, we need to understand the bias vs variance trade-off. 

Bias refers to the error due to the model’s simplistic assumptions in fitting the data. A high bias means that the model is unable to capture the patterns in the data and this results in under-fitting the model to the data points.

Variance refers to the error due to the complex model trying to fit the data. High variance means the model passes through most of the data points and it results in over-fitting the data to the data points.

Ideally, a machine learning model should have low variance and low bias. 

But practically it’s impossible to have both. Therefore, to achieve a good model that performs well both on the training and unseen data, a trade-off is made between Bias and Variance.
 
## 7.	Evaluation of Machine Learning Models – Results and Conclusions 

The machine Learning models were run with differing combinations of Independent Variables and the results are tabulated below showing combinations of variables, Mean Square Error values and R Squared values.
7.1	Machine Learning models using Linear Regression
The results  show that the best outcomes were obtained using 4 variables – Confirmed Cases, Active Cases, Recovered Cases and Deaths (yellow highlight). 
The next best results were obtained using any combination of 3 variables (green highlight). 
 

7.2	Machine Learning model using Polynomial Regression with X in the 5th Degree
The results  show that the best outcomes were obtained using 4 variables – Confirmed Cases, Active Cases, Recovered Cases and Deaths (yellow highlight). 
The next best results were obtained using the combination of Confirmed Cases and Recovered Cases (green highlight). 
	
 
 



