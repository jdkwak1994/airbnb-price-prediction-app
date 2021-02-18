# Airbnb Price Prediction Application
The purpose of this project is to create a price prediction app for Airbnb NYC housings through various inputs such as borough, room type, reviews per month, and availability in a year.

You can access the application through the link: https://jdkwak1994-airbnb-price-predic.herokuapp.com

### Dataset Sources:
* https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data?select=AB_NYC_2019.csv
* https://www.kaggle.com/kritikseth/us-airbnb-open-data#__sid=js0
* http://insideairbnb.com/get-the-data.html

---

## Project Description
**Step 1: Data Cleaning and Machine Learning Models**
* Clean up the given data by adding `0` to any `N/A` data.
* Dummy data with neighborhood type, room type, reviews per month, and availability in 365.
* 3 models are created: linear regression model, xgboost model, and random forest model.

**Step 2: HTML/CSS/JS**
* Create application webpage under `index.html`
* Add different pages such as infographic, project information, and prediction.
* Make sure the pages are mobile friendly.

**Step 3: Flask App and Heroku Deployment**
* Connect the created html pages to `app.py`.
* Deploy the application through Heroku to make it accessible by public.

---

## Sample Screenshots
* **Main Page**
![Screenshot](templates/static/images/mainpage.png "Screenshot")

* **Prediction Page**
![Screenshot](templates/static/images/predictionpage.png "Screenshot")

* **Infographic Page**
![Screenshot](templates/static/images/infographicpage.png "Screenshot")

---

## Getting Started
**Steps below will run the application via Flask, which uses all 3 models**
1. Clone this repo.
2. Uncomment (get rid of the #) lines 69 and 70 of `app.py`.
3. Comment out (add the # in front of the line) line 71.
4. Change the line 77 to `avgprice = round((sum(price) / 3), 2)`.
5. Run `flask run` or `python -m http.server` or any other method for this purpose
---

### Team Members:
* [Jeongdae (JD) Kwak](https://github.com/jdkwak1994)
* [Adriana Cieslak](https://github.com/AdrianaCieslak)
* [Anumala Thapa](https://github.com/Anumala89)
* [Samuel Okunola](https://github.com/samuelokunola326)
