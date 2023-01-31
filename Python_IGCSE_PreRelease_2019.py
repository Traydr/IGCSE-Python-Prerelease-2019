itemNum = [0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001]
itemNumDesc = ["lamp", "monitor", "desk", "laptop", "phone", "mouse", "keyboard", "microphone", "earphones",
               "headphones"]
itemReservePrice = [20, 150, 100, 800, 500, 50, 120, 75, 25, 60]
numOfBids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
currentMaxBid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
buyerId = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
isItemSold = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
itemNumCounter = 0
finalBid = 0
companyFee = 0
totalFee = 0
tempVar = 0


def buyer_view():
    viewitem = int(
        input("Which item would you like to view (write the itemnum)"))
    listitem = itemNum.index(viewitem)
    print("The description of", viewitem, "is", itemNumDesc[listitem])
    print("The reserve price of", viewitem, "is $", itemReservePrice[listitem])
    print("There are currently", numOfBids[listitem], "bid(s) on ", viewitem)
    print("The current highest bid of", viewitem,
          "is $", currentMaxBid[listitem])
    buyer_view_again()


def buyer_view_again():
    viewagain = input("Would you like to look at the items again (y/n)")
    if viewagain == "y":
        buyer_view()
    elif viewagain == "n":
        buyer_bid_temp()
    else:
        print("Wrong input")
        buyer_view_again()


def buyer_bid_temp():
    wouldbuyerliketobid = input("Would you like to bid right now? (y/n)")
    if wouldbuyerliketobid == 'y':
        buyer_bid()
    elif wouldbuyerliketobid == 'n':
        print("Exiting biding")
        quit
    else:
        print("error worng input")
        buyer_bid_temp()


def buyer_bid():
    global finalBid
    biditemtemp = int(
        input("Which item would you like to bid on (write itemnum)"))
    biditemnumtemp = itemNum.index(biditemtemp)
    buyeridtemp = input("What is your buyer id")
    biditemamount = input("How much would you like to bid on the item")
    if int(biditemamount) > int(currentMaxBid[biditemnumtemp]):
        print("Congradulations your bid was succesful!")
        buyerId[biditemnumtemp] = buyer_bid_temp
        currentMaxBid[biditemnumtemp] = biditemamount
        finalBid = biditemamount
        numOfBids[biditemnumtemp] += 1
    elif biditemamount < currentMaxBid[biditemnumtemp]:
        print("Your bid was lower that the current bid, and therefore is invalid")
    else:
        print("You did not type your bid correctly")
    wouldlikebidagain = input("Would you like to bid again (y/n)")
    if wouldlikebidagain == 'y':
        buyer_bid()
    elif wouldlikebidagain == 'n':
        calc_sold()
    else:
        print("Wrong input, restarting")
        buyer_bid()


def calc_sold():
    itemnumcounter = 0
    for i in range(0, 10):
        if int(currentMaxBid[itemnumcounter]) > int(itemReservePrice[itemnumcounter]):
            isItemSold[itemnumcounter] = 'is'
        elif int(currentMaxBid[itemnumcounter]) < int(itemReservePrice[itemnumcounter]):
            isItemSold[itemnumcounter] = 'is not'
        else:
            print("Something wrong happenend in the calculation of items sold")
        itemnumcounter += 1
    auction_end()


def auction_end():
    global totalFee
    itemnumcounter = 0
    totalfeetemp = 0
    for i in range(0, 10):
        print("Item", itemNum[itemnumcounter],
              isItemSold[itemnumcounter], "SOLD!")
        totalfeetemp += int(currentMaxBid[itemnumcounter])
        totalFee += totalfeetemp
        itemnumcounter += 1
    companyfee = int(finalBid) * 0.1
    totalFee += companyfee
    print("The total fee for all items sold is $", totalFee)
    itemnumcounter = 0
    for i in range(0, 10):
        if numOfBids[itemnumcounter] == 0:
            print("Item", itemNum[itemnumcounter], "did not recieve any bids")
        elif numOfBids[itemnumcounter] > 0:
            if int(currentMaxBid[itemnumcounter]) < int(itemReservePrice[itemnumcounter]):
                print("Item", itemNum[itemnumcounter],
                      "was not sold because it did not reserve price, the final bid was", currentMaxBid[itemnumcounter])
            else:
                print()
        else:
            print()
        itemnumcounter += 1
    print(numOfBids.count(0), " item(s) recieved no bids")
    print(isItemSold.count('is'), "item(s) were sold")
    print(isItemSold.count('is not'), "item(s) did not reach their reserve price")


buyer_view()
