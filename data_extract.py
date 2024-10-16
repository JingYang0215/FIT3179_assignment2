import pandas as pd

# Load the CSV file
df = pd.read_csv('CB-Insights_Global-Unicorn-Club_2024_split.csv')

# Extract all investors from the 'Select Investors' column and count their occurrences
investors = df['Select Investors'].str.split(',').explode().str.strip()
top_investors = investors.value_counts().head(10)
print(top_investors)

# Create a DataFrame for the top 10 investors
top_investors_df = pd.DataFrame({
    'Investor': top_investors.index,
    'Count': top_investors.values
})

# Save the top investors DataFrame to a CSV file for visualization
top_investors_df.to_csv('top_investors.csv', index=False)
