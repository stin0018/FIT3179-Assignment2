import pandas as pd

# --- 1️⃣ Load data ---
museums = pd.read_csv("museums_per_LAD_updated.csv")
cleaned = pd.read_csv("cleaned_matched_LADs.csv", on_bad_lines='skip', engine='python')

# --- 2️⃣ Replace LAD_name using cleaned file based on LAD_code ---
museums = museums.merge(
    cleaned[['LAD_code', 'LAD_name']],
    on='LAD_code',
    how='left',
    suffixes=('', '_cleaned')
)

# Use cleaned LAD_name when available
museums['LAD_name'] = museums['LAD_name_cleaned'].combine_first(museums['LAD_name'])
museums = museums.drop(columns=['LAD_name_cleaned'])

# --- 3️⃣ Remove rows where LAD_name is NaN ---
museums = museums.dropna(subset=['LAD_name'])

# --- 4️⃣ Convert numeric columns safely ---
for col in ['Counts', 'Population']:
    museums[col] = pd.to_numeric(museums[col], errors='coerce')

# --- 5️⃣ Combine rows with same LAD_name (ignore LAD_code) ---
grouped = museums.groupby('LAD_name', as_index=False).agg({
    'Counts': 'sum',
    'Population': 'sum'
})

# --- 6️⃣ Recalculate metrics ---
grouped['People_per_museum'] = grouped['Population'] / grouped['Counts']
grouped['Museums_per_100k'] = (grouped['Counts'] / grouped['Population']) * 100000

# --- 7️⃣ Reorder columns for clarity ---
grouped = grouped[['LAD_name', 'Counts', 'People_per_museum', 'Museums_per_100k', 'Population']]

# --- 8️⃣ Save final output ---
grouped.to_csv("museums_per_LAD_final.csv", index=False)

print("✅ Finished cleaning and merging by LAD_name.")
print("💾 Saved as: museums_per_LAD_final.csv")
