# ============================================================
# Preprocessing Script for British Museum Data Visualization
# Cleans acquisition year and culture/period data for Vega-Lite
# ============================================================

import pandas as pd

# -----------------------------
# Step 1: Load and clean dataset
# -----------------------------
df = pd.read_csv("./data/british_museum_object.csv")

# Convert acquisition_date to numeric (ignore text like 'Unknown')
df["acquisition_year"] = pd.to_numeric(df["acquisition_date"], errors="coerce")

# Keep only valid years
df = df[(df["acquisition_year"].notna()) & (df["acquisition_year"] > 1600) & (df["acquisition_year"] <= 2025)]

# Clean 'Cultures/periods' column
df["Cultures/periods"] = df["Cultures/periods"].astype(str).str.strip()

# Drop NA, "None", or blank cultures before processing
df = df[
    (df["Cultures/periods"].notna()) &
    (~df["Cultures/periods"].isin(["None", "Unknown", "", " ","nan"]))
]

# Create a 'decade' column
df["decade"] = (df["acquisition_year"] // 10 * 10).astype(int)

print(f"✅ Loaded {len(df)} valid records after cleaning.")


# ----------------------------------
# Step 2: Aggregate by decade/culture
# ----------------------------------
df_grouped = (
    df.groupby(["decade", "Cultures/periods"])
    .size()
    .reset_index(name="count")
)

# Total objects per culture across all decades
culture_totals = (
    df_grouped.groupby("Cultures/periods")["count"]
    .sum()
    .sort_values(ascending=False)
)

# Pick top 10 most frequent cultures
top_cultures = culture_totals.head(10).index.tolist()

# Label less frequent ones as "Other"
df_grouped["filtered_culture"] = df_grouped["Cultures/periods"].apply(
    lambda x: x if x in top_cultures else "Other"
)

# Re-aggregate (combine all "Other")
df_final = (
    df_grouped.groupby(["decade", "filtered_culture"])["count"]
    .sum()
    .reset_index()
    .sort_values("decade")
)

# ---------------------------------------
# Step 3: Compute percentage per decade
# ---------------------------------------
# Calculate total per decade for normalization
total_per_decade = df_final.groupby("decade")["count"].transform("sum")
df_final["percentage"] = (df_final["count"] / total_per_decade * 100).round(2)

# ---------------------------------------
# Step 4: Save cleaned data
# ---------------------------------------
output_file = "./data/british_museum_culture_trends.csv"
df_final.to_csv(output_file, index=False)

print(f"💾 Saved preprocessed dataset to '{output_file}'")
print(df_final.head(15))
