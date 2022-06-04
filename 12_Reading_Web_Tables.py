import pandas as pd

exchangeRateDF = pd.read_html("https://www.x-rates.com/table/?from=USD&amount=1")[1]
print(exchangeRateDF)
exchangeRateDF.to_excel("Data/ExchangeRates.xlsx", index=False)

