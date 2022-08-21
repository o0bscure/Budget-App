
class Category:
    #making an independent ledger for each withdraw and deposit
    deposit_ledger = list()
    withdraw_ledger = list()
    #a class attribute that can be used on all this class objects
    balance = int()
    categories = []
    
    def __init__(self,name:str):
        self.name = name
        self.withdraw_ledger = list()
        self.deposit_ledger = list()
        Category.categories.append(self) #or self .name ?! , i'll have to look at the latest function requirement later

    def deposit(self,amount,description=""):
        #keeping track of the balance
        self.balance = self.balance + amount
        #created a "data" dictionary for each category object, containing its value and description
        data = dict()
        #okay maybe make a condition to add the key and value if the disctionary doesnt exist to avoid overwriting it
        #you'll have tp manipulate existing ledger in case you wanna deposite twice 
        data["amount"] = amount
        data["description"] = description
        #adding the dictionary to the ledger list
        #hmmm maybe find a way to write that on a csv file (fun)
        self.deposit_ledger.append(data)
        
    def withdraw(self,amount,description=""):
        #check if the given amount to be withdrawn is actually available for that category
        if self.check_funds(amount) == True:
            #withdraw from the category balance
            self.balance = self.balance - amount
            #making sure i add nothing to the ledger if there isnt enough balance(not enough deposited money to withdraw from)
            #okay maybe make a condition to add the key and value if the disctionary doesnt exist to avoid overwriting it
            #you'll have tp manipulate existing ledger in case you wanna withdraw twice
            #each withdraw will add the object withdrawn from as a dictionary
            data = dict()
            #the amount should be stored in the withdraw ledger as a negative number, did that by adding the minus sign as a string then convert it to string
            data["amount"] = "-"+ str(amount)
            data["amount"] = int(data["amount"])
            data["description"] = description
            self.withdraw_ledger.append(data)
            return True
        else:
            print("not enough balance")
            return False


    def get_balance(self):
        return self.balance
        #A get_balance method that returns the current balance of the budget category 
        #based on the deposits and withdrawals that have occurred
        
    def transfer(self,destination,amount:int,description=""):
        #first check if the given argument to transfer the money to (destination) is an actual category object
        if not isinstance(destination,Category):
            print(f"{destination} isn't a category")
            return False
        else: 
            #check if the amount to be transfered is available in the target caegory
            if self.check_funds(amount) == False:
                print(f"not enough balance in {self.name} category")
                return False
            else:
                #assert len(description) > 1, f"please add a transfer description"
                description = f"Transfer {amount} to [{destination.name}]"
                print(description)
                self.withdraw(amount)
                #check within the categories list if the category you're transfering to exists
                for object in Category.categories:
                    if destination == object:
                        #if the targetted category(object) exist, deposite the money you trasfered
                        object.deposit(amount)
                        description = f"Transfer {amount} from [{self.name}]"
                        print(description)
                        return True       
    
    #a function that tells you if the input amount is availble for that particular category
    def check_funds(self,amount):
        #check if the amount given is greater than the category balance or not
        if amount > self.balance:
            return False
        else:
            return True
        
    def __repr__(self):
        header = str("*"*30)
        title = self.name
        header = header[int(len(title)):]
        if len(header) < 30 and len(title) == len(self.name):
            header = header[:int(len(header)/2)] + str(self.name) + header[int(len(header)/2):]
            #header is ready, now do the rest
        chart = list()
        #need to make a loop inside that return statement, a loop which goes through the ledger list by index, then print the description and amount keys from each withdraw disctionary
        for index in range(len(self.withdraw_ledger)):
            #next line is where each withdraw or deposite will be presented
            #adjust the position of the amount to be aligned on the right, opposite of the description, without exceeding the lenght of the entire header
            line = str(self.withdraw_ledger[index]['description']) + str(self.withdraw_ledger[index]['amount']).rjust(len(header)-len(self.withdraw_ledger[index]['description']))
            #once extraced, add it to a list so u can pick from that list later in order to print the result
            chart.append(line)
            
            
        #need to figure a way to figure out how many items in the intire chart list, then find a dynamic way to add each one into the final output
        #here i just added the list items through manual index(not great)
        #go through the chart list (by index) which has each line of discripton and amount as an item.
        result = ""
        for index in range(len(chart)):
            #each time the loop runs, it adds a line from the list to the initial result until there are no more items.
            result = f"{result}{chart[index]}\n"
        #finally add the header to the final output
        output = f"{header}\n{result}"
        return output

#looks like i need to have dedicated deposite ledger and withdraw ledger for each category

#creating the category objects
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

#calling the deposide method, which creates a dictionary for each category, containing the money deposited for each category along with the description
food.deposit(500,"initial deposite")
clothing.deposit(200,"Money for clothes")
entertainment.deposit(300,"Money for hangouts")


clothing.withdraw(100,"sneakers")
food.withdraw(100,"groceries")
food.withdraw(150,"protein supplements")
food.withdraw(50,"energy driks")
food.withdraw(50,"desserts")

print(food)
print(clothing)









































categories = []
for cat in Category.categories:
    categories.append(cat.name)
def create_spend_chart(categories):
    #create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
    return str(categories)
#print this method later
create_spend_chart(categories)