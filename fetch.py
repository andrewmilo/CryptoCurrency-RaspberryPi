from coinmarketcap import Market
import matplotlib.pyplot as plt

coinmarketcap = Market()

AMOUNT = 10
data = coinmarketcap.ticker()[:AMOUNT]
data = sorted(data, key=lambda k: k['price_usd'])
print data
fig, ax = plt.subplots()
# rects1 = ax.bar(ind, x['name'] for x in data], width, color='r', yerr=men_std)

ax.set_ylabel('Price (USD)')
ax.set_title("Today's Cryptocurrency Prices")
ax.set_xticks(range(len(data)))
ax.set_xticklabels([x['name'] for x in data])

# for i in xrange(len(data)):
ax.bar(range(len(data)), [x['price_usd'] for x in data], .1)

# plt.plot( [x['name'] for x in data], [x['price_usd'] for x in data] )
plt.show()