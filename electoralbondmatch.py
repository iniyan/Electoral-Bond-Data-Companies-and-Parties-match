import pandas as pd

# Load the data from the CSV file into a Pandas DataFrame
df = pd.read_csv("ebdata.csv")

# Remove commas from the 'Denominations' column and convert it to integers
df['Denominations'] = df['Denominations'].str.replace(',', '').astype(int)

# Convert bond number columns to strings, removing ".0" suffix
df['Company Bond Number'] = df['Company Bond Number'].fillna('').astype(str).str.rstrip('.0')
df['Party Bond Number'] = df['Party Bond Number'].fillna('').astype(str).str.rstrip('.0')

# Group the data by 'Company Name' and 'Party Name' and sum up the 'Denominations' for companies' donations to parties
donation_summary = df.groupby(['Company Name', 'Party Name']).agg({'Denominations': 'sum', 'Company Bond Number': ','.join, 'Party Bond Number': ','.join}).reset_index()

# Optionally, you can rename the columns for clarity
donation_summary.columns = ['Company Name', 'Party Name', 'Total Donations', 'Company Bond Numbers', 'Party Bond Numbers']

# Save the summary for companies' donations to parties to a new CSV file
donation_summary.to_csv("companies_donation_summary.csv", index=False)

# Group the data by 'Party Name' and 'Company Name' and sum up the 'Denominations' for parties' donations from companies
party_donations_summary = df.groupby(['Party Name', 'Company Name']).agg({'Denominations': 'sum', 'Party Bond Number': ','.join, 'Company Bond Number': ','.join}).reset_index()

# Optionally, you can rename the columns for clarity
party_donations_summary.columns = ['Party Name', 'Company Name', 'Total Donations', 'Party Bond Numbers', 'Company Bond Numbers']

# Save the summary for parties' donations from companies to a new CSV file
party_donations_summary.to_csv("party_donations_summary.csv", index=False)
