# Student Name: He Zhenkai
# Admin Number: 204304Z
# Tutorial Group: IT2154 Group 4


class Item:
    def __init__(self, item_index, item_desc, item_price, item_stock):
        self.__item_index = item_index
        self.__item_desc = item_desc
        self.__item_price = item_price
        self.__item_stock = item_stock

    # Item's index Getters / Accessors
    @property
    def itemIndex(self):
        return self.__item_index

    @itemIndex.setter
    def itemIndex(self, value):
        self.__item_index = value

    # Item's description Getters / Accessors
    @property
    def itemDescription(self):
        return self.__item_desc

    @itemDescription.setter
    def itemDescription(self, value):
        self.__item_desc = value

    # Item's price Getters / Accessors
    @property
    def itemPrice(self):
        return self.__item_price

    @itemPrice.setter
    def itemPrice(self, value):
        self.__item_price = value

    # Item's stock Getters / Accessors
    @property
    def itemStock(self):
        return self.__item_stock

    @itemStock.setter
    def itemStock(self, value):
        self.__item_stock = value

