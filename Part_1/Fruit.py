# Student Name: He Zhenkai
# Admin Number: 204304Z
# Tutorial Group: IT2154 Group 4

from Part_1.Item import Item


class Fruit(Item):
    def __init__(self, item_index, item_name, item_desc, item_price, item_stock, item_supplier, item_rating=1):
        self.__item_name = item_name
        self.__item_supplier = item_supplier
        self.__item_rating = item_rating
        super().__init__(item_index, item_desc, item_price, item_stock)

    # Item's name Getters / Accessors
    @property
    def itemName(self):
        return self.__item_name

    @itemName.setter
    def itemName(self, value):
        self.__item_name = value

    # Item's supplier Getters / Accessors
    @property
    def itemSupplier(self):
        return self.__item_supplier

    @itemSupplier.setter
    def itemSupplier(self, value):
        self.__item_supplier = value

    # Item's rating Getters / Accessors
    @property
    def itemRating(self):
        return self.__item_rating

    @itemRating.setter
    def itemRating(self, value):
        self.__item_rating = value

    def __str__(self):
        return '----------------------------------------\n' \
               'Index: {}\nName: {}\nDescription: {}\nPrice: ${}\nStock: {}\nSupplier: {}\nRating: {}\n' \
               '----------------------------------------'.format(
                self.itemIndex,
                self.itemName,
                self.itemDescription,
                self.itemPrice,
                self.itemStock,
                self.itemSupplier,
                self.itemRating
        )
