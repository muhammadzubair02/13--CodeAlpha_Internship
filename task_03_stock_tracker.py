#Create a stock dictionary
stock_dic = {
    'MSFT' : 200,
    'AMZN' : 300,
    'GOOGL': 400,
    'META' : 500,
    'NVDA' : 600,
    'TSLA' : 700
}

def stock_tracker():
    #Get data from user
    stock_name = input("Please enter the stock name: ").upper()
    stock_quantity = input("Please enter the invested stock quantity: ")

    #Converts quantity into integer
    stock_quantity = int(stock_quantity)
