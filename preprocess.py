import pandas as pd

# Load CSV with low_memory=False to avoid mixed type warnings
df = pd.read_csv("british_museum_object.csv", low_memory=False)

# Clean 'acquisition_date'
df['acquisition_date'] = pd.to_numeric(df['acquisition_date'], errors='coerce')

# Drop rows with missing acquisition_date and make a copy to avoid SettingWithCopyWarning
df_clean = df.dropna(subset=['acquisition_date']).copy()

# Convert acquisition_date to integer
df_clean.loc[:, 'acquisition_date'] = df_clean['acquisition_date'].astype(int)

# --- Option 1: Aggregate by year ---
acquisition_per_year = df_clean.groupby(['acquisition_date', 'aqusition_way'], dropna=False).size().reset_index(name='count')

# Save CSV
acquisition_per_year.to_csv("acquisition_per_year.csv", index=False)

# --- Option 2: Aggregate by decade ---
df_clean.loc[:, 'acquisition_decade'] = (df_clean['acquisition_date'] // 10) * 10
acquisition_per_decade = df_clean.groupby(['acquisition_decade', 'aqusition_way'], dropna=False).size().reset_index(name='count')

# Save CSV
acquisition_per_decade.to_csv("acquisition_per_decade.csv", index=False)
