# Student Name: He Zhenkai
# Admin Number: 204304Z
# Tutorial Group: IT2154 Group 4


def DrawMenu():
    print("\nPlease Select One Of The Following Options! (Stock Inventory)")
    print("=============================================================")
    print('|1. Add item                                                |')
    print('|2. Update item                                             |')
    print('|3. Remove items                                            |')
    print('|4. Display items                                           |')
    print('|5. Sort items                                              |')
    print('|6. Search items                                            |')
    print('|7. Exit Application                                        |')
    print("=============================================================")


def ReadLine(string=''):
    return input(string)


def WriteLine(string=''):
    print(string)


def PrintSuccess(string):
    print("{}{}{}".format('\x1b[5;30;42m', string, '\x1b[0m'))


def PrintError(string):
    print("{}{}{}".format('\x1b[2;30;41m', string, '\x1b[0m'))


def AskInfo(aIndex, aName, aDesc, aPrice, aStock, aSupplier, aRating):
    index = 1
    name = ''
    description = ''
    price = 0
    stock = 0
    supplier = ''
    rating = 1

    if aIndex:
        index = int(ReadLine("Enter the item's index: "))

    if aName:
        name = ReadLine("Enter the item's name: ")

    if aDesc:
        description = ReadLine("Enter the item's description: ")

    if aPrice:
        price = float(ReadLine("Enter the item's price: "))

    if aStock:
        stock = int(ReadLine("Enter the item's stock: "))

    if aSupplier:
        supplier = ReadLine("Enter the item's supplier: ")

    if aRating:
        rating = float(ReadLine("Enter the item's rating: "))

    return {'index': index, 'name': name, 'desc': description, 'price': price, 'stock': stock, 'supplier': supplier, 'rating': rating}
