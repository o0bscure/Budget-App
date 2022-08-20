


class Category:
    
    #making an independent ledger for each withdraw and deposit
    deposit_ledger = list()
    withdraw_ledger = list()
    #a class attribute that can be used on all this class objects
    balance = int()

    categories = []
    
    def __init__(self,name:str):
        self.name = name
        Category.categories.append(self) #or self .name ?! , i'll have to look at the latest function requirement later

    def deposit(self,amount,description=""):
        #keeping track of the balance
        self.balance = self.balance + amount
        #created a "self" dictionary for each category object, containing its value and description
        self = dict()
        #okay maybe make a condition to add the key and value if the disctionary doesnt exist to avoid overwriting it
        #you'll have tp manipulate existing ledger in case you wanna deposite twice 
        self["amount"] = amount
        self["description"] = description
        #adding the dictionary to the ledger list
        #hmmm maybe find a way to write that on a csv file (fun)
        Category.deposit_ledger.append(self)
        
    def withdraw(self,amount,description=""):
        #check if the given amount to be withdrawn is actually available for that category
        if self.check_funds(amount) == True:
            #withdraw from the category balance
            self.balance = self.balance - amount
            #making sure i add nothing to the ledger if there isnt enough balance(not enough deposited money to withdraw from)
            #okay maybe make a condition to add the key and value if the disctionary doesnt exist to avoid overwriting it
            #you'll have tp manipulate existing ledger in case you wanna withdraw twice
            #each withdraw will add the object withdrawn from as a dictionary
            self = dict()
            #the amount should be stored in the withdraw ledger as a negative number, did that by adding the minus sign as a string then convert it to string
            self["amount"] = "-"+ str(amount)
            self["amount"] = int(self["amount"])
            self["description"] = description
            Category.withdraw_ledger.append(self)
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
        #need to make a loop inside that return statement, a loop which goes through the ledger list by index, then print the description and amount keys from each withdraw disctionary
        return f"{self.balance}\n{self.withdraw_ledger[0]['description']}       {self.withdraw_ledger[0]['amount']}"




#creating the category objects
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

#calling the deposide method, which creates a dictionary for each category, containing the money deposited for each category along with the description
food.deposit(500,"Money deposited for food")
clothing.deposit(200,"Money for clothes")
entertainment.deposit(300,"Money for hangouts")

food.withdraw(100,"groceries")
print(food)









































categories = []
for cat in Category.categories:
    categories.append(cat.name)
def create_spend_chart(categories):
    #create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
    return str(categories)
#print this method later
create_spend_chart(categories)