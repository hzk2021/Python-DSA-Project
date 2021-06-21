# Student Name: He Zhenkai
# Admin Number: 204304Z
# Tutorial Group: IT2154 Group 4

from Part_1.Utility import Console
from Part_1.Fruit import Fruit
import math

# Item dictionary for storing (temp)
Items = {}


# Add item into dictionary
def AddItem():
    Info = Console.AskInfo(False, True, True, True, True, True, True)

    f = Fruit(len(Items),
              Info['name'], Info['desc'],
              Info['price'], Info['stock'],
              Info['supplier'],
              Info['rating'])
    Items[f.itemIndex] = f

    Console.PrintSuccess("{} fruit has been added to index {}".format(f.itemName, f.itemIndex))


# Update item in the dictionary
def UpdateItem():
    Info = Console.AskInfo(True, False, False, False, False, False, False)

    itemIndex = Info['index']
    if itemIndex in Items:
        Info = Console.AskInfo(False, True, True, True, True, True, True)
        f = Fruit(itemIndex,
                  Info['name'], Info['desc'],
                  Info['price'], Info['stock'],
                  Info['supplier'],
                  Info['rating'])
        Items[f.itemIndex] = f
        Console.PrintSuccess("Fruit with index {} has been updated".format(f.itemIndex))
    else:
        Console.PrintError('Fruit with index {} is not found'.format(itemIndex))


# Delete item from dictionary
def RemoveItem():
    global Items
    Info = Console.AskInfo(True, False, False, False, False, False, False)

    itemIndex = Info['index']
    for i in range(len(Items)):
        if Items[i].itemIndex == itemIndex:
            Items.pop(i)

            # Reorder the dictionary indices. In this case, Items.values are the stored objects
            tempDict = {index: key for index, key in enumerate(Items.values())}
            Items = tempDict

            return Console.PrintSuccess("Fruit with index {} has been deleted".format(itemIndex))

    Console.PrintError('Fruit with index {} is not found'.format(itemIndex))


# Display all items in the dictionary
def DisplayItems():
    itemCount = len(Items)
    if itemCount > 0:
        for item in Items:
            print(Items[item])
    else:
        print('No fruits in the dictionary')


# Ask for which sorting algorithm to use
def SortItem():
    typeOfSort = int(Console.ReadLine("(1 for Selection Sort) || (2 for Insertion Sort) || (3 for Bubble Sort): "))
    if typeOfSort == 1:
        SelectionSort()
    elif typeOfSort == 2:
        InsertionSort()
    elif typeOfSort == 3:
        BubbleSort()
    else:
        return Console.PrintError("Not a valid sort option.")


# Sort items using Selection Sort
def SelectionSort():
    dictLength = len(Items)

    if dictLength > 0:
        for i in range(dictLength - 1):
            smallestIndex = i
            for j in range(i + 1, dictLength):
                if Items[i].itemStock > Items[j].itemStock:
                    smallestIndex = j

            if smallestIndex != i:
                tmp = Items[i]
                Items[i] = Items[smallestIndex]
                Items[smallestIndex] = tmp

        Console.PrintSuccess("Dictionary has been sorted using Selection Sort!")
    else:
        Console.PrintError("Dictionary is empty!")


# Sort items using Selection Sort
def InsertionSort():
    dictLength = len(Items)

    if dictLength > 0:
        for i in range(1, dictLength):
            stockValue = Items[i].itemStock
            positionIndex = Items[i]

            pos = i
            while pos > 0 and stockValue < Items[pos - 1].itemStock:
                Items[pos] = Items[pos - 1]
                pos -= 1

            Items[pos] = positionIndex

        Console.PrintSuccess("Dictionary has been sorted using Insertion Sort!")
    else:
        Console.PrintError("Dictionary is empty!")


# Sort items using Selection Sort
def BubbleSort():
    dictLength = len(Items)

    if dictLength > 0:
        for i in range(dictLength - 1, 0, -1):
            noSwap = True

            for j in range(i):
                if Items[j].itemStock > Items[j + 1].itemStock:
                    temp = Items[j]
                    Items[j] = Items[j + 1]
                    Items[j + 1] = temp
                    noSwap = False

            if noSwap:
                break

        Console.PrintSuccess("Dictionary has been sorted using Bubble Sort!")
    else:
        Console.PrintError("Dictionary is empty!")


# Ask for which searching algorithm to use
def SearchItem():
    typeOfSearch = int(Console.ReadLine("(1 for Linear Search) || (2 for Binary Search) || (3 For JumpSearch [Advanced Algorithm]): "))
    if typeOfSearch == 1:
        LinearSearch()
    elif typeOfSearch == 2:
        BinarySearch()
    elif typeOfSearch == 3:
        JumpSearch()
    else:
        return Console.PrintError("Not a valid search option.")


# Search for item using Linear Search
def LinearSearch():
    dictLength = len(Items)

    if dictLength > 0:
        BubbleSort()
        Info = Console.AskInfo(False, False, False, False, True, False, False)
        search_stock = Info['stock']

        for i in range(0, dictLength):
            if search_stock == Items[i].itemStock:
                Console.PrintSuccess("Fruit with the stock count of {} has been found!".format(search_stock))
                return print(Items[i], '\n')
            elif search_stock < Items[i].itemStock:
                return Console.PrintError("Fruit with the stock count of {} was not found!".format(search_stock))

        return Console.PrintError("Fruit with the stock count of {} was not found!".format(search_stock))

    return Console.PrintError("Dictionary is empty!")


# Search for item using BinarySearch
def BinarySearch():
    dictLength = len(Items)

    if dictLength > 0:
        SelectionSort()
        Info = Console.AskInfo(False, False, False, False, True, False, False)
        search_stock = Info['stock']

        low = 0
        high = dictLength - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if search_stock == Items[mid].itemStock:
                Console.PrintSuccess("Fruit with the stock count of {} has been found!".format(search_stock))
                return print(Items[mid], '\n')
            elif search_stock > Items[mid].itemStock:
                low = mid + 1
            else:
                high = mid - 1

        return Console.PrintError("Fruit with the stock count of {} was not found!".format(search_stock))

    return Console.PrintError("Dictionary is empty!")


# Search for item using JumpSearch [Advanced Feature]
def JumpSearch():
    dictLength = len(Items)

    if dictLength > 0:
        InsertionSort()
        Info = Console.AskInfo(False, False, False, False, True, False, False)
        search_stock = Info['stock']

        jump = int(math.sqrt(dictLength))
        left, right = 0, 0
        while left < dictLength and Items[left].itemStock <= search_stock:
            right = min(dictLength - 1, left + jump)
            if Items[left].itemStock <= search_stock <= Items[right].itemStock:
                break
            left += jump

        if left >= dictLength or Items[left].itemStock > search_stock:
            return Console.PrintError("Fruit with the stock count of {} was not found!".format(search_stock))

        right = min(dictLength - 1, right)
        i = left

        while i <= right and Items[i].itemStock <= search_stock:
            if Items[i].itemStock == search_stock:
                Console.PrintSuccess("Fruit with the stock count of {} has been found!".format(search_stock))
                return print(Items[i], '\n')

            i += 1

        return Console.PrintError("Fruit with the stock count of {} was not found!".format(search_stock))

    return Console.PrintError("Dictionary is empty!")


# Exit from console/terminal
def ExitApplication():
    exit()


# Improvised enum since Python doesn't have it
options = {1: AddItem,
           2: UpdateItem,
           3: RemoveItem,
           4: DisplayItems,
           5: SortItem,
           6: SearchItem,
           7: ExitApplication}


# Function to run all the tasks
def InitiateTasks():
    while True:
        try:
            Console.DrawMenu()
            userOption = int(Console.ReadLine('\nOption: '))
            options[userOption]()
        except ValueError:
            Console.PrintError("Please insert only number")
        except KeyError:
            Console.PrintError('Option/Key not found')


# Run the task when function is being called
InitiateTasks()
