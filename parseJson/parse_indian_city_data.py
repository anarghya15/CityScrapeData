import pandas as pd
import functools
import json

# Assuming your JSON file is named "data.json"
with open("..\extractedData\indian_city_data.json", "r", encoding="utf-8") as f:
  data = json.load(f)

# Concatenate paragraphs with a newline character
def concatenate_paragraphs(paragraphs):
  return " ".join(paragraphs)

# Apply the function to the "paragraphs" column
data = [{"city": entry["city"], "paragraphs": concatenate_paragraphs(entry["paragraphs"]), "image": entry["image_url"]} for entry in data]

# for entry in data:
#     print(entry["city"])
#     print(entry["paragraphs"])

# Create a pandas dataframe
df = pd.DataFrame(data)

# Save the dataframe as a CSV file
df.to_excel("..\extractedData\indian_city_data.xlsx", index=False)  # Set index=False to avoid an extra index column
