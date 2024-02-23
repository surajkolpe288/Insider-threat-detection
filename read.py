import pandas as pd

# Load the CSV file into a DataFrame
email_data = pd.read_csv('Email_dataset.csv')

# Iterate over each row in the DataFrame
for index, row in email_data.iterrows():
    subject = row['Sub']
    sender = row['FROM']
    To = row['TO']
    # body = row['Body']
    uniq_id = row['Unique.id']
    Thr_NoThr = row['Thr(1) or No thr(0)']
    
    # Process the email (e.g., perform feature extraction)
    # Your code for feature extraction goes here
# email_data.head()
# email_data.describe()

 

print(email_data)