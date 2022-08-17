


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
        #A deposit method that accepts an amount and description. 
        #If no description is given, it should default to an empty string.
        #The method should append an object to the ledger list in the form of 
        #{"amount": amount, "description": description}.
        
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
        #keep track of the balance
        if amount <= self.balance:    #fixed bug here where the value of the balance can be in negative.
            #THIS NEEDS FIXING!!!
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
            #first withdraw the amount to be transefered from the desired category.
            #self.withdraw(amount)
            #if the withdraw operation has failed, return false
            #it seems like once the function is put in an conditional statement, it actually runs!(in the that if statement the withdrawal function already being executed)
            if self.withdraw(amount) == False:
                print(f"not enough balance in {self.name} category")
                return False
            else:
                #check within the categories list if the category you're transfering to exists
                for object in Category.categories:
                    if destination == object:
                        #if the targetted category(object) exist, deposite the money you trasfered
                        object.deposit(amount)
                        print(f"Transfer {amount} from [{self.name}]")
                        return True       
        #The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
        #The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
        #If there are not enough funds, nothing should be added to either ledgers.
    
    def check_funds():
        #A check_funds method that accepts an amount as an argument.
        #It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        #This method should be used by both the withdraw method and transfer method.
        pass





#creating the category objects
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

#calling the deposide method, which creates a dictionary for each category, containing the money deposited for each category along with the description
food.deposit(500,"Money deposited for food")
clothing.deposit(200,"Money for clothes")
entertainment.deposit(300,"Money for hangouts")



print("the food balance is :",food.get_balance())
print("the clothing balance is :",clothing.get_balance())
food.transfer(clothing,450)
print("the food balance is :",food.get_balance())
print("the clothing balance is :",clothing.get_balance())















categories = []
for cat in Category.categories:
    categories.append(cat.name)
def create_spend_chart(categories):
    #create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
    return str(categories)
#print this method later
create_spend_chart(categories)