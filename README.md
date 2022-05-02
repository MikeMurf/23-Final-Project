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

 



