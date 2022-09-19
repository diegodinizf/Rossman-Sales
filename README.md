# Rossmann Stores - 6 Weeks Sales Forecast

Disclaimer: this project was inspired by the "Rossmann Store Sales" challenge published on kaggle (https://www.kaggle.com/c/rossmann-store-sales). It is a fictitious project but with all the steps of a real project.

## Business Scenario
The sales director of Rossmann's stores wants to estimate the sales forecast for the next 6 weeks on each store unit of the company spread across Europe

## Solution Methodology
This project was carried out following CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology.
You can read more about it on: https://www.datascience-pm.com/crisp-dm-2/ 
![image](https://user-images.githubusercontent.com/110054775/190948215-a5c92fd4-95e3-43a4-bd60-ed69bf094860.png)

## Data Collection and Understanding
Data was collected from kaggle as a .csv file. The step of understanding data involved changing data types, filling missing values and checking the statistical metrics of numeric and categorical data.
An overview of some attributes and data:
- In total, there ate 1017209 sales records
- There are 1115 different stores
- Data contanins attributes such as: "date", "store_type", "customers", "assortment", "school_holiday", "open", "promo2", "sales", among others.

**Assumption**: This project does not contemplate the prediction of number of customers of each store. Since this attribute will only be know on the day of sales, it was removed from the train data

## Exploratory Data Analysis
In order to understand better the correlation between the attributes and their importance to data, this step was created. From here, it will be generated insights that were validated or refutaded.
To help with the progress of this step, a mindmap was created.
![Mind_Map_Hip](https://user-images.githubusercontent.com/110054775/190950264-09030b73-147a-4c07-b5ec-83dd9ee0e042.png)

This diagram helped to guide the EDA. With the features listed above, 12 hypotheses were created

1. Stores with a larger assortment should sell more
2. Stores with closer competitors should sell less
3. Stores with longer-standing competitors should sell more
4. Stores where products cost less for longer (active promotions) should sell more
5. Stores with more promotion days should sell more
6. Stores with more extended promotions should sell more
7. Stores open during Christmas holiday should sell more
8. Stores should sell more over the years
9. Stores should sell more in the second half of the year
10. Stores should sell more after the 10th day of each month
11. Stores should sell less on weekends
12. Stores should sell less during school holidays

The discussion of each hypothesis is found in the notebook file.

The ones that were judged to be most relevant were discussed below.

### 1. Stores with a larger assortment should sell more

**True** On average, stores with extra assortment tends to sell more, followed by extended and basic assortments, respectively.
Also, the stores sales by assortment over time shows that stores with extra assortment have an increase of their sales.

![image](https://user-images.githubusercontent.com/110054775/190952028-2beb609c-8693-4667-9a43-52a92f7a06f9.png)


### 9. Stores should sell more in the second half of the year, on average

**False**. There is a tendency of sales decrease over the year. In view of this, it is seen a higher concentration of sales in the first half of the year.
It is important to point out that november and december sales tends to increase the sales, due the proximity with the Christmas holiday.

![image](https://user-images.githubusercontent.com/110054775/190952847-733bffe5-3e2a-4af5-949c-5e012b0d4e79.png)

### 10. Stores should sell more after the 10th day of each month, on average
**False**. The composition of the 2 top graphs shows that the highest sales concentration are in the beggining and in the end of the months. However, the sales tend to decrease over the month. 

In this case, the peaks of sales over the month can be explained by dates next to salary pay day.

![image](https://user-images.githubusercontent.com/110054775/190953280-40482884-191a-4275-b80f-8cf67948deb6.png)

## Data Preparation
In this step two important actions were made: stardardization and feature selection.

As a way to transform all data into the same scale range, some rescaling and encoding was made; and as a highlight, cyclical data, such as month and day of week, were transformed using sine and cosine.

With this, it was possible to make data recognize the proximity between the 30th day of the month and the 1st of the next month, as the scheme shows.

![Circle_cos_sin](https://user-images.githubusercontent.com/110054775/191055399-5cd859b6-b87f-4063-9b8b-e97bcd725cf0.gif)


## Machine Learning Modeling

Four different models (linear regression, regularized linear regression - lasso, random forest and XGBoost) were evaluated using a time series cross-validation. It is schematically represented below

![image](https://user-images.githubusercontent.com/110054775/191046190-541a3f65-3b7e-493b-b5bd-bce890f2f11a.png)
 
 The test data was fixed as a 6 weeks portion of the data; then the model was trained and its performance evaluated.
 The time series cross-validation works increasing the training dataset and varying the time portion of test data through its iteractions.
 
 The results in terms of Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE) AND Root Mean Square Error (RMSE) are presented below:
    
|Model|MAE|MAPE|RMSE|
|-----------------------------|------------------|-------------|------------------|
|Random Forest Regressor	    |796.7 +/- 146.77	 |0.11 +/- 0.02|1202.19 +/- 269.83|
|XGBoost Regressor	          |1062.85 +/- 174.01|0.15 +/- 0.02|1503.14 +/- 273.61|
|Linear Regression	          |1933.91 +/- 79.66 |0.28 +/- 0.02|2739.27 +/- 154.61|
|Regularized Linear Regression|1980.51 +/- 96.91 |0.28 +/- 0.01|2849.35 +/- 200.81| 

Although Random Forest model appears to perform better, the model chosen to be implemented was the XGBoost, due to its lower memory consuming and does not have significant difference in performance.

## Hyperparameter Tuning
Using the random search method, different values were chosen for the XGBoost model: "n_estimators", "eta", "max_depth", "subsample", "colsample_bytree" and "min_child_weight". 5 iteractions were performed using different parameters combination and it could result in the following performance through cross-validation:

|Model|MAE|MAPE|RMSE|
|-----------------------------|------------------|-------------|------------------|
|XGBoosr Regressor	          |984.84 +/- 146.91 |0.13 +/- 0.02|1410.79 +/- 251.6 |

The best hyperparameter combination was used to train the entire model:

```python
model_xgb_tuned = xgb.XGBRegressor(objective = 'reg:squarederror',
                                   n_estimators = 300,
                                   eta = 0.1,
                                   max_depth = 7,
                                   subsample = 0.5,
                                   colsample_bytree = 0.5,
                                   min_child_weight = 3).fit(x_train,y_train)
```
And the overall performance was:

|Model|MAE|MAPE|RMSE|
|-----------------------------|------------------|-------------|------------------|
|XGBoost Regressor	          |832.97            |0.12         |1205.31           |

## Business Performance

After the evaluation of the predictions, it was possible to translate the model performance to the business.

![image](https://user-images.githubusercontent.com/110054775/191058856-99a9f40a-0342-4f63-8083-af5d6b1a8353.png)

- The **top-left** graph shows us how much the predictions get close to the real sales values
- The **top-right** graph shows the error rate, in other words, it is a representation of whethe the values are underestimated or overestimated.
- The **bottom-left** graph is the error distribution, which is close of a normal distribution
- The **bottom-right** residual graph brings the insight that errors tend to be higher when the forecast of sales is between $5k and $10k

## Model Deployiment

The model used for the predictions was deployed in Google Cloud Platform. To get the values, it was created a Telegram Bot.

In this application, the user inputs the Store ID and the app responds with the forescast

![ezgif-2-f475e308c7](https://user-images.githubusercontent.com/110054775/191134126-b365d7de-8e7a-41e2-ab9b-d54d43d011f1.gif)

To access the Bot inside Telegram, search for @rossmannapp_bot








