import pandas as pd
import ssl

#LINK: "https://en.wikipedia.org/wiki/Presidents_of_the_United_States"
#Wikipedia does not let me scrape their data without giving 'HTTP ERROR 403: Forbidden'

ssl._create_default_https_context = ssl._create_unverified_context

tables = pd.read_html("https://en.wikipedia.org/wiki/Presidents_of_the_United_States")

len(tables)
tables[1]
if __name__ == "__main__":
    print("Running scrapper two...")
