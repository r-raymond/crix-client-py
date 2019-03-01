# CRIX.io official client

**TODO**
* license and to setup.py
* all orders
* publish to pip

This official client of CRIX.io crypto exchange.

Environment requirements:

* python 3.5+
* requests 2.* 

For several operations like create/cancel orders you should
also be registered in the exchange and got BOT API token and secret.

To access historical you should get explicit permission by exchange support.

## Installation

* over pip: `pip install crix`
* manually: `pip install git+https://github.com/blockwise/crix-client-py.git#egg=crix`

## Sample usage


### Unauthorized (public) access


```python
import crix

client = crix.Client(env='prod')

# get all symbols
for symbol in client.fetch_markets():
    print(symbol)

# get some order book
depth = client.fetch_order_book('BTC_BCH')
print(depth)
```


### Authorized (clients-only) access

**BOT API token and secret are required**



```python
import crix
from crix.models import NewOrder

client = crix.AuthorizedClient(
    env='prod',
    token='xxyyzz',
    secret='aabbcc'
) # replace token and secret value for your personal API credentials


# list all open orders
for order in client.fetch_open_orders('BTC_BCH'):
    print(order)
    
# prepare order
new_order = NewOrder.market('BTC_BCH', is_buy=True, quantity=0.1) # or use NewOrder constructor
# place order
order = client.create_order(new_order)
print(order)
```