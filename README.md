# 🎬 Netflix Data Cleaning & Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on cleaning and analyzing the **Netflix Movies & TV Shows Dataset** using **Python**, **Pandas**, and **Matplotlib**. The objective is to extract meaningful insights from the dataset while demonstrating essential data analysis and data cleaning techniques.

The project includes data preprocessing, statistical analysis, visualization, and exporting a cleaned dataset for future use. The analysis script calculates several key metrics and generates visualizations to better understand Netflix's content library.

---

## 📂 Dataset

* **Dataset:** Netflix Movies and TV Shows
* **Format:** CSV
* **Columns include:**

  * Title
  * Type (Movie / TV Show)
  * Director
  * Cast
  * Country
  * Release Year
  * Rating
  * Duration
  * Genre
  * Description
  * Date Added

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib

---

## 📊 Analysis Performed

The project performs the following analyses:

* Count of Movies and TV Shows
* Distribution of Movies vs TV Shows (Pie Chart)
* Most Common Content Rating
* Year with the Highest Number of Releases
* Releases by Year (Bar Chart)
* Most Common Genres
* Most Common Country of Origin
* Top 5 Directors
* Movies vs TV Shows Trend by Release Year (Line Graph)
* Oldest Content Available on Netflix
* Average Movie Duration
* Top 10 Most Frequently Appearing Actors

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

* Removed unnecessary columns:

  * `description`
  * `date_added`
* Handled missing values where required.
* Created a cleaned version of the dataset for future analysis.
* Exported the cleaned dataset as:

```
cleaned_netflix_titles.csv
```

---

## 📈 Visualizations

The project generates the following visualizations:

* 📌 Pie Chart – Movies vs TV Shows
* 📌 Bar Chart – Number of Releases by Year
* 📌 Line Graph – Movies vs TV Shows Released Each Year

---

## 📁 Project Structure

```
Netflix-Data-Analysis/
│
├── netflix_titles.csv
├── cleaned_netflix_titles.csv
├── main.py
├── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Netflix-Data-Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Netflix-Data-Analysis
```

### 3. Install the required libraries

```bash
pip install pandas matplotlib
```

### 4. Run the project

```bash
python main.py
```

---

## 📌 Sample Insights

* Movies make up the majority of Netflix's catalog.
* The most common content rating can be identified using the dataset.
* Certain years saw a significant increase in Netflix content releases.
* The United States contributes the largest amount of content.
* A small number of directors and actors appear frequently across the platform.

---

## 🎯 Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Pandas Data Manipulation
* Statistical Analysis
* File Handling
* Python Programming

---

## 📚 Future Improvements

* Add interactive visualizations using Plotly or Seaborn.
* Perform sentiment analysis on movie descriptions.
* Build a Netflix recommendation system.
* Develop an interactive dashboard using Streamlit or Power BI.
* Create additional visualizations for genres, ratings, and countries.

⭐ If you found this project useful, feel free to star the repository!
