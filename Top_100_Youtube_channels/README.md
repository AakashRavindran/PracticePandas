YouTube Channel Data Analysis
This project analyzes a dataset containing YouTube channel statistics, focusing on cleaning, transformation, and deriving insights such as the fastest growing channels, 
channels with the most subscribers per upload, and more.


Overview
This project takes a CSV file (YOUTUBE CHANNELS DATASET.csv) that contains information about various YouTube channels, including their upload counts, views, and subscriber count. The goal is to clean the data, transform it into a more usable form, and perform some simple analysis to derive key insights.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/youtube-channel-analysis.git
Navigate into the project directory:

bash
Copy code
cd youtube-channel-analysis
Install the required libraries using pip:

bash
Copy code
pip install -r requirements.txt
Note: You will need a Python environment with pandas installed.

Usage
Ensure that the YOUTUBE CHANNELS DATASET.csv file is available in the same directory as the script, or update the file path in the code.

Run the Python script:

bash
Copy code
python youtube_channel_analysis.py
The cleaned and analyzed data will be saved to a file called Fastest_growing_Youtube_channels_2024.csv.

Code Description
The Python script performs the following steps:

1. Data Loading
The dataset is loaded using pandas.read_csv() with the skipfooter option to remove any unwanted footer rows.

python
Copy code
channels = pd.read_csv("YOUTUBE CHANNELS DATASET.csv", skipfooter=1, engine="python")
2. Data Inspection
Basic inspection is done to understand the structure of the data using head(), tail(), and info() methods.

python
Copy code
channels.head()
channels.tail()
channels.info()
3. Data Transformation
Columns like Uploads and Views are cleaned by removing commas and converting them into integer types for better analysis.

python
Copy code
channels.Uploads = channels.Uploads.str.replace(",", "").astype("int")
channels.Views = channels.Views.str.replace(",", "").astype("int64")
4. Name Transformation
A function add_yt_to_name() is created to append "YouTube" to the usernames of official YouTube channels with 0 uploads (i.e., official channels that don't upload content).

python
Copy code
def add_yt_to_name(name):
    if not "youtube" in name.lower():
        return "Youtube "+ name
    else:
        return name
channels.loc[channels["Uploads"]==0, "Username"] = channels.loc[channels["Uploads"]==0,"Username"].apply(add_yt_to_name)
5. Handling Missing Data
Missing country information is filled with "Unknown" to prevent null values from interfering with analysis.

python
Copy code
channels['Country'] = channels["Country"].fillna("Unknown")
6. Data Type Transformation
The Subscribers column is cleaned by removing the 'M' (for millions), converting the values to float, and multiplying by 1 million for proper scaling.

python
Copy code
channels["Subscribers"] = channels.Subscribers.str.replace("M", "").astype("float")
channels.Subscribers = channels.Subscribers * 1e6
7. Sorting Data
The data is sorted by Subscribers to validate the ranking of channels.

python
Copy code
channels.sort_values("Subscribers", ascending=False)
Data Cleaning and Transformation
Removing commas in the Uploads and Views columns and converting them to appropriate data types (int and int64).
Handling missing values by filling NaN values in the Country column with "Unknown".
Converting the 'Subscribers' column to a numeric format and adjusting values from millions to actual subscriber counts.
Transforming channel names to add "YouTube" to official YouTube channels with zero uploads.
Analysis
The script performs the following analysis:

Subscribers per upload: A new column Subscribers_per_Upload is created to understand how many subscribers each channel has per upload. The data is sorted by this value to identify top-performing channels based on uploads.
Fastest growing channels: The script identifies the channels with the fastest growth by ranking the channels based on their Subscribers_per_Upload values.
Ranking: The final ranking of fastest-growing channels is stored in a new column called Fastest_growing_channel_rank.
Results
The cleaned data is saved to a new CSV file, which includes:

Updated channel names (with "YouTube" added where necessary).
Corrected and numeric data for columns like Subscribers, Uploads, and Views.
Additional metrics like Subscribers_per_Upload and Fastest_growing_channel_rank.
The resulting file is saved as Fastest_growing_Youtube_channels_2024.csv.
