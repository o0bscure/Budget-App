

class Category:
    
    ledger = list()
    categories = []
    
    def __init__(self,name):
        self.name = name
        Category.categories.append(self)

    def deposit(self,amount,description=""):
        #A deposit method that accepts an amount and description. 
        #If no description is given, it should default to an empty string.
        #The method should append an object to the ledger list in the form of 
        #{"amount": amount, "description": description}.
        #created a "self" dictionary for each category object, containing its value and description
        self = dict()
        self["amount"] = amount
        self["description"] = description
        #adding the dictionary to the ledger list
        #hmmm maybe find a way to write that on a csv file (fun)
        Category.ledger.append(self)
        
    def withdraw(self,amount,description=""):
        #A withdraw method that is similar to the deposit method,
        #but the amount passed in should be stored in the ledger as a negative number. 
        #If there are not enough funds, nothing should be added to the ledger.
        #This method should return True if the withdrawal took place, and False otherwise.
        
        return True
        return False
        pass

    def get_balance():
        #A get_balance method that returns the current balance of the budget category 
        #based on the deposits and withdrawals that have occurred.
        pass
    
    def transfer():
        #A transfer method that accepts an amount and another budget category as arguments. 
        #The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
        #The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
        #If there are not enough funds, nothing should be added to either ledgers.
        # This method should return True if the transfer took place, and False otherwise.
        pass
    
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
Category.deposit(food,500,"Money deposited for food")
Category.deposit(clothing,300,"Money deposited for clothes")
Category.deposit(entertainment,200,"Money deposited for weekend hangouts")
#print(Category.ledger)











categories = []
for cat in Category.categories:
    categories.append(cat.name)
def create_spend_chart(categories):
    #create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
    return str(categories)
#print this method later
create_spend_chart(categories)