import pandas as pd

url = r'https://bnr.ro/Cursul-de-schimb--7372.aspx'
tables = pd.read_html(url) # Returns list of all tables on page
# sp500_table = tables[0] # Select table of interest
print(tables[0])