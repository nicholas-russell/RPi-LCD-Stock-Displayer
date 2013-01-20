import ystockquote # Yahoo stocks library written by Corey Goldberg. 
from Adafruit_CharLCD import Adafruit_CharLCD # Adafruit CharLCD libary, from their github. 
from time import sleep

lcd = Adafruit_CharLCD() # Starts the lcd
lcd.begin(16,1)
# Gets the stocks from stocks.txt.  
def getStockList() :
	file = open("stocks.txt", "r") # Opens stocks.txt in read mode. 
	stocksList = file.read() # Puts the stocks into a string. 
	return stocksList.split() # Returns the splitted version. 

def printStocks(sL) : # Prints the stocks
	for x in sL: # A for each loop
		lcd.clear() # Clears the LCD
		print x + " " + ystockquote.get_price(x) # Gets the price of x and prints it to console
		lcd.message(x + " " + ystockquote.get_price(x)) # Gets the price and shows it on the lcd
		print ystockquote.get_change(x) # Gets the price change and prints it to the console
		lcd.message(ystockquote.get_change(x)) # Gets the price change and shows it on the lcd
		sleep(10) # Sleeps so it user can read the info

stockList = getStockList() # Puts the stocks as a list into stockList

print stockList # Prints it to the console, for debugging purposes


while 1:
	printStocks(stockList) # Continually prints the stocks

