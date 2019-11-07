from linenotify import Notify
from stock_price import get_quote

token = ''

stock_no = '2330'
quote = "{}目前股價為{}元！".format(stock_no, get_quote(stock_no))
print(quote)
Notify(token, quote)
