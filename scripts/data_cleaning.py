import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw_data.csv")

print("Initial Shape:", df.shape)

# Remove unnecessary columns if they exist
cols_to_drop = ["Unnamed: 0", "id"]
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Handle missing values
if "arrival_delay_in_minutes" in df.columns:
    df["arrival_delay_in_minutes"] = df[
        "arrival_delay_in_minutes"
    ].fillna(df["arrival_delay_in_minutes"].median())

# Convert satisfaction to numeric
if "satisfaction" in df.columns:
    df["satisfaction"] = df["satisfaction"].map({
        "satisfied": 1,
        "neutral or dissatisfied": 0
    })

# Remove duplicates
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("../data/cleaned_data.csv", index=False)

print("✅ Cleaned dataset saved.")