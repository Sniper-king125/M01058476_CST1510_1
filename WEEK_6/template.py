"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


import pandas as pd
import matplotlib.pyplot as plt

# ====================================================================
# LOAD
# 1. Read the CSV file
df = pd.read_csv("records.csv")

# ====================================================================
# PROCESS
# 2. Calculate the percentage for each record
df["percent"] = (df["value"] / df["limit"]) * 100

# Create a status column using a lambda function
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100
    else "WARNING" if x >= 90
    else "OK"
)

# ====================================================================
# OUTPUT
# 3. Print the complete DataFrame
print("ALL RECORDS:")
print(df)

# Show only records that are not OK
print("\nRECORDS THAT NEED ATTENTION:")
print(df[df["status"] != "OK"])

# Count the number of records in each status
print("\nSTATUS COUNTS:")
print(df.groupby("status").size())

# Save the full DataFrame to a new CSV file
df.to_csv("output.csv", index=False)

# Create a bar chart showing the status counts
df["status"].value_counts().plot(kind="bar")

plt.title("Record Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("status_chart.png")

print("\nFiles saved successfully!")

