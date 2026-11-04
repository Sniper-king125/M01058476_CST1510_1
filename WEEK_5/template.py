"""
RECORD CHECK  -  my version
===========================

Name  :Travis chaula
Lane  :Cyber     (delete two)
Date  :11/4/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ==========================================================
# 1. CLASS
# ==========================================================

class Record:
    """Stores and checks an individual record."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialises a record with its label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns the status of the record."""
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= self.limit * 0.90:
            return "WARNING"
        else:
            return "OK"


# ==========================================================
# 2. LOAD RECORDS FROM A FILE
# ==========================================================

def load_records(path):
    """Reads records from a file and returns Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


records = load_records("records.txt")


# ==========================================================
# 3. OUTPUT REPORT
# ==========================================================

over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Label:  {record.label}")
    print(f"  Value:  {record.value}")
    print(f"  Limit:  {record.limit}")
    print(f"  Status: {record.status()}")

    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print()
print("TOTAL RECORDS OVER LIMIT:", over_limit_count)

