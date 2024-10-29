import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('/Users/venkatakrishna/Career/priya/dialy_learnings/python_tasks/Realworld_programs/repeted_callers/api_data.csv')

# Step 2: Define functions to manually extract 'phoneNumber' and 'target'
def extract_phone_number(event_str):
    try:
        # Find the position of 'phoneNumber' and extract the value
        phone_start = event_str.find('"phoneNumber":"') + len('"phoneNumber":"')
        phone_end = event_str.find('"', phone_start)
        phone_number = event_str[phone_start:phone_end]
        return phone_number
    except (ValueError, IndexError):
        return None  # Handle cases where 'phoneNumber' is not found

def extract_target(event_str):
    try:
        # Find the position of 'target' and extract the value
        target_start = event_str.find('"target":"') + len('"target":"')
        target_end = event_str.find('"', target_start)
        target_value = event_str[target_start:target_end]
        return target_value
    except (ValueError, IndexError):
        return None  # Handle cases where 'target' is not found

# Step 3: Apply each function to the 'events' column and create separate columns
df['Phone Number'] = df['event'].apply(extract_phone_number)
df['Target'] = df['event'].apply(extract_target)

# Step 4: Display the DataFrame with the extracted columns
#print(df[['Phone Number', 'Target']])
df['Phone Number'] = df['event'].apply(extract_phone_number)
df['Target'] = df['event'].apply(extract_target)

# grouped_data = df.groupby(['Phone Number', 'Target']).size().reset_index(name='Count')

# # Step 5: Save grouped data to CSV
# grouped_data.to_csv('grouped_phone_target_counts.csv', index=False)

# # Step 6: If you want just phone numbers and their total repetition count (irrespective of target)
# phone_counts = df['Phone Number'].value_counts().reset_index(name='Count')
# phone_counts.columns = ['Phone Number', 'Count']

# # Step 7: Save phone number counts to CSV
# phone_counts.to_csv('phone_number_counts.csv', index=False)

grouped_data = df.groupby(['Phone Number', 'Target']).size().reset_index(name='Count')

# Step 5: Save grouped data (Phone Number + Target + Count) to CSV
grouped_data.to_csv('grouped_phone_target_counts.csv', index=False)