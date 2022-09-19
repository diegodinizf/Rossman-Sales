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




