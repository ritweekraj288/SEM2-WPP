# # import pandas as pd
# # data = {
# # "date": ["2023-01-15", "2023-01-20", "2023-02-10", "2023-02-15", "2023-01-15"],
# # "artist": ["Artist A", "Artist B", "Artist A", "Artist C", "Artist A"],
# # "venue": ["Venue X", "Venue Y", "Venue X", "Venue Z", "Venue Z"]
# # }
# # concerts = pd.DataFrame(data)concerts["year_month"] = pd.to_datetime(concerts["date"]).dt.to_period("M")
# # artists = pd.Series(concerts["artist"].unique())
# # venues = pd.Series(concerts["venue"].unique())
# # artist_venue_pairs = [(artist, venue) for artist in artists for venue in venues]
# # wide_table = pd.DataFrame({"year_month": concerts["year_month"].unique()})
# # wide_table["year_month"] = wide_table["year_month"].astype(str)
# # for artist, venue in artist_venue_pairs:
# # count = concerts[(concerts["artist"] == artist) & (concerts["venue"] ==
# # venue)].groupby("year_month").size()
# # wide_table[f"{artist}, {venue}"] =
# # wide_table["year_month"].map(count).fillna(0).astype(int)
# # print(wide_table)

# import pandas as pd

# # Sample dataset
# data = {
#     "artist": ["Arijit Singh", "B Praak", "Arijit Singh", "Honey Singh", "B Praak", "Arijit Singh", "Honey Singh", "Arijit Singh", "B Praak"],
#     "venue": ["Surat", "Mumbai", "Pune", "Pune", "Mumbai", "Surat", "Pune", "Mumbai", "Surat"],
#     "date": ["2024-01-15", "2024-01-22", "2024-02-10", "2024-02-18","2024-03-05", "2024-03-15", "2024-04-10", "2024-04-15", "2024-04-20"]
# }

# # Convert to DataFrame
# df = pd.DataFrame(data)

# # Convert 'date' column to datetime and extract 'year-month'
# df["date"] = pd.to_datetime(df["date"])
# df["year_month"] = df["date"].dt.to_period("M")

# # Count concerts per (artist, venue, year-month)
# concert_counts = df.groupby(["year_month", "artist", "venue"]).size().reset_index(name="count")

# # Pivot table to wide format
# wide_table = concert_counts.pivot(index="year_month", columns=["artist", "venue"], values="count").fillna(0)

# # Flatten column names
# wide_table.columns = [f"{a}_{v}" for a, v in wide_table.columns]
# wide_table.reset_index(inplace=True)

# # Print result
# print(wide_table)

import pandas as pd

# Sample dataset
data = {
    "artist": ["Arijit Singh", "B Praak", "Arijit Singh", "Honey Singh", "B Praak", "Arijit Singh", "Honey Singh", "Arijit Singh", "B Praak"],
    "venue": ["Surat", "Mumbai", "Pune", "Pune", "Mumbai", "Surat", "Pune", "Mumbai", "Surat"],
    "date": ["2024-01-15", "2024-01-22", "2024-02-10", "2024-02-18","2024-03-05", "2024-03-15", "2024-04-10", "2024-04-15", "2024-04-20"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'date' column to datetime and extract 'year-month'
df["date"] = pd.to_datetime(df["date"])
df["year_month"] = df["date"].dt.to_period("M")

# Count concerts per (artist, venue, year-month)
concert_counts = df.groupby(["year_month", "artist", "venue"]).size().reset_index(name="count")

# Pivot table to wide format
wide_table = concert_counts.pivot(index="year_month", columns=["artist", "venue"], values="count").fillna(0)

# Flatten column names
wide_table.columns = [f"{a}_{v}" for a, v in wide_table.columns]
wide_table.reset_index(inplace=True)

# Print result
print(wide_table)