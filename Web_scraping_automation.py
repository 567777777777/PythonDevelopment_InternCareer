import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Make the request to the BBC News website
response = requests.get("https://www.bbc.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# Find all heading elements
headline_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')

# Generate a timestamp for the output file name
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Create the output file name with the timestamp
output_file = f'bbc_news_headlines_{timestamp}.csv'

# Extract headlines
headlines = []
for headline_element in headline_elements:
    # Extract headline text
    headline_text = headline_element.text.strip()
    # Append the data to the headlines list
    headlines.append({'Headline': headline_text})

# Create a DataFrame from the headlines list
df = pd.DataFrame(headlines)

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)

# Print a message indicating the successful execution of the code
print(f"Headlines have been scraped and saved to {output_file}")

# Automation Process:
# - This script automates the process of scraping headlines from the BBC News website.
# - It utilizes the requests library to make an HTTP request to the BBC News website.
# - BeautifulSoup is used to parse the HTML content of the webpage and extract headline elements.
# - The script then generates a timestamp to include in the output file name for versioning and tracking purposes.
# - It extracts the text content of each headline element and appends it to a list.
# - The list of headlines is converted into a pandas DataFrame for easy manipulation.
# - Finally, the DataFrame is saved to a CSV file with the dynamically generated filename.
# - A message is printed to confirm the successful execution of the automation process.
