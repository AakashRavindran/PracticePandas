import pandas as pd
channels = pd.read_csv("YOUTUBE CHANNELS DATASET.csv", skipfooter = 1, engine = "python")
channels.head()
channels.tail()
channels.info()

# From the above info method , We could see that some of the columns can be changed to numeric types for better analysis

channels.Uploads = channels.Uploads.str.replace(",", "",)
channels.Uploads = channels.Uploads.astype("int")

channels.Views = channels.Views.str.replace(",", "",)
channels.Views = channels.Views.astype("int64")

# Below function was created to Add the String "Youtube" to Youtube's official channels. these channels have 0 videos uploaded 

def add_yt_to_name(name):
    if not "youtube" in name.lower():
        return "Youtube "+ name
    else:
        return name    

channels.loc[channels["Uploads"]==0, "Username"] = channels.loc[channels["Uploads"]==0,"Username"].apply(add_yt_to_name)

# Verify the above 

channels.loc[channels.Username.str.contains("Youtube")]

# Data Cleaning 

# Check for Duplicates 
channels.loc[channels.duplicated()]

channels['Country'] = channels["Country"].fillna("Unknown")

# Changing the Subscribers field to numeric / float data type

channels["Subscribers"] = channels.Subscribers.str.replace("M","") 
channels["Subscribers"] = channels.Subscribers.astype("float")
channels.Subscribers = channels.Subscribers * 1e6

# Now sort by Subs to Validate the Ranking

channels.sort_values("Subscribers", ascending = False)

# Perform some Data Analysis

# Get the Channels with the most Subscribers per upload

channels["Subscribers_per_Upload"] = channels["Subscribers"] / channels["Uploads"]

channels.sort_values(by = "Subscribers_per_Upload", inplace = True )

# Get the fastest growing channel 

channels.sort_values(by = "Subscribers_per_Upload", inplace = True , ascending = False)

channels["Fastest_growing_channel_rank"] = channels.Subscribers_per_Upload.rank(ascending = False)

channels.sort_values(by = "Subscribers_per_Upload", inplace = True , ascending = False)

channels.reset_index(inplace = True, drop = True)

# Export cleaned and sorted data

channels.to_csv("Fastest_growing_Youtube_channels_2024")
