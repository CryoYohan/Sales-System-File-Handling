'''
                SIMPLE SALES SYSTEM
    *****CERTIFIIED ORIGINAL COPY OF THE CODE******
                YPIL, CYRIL JOHN T.
   
   **incase of plagiarism, this is the original copy**
   
'''
from os import system, path

itemsfile:str = 'items.csv'
cartfile:str = 'cartfile.csv'

quantity:int = 0

cart:list = []
inventory:list = []
itemcode:str = ""
headercart:list = ['#','ITEM CODE','DESCRIPTION', 'PRICE','QTY','TOTAL']
headeritem:list = ['ITEM CODE', 'DESCRIPTION', 'PRICE']

def function_header(title:str)->None:
    '''Displays the header of a specific Function'''
    system('cls')
    print(title.upper())
    print("-"*100)

def buy()->None:
    '''Buy function with sub functions to find the items the user wants to buy and add the item in the cart'''
    global itemcode
    function_header('Buy')
    try:
        itemcode = input('ITEM CODE       : ').strip()
        if itemcode == '':
            raise ValueError
            sales_system_menu()
    except ValueError:
        print('\nYou\'ve entered an empty field!\n')
    if find_item():
        price = float(cart[2])
        print(f"DESCRIPTION     : {cart[1]}\nPRICE           : {price:.2f}")
        totalprice = getQuantity()
        if not totalprice == None:
            print(f'{'-'*30}\nTOTAL           : {totalprice}')
            cart.append(str(quantity))
            cart.append(totalprice)
            add_to_cart(cart)
        else:
            sales_system_menu()
        
        
def find_item()->bool:
    '''Find item function that finds the item base on the prompted ITEMCODE'''
    global cart, inventory, itemcode
    file = open(itemsfile)
    inventory = file.readlines()
    file.close()
    
    item_found:bool = True
    
    for items in inventory:
        item:list = items.strip().split(',')
        if itemcode == item[0]:
            item_found = True
            cart = item
            return True
            break
        else:
            item_found = False
    if not item_found:
        print('\nITEM NOT FOUND: Sorry we do not have this item at the moment.\n')
        return False
            

def getQuantity()->float:
    '''Let user prompt the quantity of the item and returns the calculated total price of the item'''
    global quantity
    quantity = int(input('QTY             : '))
    try:
        if quantity <0: raise ValueError
        elif quantity == 0: raise TypeError
    except ValueError:
        print('\nNegatives not allowed!\n')
        input('Press any key to continue...')
    except TypeError:
        print('\nYou must enter a valid quantity that is > \'0\'\n')
        input('Press any key to continue...')
    else:
        totalprice:float = quantity * float(cart[2])
        return f"{totalprice:.2f}"
    
    
def add_to_cart(item:list)->None:
    '''Adds the items to the cart and write it in "cartfile.csv" '''
    my_item = ",".join(item)
    if not path.exists(cartfile):
        print('\nFile does not exist !!!\n\nCreating file...\n\nFile Successfully Created! You can now add your items in your cart.\n')
        file = open(cartfile, 'a')
        file.close
    else:
        file = open(cartfile,'a')
        file.write(my_item + "\n")
        file.close()
    

def showcart()->None:
    '''Displays the items added in the cart from the cartfile with a subfunction to show the overall total price'''
    show_cart:list = []
    function_header('Show Cart')
    if path.exists(cartfile):       
        file = open(cartfile)
        show_cart = file.readlines()
        file.close()
        if not len(show_cart) == 0:
            [print(f"{head:<17}", end = "") for head in headercart]
            print()
            print('-'*100)
            itemno:int = 1
            for items in show_cart:
                item = items.strip().split(',')
                print(f"{itemno:<17}", end = "")
                [print(f"{data:<17}", end="") for data in item]
                itemno+=1
                print()
            print('-'*100)
            print(f"\t\t\t\t\t\t\t\t\t     TOTAL : {show_totalprice(show_cart):.2f}")
        else:
            print('-'*100)
            print('You currently have no items in your cart.'.center(100))
            print('-'*100)
    else:
        print('-'*100)
        print('You currently have no items in your cart.'.center(100))
        print('-'*100)
    
 
def show_totalprice(items:list)->None:
    '''Accepts list of all items in cart and adds all of the total prices and returns the over all total price'''
    totalprice:int = 0
    for item in items:
        item:list = item.strip().split(',')
        price = float(item[4])
        totalprice += price
    return totalprice
            
    
def showitems()->None:
    '''Display all items from the "itemsfile", aka the inventory'''
    function_header('Show items')
    file = open(itemsfile)
    inventory = file.readlines()
    file.close()
    
    [print(f"{head:<20}", end = "") for head in headeritem]
    print()
    print('-'*100)
    
    for items in inventory:
        item:list = items.strip().split(',')
        [print(f"{data:<20}", end = "") for data in item]
        print()
    print('-'*100)
    print('Nothing Follows'.center(100))


def terminate()->None:
    '''Terminates the program right away'''
    print('\nProgram Terminated...')
    exit()

# A dictionary that consists the main modules of the Simple Sales System Program
menu:dict = {1:buy, 2:showcart, 3:showitems, 0:terminate}
    
def sales_system_menu()->None:
    '''Display the sales system menu and let user pick a task'''
    choice:int = -1
    while choice !=0:
        function_header('---main menu---')
        try:
            choice = int(input(f'1. Buy\n2. Show Cart\n3. Show Items\n0. Quit/End\n{'-'*20}\nEnter Option(0..3): '))
            if choice > 3 or choice < 0: raise TypeError
            menu[choice]()
        except ValueError:
            print('\nERROR: Please enter NUMERICAL values!\n')
        except TypeError:
            print('\nERROR: Pick from 0 to 3 only!\n')
            
        input('Press any key to continue...')

def main()->None:
    '''Main Module'''
    sales_system_menu()
    
if __name__ == "__main__":
    main()
