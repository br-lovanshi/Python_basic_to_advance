class Stock:
    exchange = "BSE"  # assuming we have only one exchange

    def __init__(self, name, curr_price, sector, market_cap, one_year_returns, five_year_returns):
        self.__name = name
        self.__curr_price = curr_price
        self.__sector = sector
        self.__market_cap = market_cap
        self.__one_year_returns = one_year_returns
        self.__five_year_returns = five_year_returns

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_curr_price(self):
        return self.__curr_price

    def get_stock_info(self):
        print(f"Name: {self.__name} Curr prime: {self.__curr_price} Sector: {self.__sector} Market cap: {self.__market_cap} One year return: {self.__one_year_returns} Five year return: {self.__five_year_returns}")


stock = Stock("TCS", 5000, "IT", 1500000, 20, 100)

print(stock.get_name())
print(stock.exchange)
stock.set_name("Wipro")
stock.get_stock_info()


# Encapsulation: Binding a data into a single unit, so that no one can directly access/manipulate from outside the
# class, important for security
