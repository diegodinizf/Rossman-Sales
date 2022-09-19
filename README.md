# Rossmann Stores - 6 Weeks Sales Forecast

Disclaimer: this project was inspired by the "Rossmann Store Sales" challenge published on kaggle (https://www.kaggle.com/c/rossmann-store-sales). It is a fictitious project but with all the steps of a real project.

## Business scenario
The sales director of Rossmann's stores wants to estimate the sales forecast for the next 6 weeks on each store unit of the company spread across Europe

## Solution methodology
This project was carried out following CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.
You can read more about it on: https://www.datascience-pm.com/crisp-dm-2/ 
![image](https://user-images.githubusercontent.com/110054775/190948215-a5c92fd4-95e3-43a4-bd60-ed69bf094860.png)

## Data collection and understanding
Data was collected from kaggle as a .csv file. The step of understanding data involved changing data types, filling missing values and checking the statistical metrics of numeric and categorical data.
An overview of some attributes and data:
- In total, there ate 1017209 sales records
- There are 1115 different stores
- Data contanins attributes such as: "date", "store_type", "customers", "assortment", "school_holiday", "open", "promo2", "sales", among others.

**Assumption**: This project does not contemplate the prediction of number of customers of each store. Since this attribute will only be know on the day of sales, it was removed from the train data

## Exploratory data analysis
