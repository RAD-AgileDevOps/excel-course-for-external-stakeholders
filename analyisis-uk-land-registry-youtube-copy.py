'''
Forensic Analysis of UK Land Registry Data
Systems Architect: Roger De Four (ex-ACCA/CAT qualified)
source: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads#single-file
Date: 2026-05-19
Project: Corrected Forensic Bridge for Large-Scale Property Transactions
'''

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text

# 1. Establish SQLAlchemy Engine with explicit Psycopg3 driver
# Updated URI protocol: postgresql+psycopg://  note: - remove square brackets and replace with your actual password and database name
connection_uri = "postgresql+psycopg://postgres:[ENTER YOUR PASSWORD HERE - remove square brackets]@localhost/[ENTER YOUR DATABASE NAME HERE]"
engine = create_engine(connection_uri)

# 2. Define High-Velocity SQL Query
query = '''
SELECT 
    transaction_id, 
    transfer_date, 
    price, 
    property_type,
    town_city, 
    district, 
    county
FROM public.uk_land_registry_price_paid 
WHERE COUNTY LIKE 'G%'
ORDER BY transaction_id ASC   
LIMIT 30 OFFSET 10000;
'''

# 3. Secure Data Ingestion via explicit Connection Context
try:
    with engine.connect() as conn:
        # Using text() resolves the immutabledict sequence error in SQLAlchemy 2.0
        df = pd.read_sql(text(query), conn)
    print("Database connection successful via SQLAlchemy Context.")
except Exception as e:
    print(f"Architectural Failure: {e}")
    exit()

# 4. Stakeholder Visualization Engineering
plt.style.use('dark_background') 
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the data with brand-consistent gold accents
ax.bar(df['town_city'], df['price'], color='#c8a96e', label='Property Sale Price')

# Labelling for Stakeholder Clarity
ax.set_title('UK Land Registry: Property Price Distribution by Town (County G%)', 
             fontsize=16, fontweight='bold', color='#c8a96e', pad=20)
ax.set_xlabel('Town / City (Geographic Identifier)', fontsize=12, labelpad=10)
ax.set_ylabel('Sale Price (£) - Forensic Valuation', fontsize=12, labelpad=10)

# Formatting X-axis for readability
plt.xticks(rotation=45, ha='right')

# Adding Legend and Grid for precise price analysis
ax.legend(loc='upper right', frameon=True, facecolor='#0a0a0f', edgecolor='#c8a96e')
ax.grid(axis='y', linestyle='--', alpha=0.2)

plt.tight_layout()

# 5. Output Verification
print("Dataset Verification (First 5 Forensic Rows):")
print(df.head())

plt.show()