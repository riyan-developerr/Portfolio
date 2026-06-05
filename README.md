I have made this repository to showcase my learning and skills that i will learn in Summer Vacations 
Today I have studied about api(application programming interface) they are intermmediators between two software or applications and their main goal is to ensure security and communication.
There are 3 types of apis
FRAMEWORK/LIBRARY APIS
WEB APIS
OPERATING SYSTEM APIS  

#FRAMEWORK APIS:
TODAY i used framework api of openai and did sentiment analysis.It is very useful in understanding the emotions in text.we can analyze the views and opinions of people and even change their views by changing the envirmnent around them.


date:02-06-2026 (Tuesday)
today i am finishing work.Today i learned about hugging face where models are availble.we can use them and build amazing things.Just like a Company with spcialized workers for all filds,just pick the models related to you.
I generated image using openai model,then did text-classification,sentiment analysis and finally text-generation using huggingface models especially Qwen/Qwen3-0.6B
Well done Riyan I am proud of your hardwork today.Inshallah you will rech your goals and targets.OH I WILL SURELY NO NEED OT WORRY FRIEND...

## Wednesday, June 3, 2026

Today, I continued my summer vacation learning journey by practicing Hugging Face and AI model usage in Python. I explored different types of NLP models, including text classification, zero-shot classification, question-answering models, and generative text models. I learned the difference between extractive question-answering models, which copy answers from context, and generative models, which create new text in their own words.

I also practiced working with real AI libraries and solved multiple coding issues. I tested the `deepset/roberta-base-squad2` question-answering model, understood how GPT-2 generates text from prompts, experimented with Kokoro text-to-speech voices, and learned how to adjust voice style using different voices and speed settings. I also worked with object detection using the YOLOS model and learned how to fix outdated imports by replacing `YolosFeatureExtractor` with modern tools like `AutoImageProcessor` or the object-detection pipeline.

Another important part of today’s work was experimenting with image generation using Stable Diffusion in Google Colab. I learned how to install required libraries, enable T4 GPU, fix package version conflicts between `diffusers` and `transformers`, generate an image from a prompt, display it in Colab, and save the final output. Finally, I planned how to move my Colab notebook into VS Code and push my work to GitHub so I can keep a proper record of my learning progress.

**Encouraging message:** Every small experiment today is building the foundation for the AI expert I want to become.

# Thursday, June 4, 2026

## Daily Learning Record — Pandas Data Exploration and Preprocessing

Today, I practiced basic data analysis and preprocessing using Python and Pandas in Google Colab. I worked with a student performance dataset and learned how to load, inspect, understand, and prepare data for future machine learning tasks.

## Work Completed

I started by installing and importing the required library, `pandas`, and then loaded the dataset using `pd.read_csv()`. After loading the dataset, I used `df.head()` to view the first few rows and understand the structure of the data.

I checked the size of the dataset using `df.shape`, which showed that the dataset contains 100 rows and 10 columns. This helped me understand the number of records and features available in the dataset.

I explored the data types of each column using `df.dtypes`. I learned which columns were numerical and which columns were categorical, such as the `gender` column.

I used `df.tail(10)` to view the last 10 rows of the dataset. This helped me confirm that the data was loaded properly from start to end.

I used `df.info()` to get a complete summary of the dataset, including column names, non-null counts, data types, and memory usage. This helped me understand the overall health and structure of the dataset.

I used `df.describe()` to generate statistical information about the numerical columns, including mean, minimum, maximum, standard deviation, and quartile values. This gave me a better understanding of the distribution of values in the dataset.

I checked for missing values using `df.isnull().sum()`. The result showed that there were no missing values in any column, which means the dataset was clean in terms of null values.

Finally, I practiced categorical data preprocessing by using `pd.get_dummies()` on the `gender` column. This converted the gender category into numerical columns, `gender_Female` and `gender_Male`, making the dataset more suitable for machine learning models.

## Concepts Practiced

* Installing and importing Pandas
* Reading CSV files with `pd.read_csv()`
* Viewing first and last rows using `head()` and `tail()`
* Checking dataset shape
* Checking column data types
* Understanding dataset summary with `info()`
* Generating statistical summary with `describe()`
* Checking missing values with `isnull().sum()`
* Encoding categorical columns using `pd.get_dummies()`

## Key Learning

Today, I learned that before applying machine learning models, it is important to first understand the dataset properly. Data exploration helps identify column types, missing values, value ranges, and preprocessing needs. I also learned that categorical columns like gender must be converted into numerical form before they can be used by most machine learning algorithms.

## Encouraging Message

Every dataset I explore is making me stronger in data preprocessing and bringing me one step closer to becoming skilled in machine learning.

# Day 5 — Friday, June 5, 2026

## Summer AI Learning Journey

Today I focused on **Exploratory Data Analysis (EDA)** and learned how to inspect a dataset before applying machine learning or deeper analysis.

## What I Learned Today

### 1. Checking Missing Values

I learned how to find missing values in a dataset using:

```python
df.isnull().sum()
```

This shows the total number of missing values in each column.

I also learned how to calculate the percentage of missing values:

```python
df.isnull().mean() * 100
```

This helps me understand how serious the missing value problem is in each column.

---

### 2. Checking Duplicate Rows

I learned how to count duplicate rows:

```python
df.duplicated().sum()
```

I also learned how to display the actual duplicate rows:

```python
df[df.duplicated()]
```

This is useful because duplicate data can affect the accuracy of analysis and machine learning models.

---

### 3. Checking Unique Values

I learned how to check the number of unique values in each column:

```python
df.nunique()
```

This helps identify categorical columns, ID columns, and columns with too many or too few unique values.

---

### 4. Grouping Data for Insights

I practiced grouping the data by disease:

```python
df.groupby("Disease").agg({
    "Age": "mean",
    "Severity_Score": "mean",
    "Hospital_Days": "mean",
    "Treatment_Cost_USD": "mean"
}).sort_values("Severity_Score", ascending=False)
```

This helped me understand how to compare diseases based on:

* Average patient age
* Average severity score
* Average hospital stay
* Average treatment cost

I also learned that instead of writing `"mean"` again and again, I can write a shorter version:

```python
df.groupby("Disease")[[
    "Age",
    "Severity_Score",
    "Hospital_Days",
    "Treatment_Cost_USD"
]].mean().sort_values("Severity_Score", ascending=False)
```

---

## Key Takeaway

Today I understood that EDA is not just about running commands. It is about asking questions from the data, such as:

* Are there missing values?
* Are there duplicate rows?
* Which columns are categorical?
* Which diseases are more severe?
* Which diseases cost more to treat?
* Which diseases require longer hospital stays?

## Progress Reflection

Today’s work improved my understanding of how data analysts explore datasets before building models. I am becoming more comfortable with pandas functions and slowly learning how to extract useful insights from raw data.

## Encouraging Message

Small daily progress compounds into real skill — keep showing up and keep building.

