
class Category:
    balance = float()
    categories = []
    #keeps track of all deposted money
    total_deposite = float()
    #keeps track of all spent money
    total_spent = dict()
    
    def __init__(self,name:str):
        self.name = name
        #create a ledger list for each indivisual Category (object)
        self.ledger = list()
        Category.categories.append(self)

    def deposit(self,amount,description=""):
        #keep track of all deposited money
        Category.total_deposite = Category.total_deposite + amount
        #keeping track of the balance
        self.balance = self.balance + amount
        #created a "data" dictionary for each category object, containing its value and description
        data = dict()
        data["amount"] = float(amount)
        data["description"] = description
        #adding the dictionary to the ledger list
        self.ledger.append(data)
        
    def withdraw(self,amount,description=""):
        #check if the given amount to be withdrawn is actually available for that category
        if self.check_funds(amount) == True:
            #withdraw from the category balance
            self.balance = self.balance - amount
            #making sure to add nothing to the ledger if there isnt enough balance
            data = dict()
            #the amount should be stored in the withdraw ledger as a negative number add the minus sign as a string then convert it to string
            data["amount"] = "-"+ str(amount)
            data["amount"] = float(data["amount"])
            data["description"] = description
            self.ledger.append(data)
            #add each amount spent in a separate dictionary, to calculate the percentage spent for each category(to be used later)
            if f"{self.name}" in Category.total_spent:
                Category.total_spent[f"{self.name}"] = Category.total_spent[f"{self.name}"] + float(data["amount"])
            else:
                Category.total_spent[f"{self.name}"] = float(data["amount"])                
            return True
        else:
            print("not enough balance")
            return False

    def get_balance(self):
        return self.balance
        #A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred
        
    def transfer(self,amount:int,destination,description=""):
        #first check if the given argument to transfer the money to (destination) is an actual category object
        if not isinstance(destination,Category):
            print(f"{destination} isn't a category")
            return False
        else: 
            #check if the amount to be transfered is available in the target category
            if self.check_funds(amount) == False:
                print(f"not enough balance in {self.name} category")
                return False
            else:
                description = f"Transfer to {destination.name}"
                self.withdraw(amount,description)
                #check within the categories list if the category you're transfering to exists
                for object in Category.categories:
                    if destination == object:
                        #if the targetted category(object) exists, deposite the money you trasfered
                        description = f"Transfer from {self.name}"
                        object.deposit(amount,description)
                        return True       
    
    #a function that tells you if the input amount is availble for that particular category
    def check_funds(self,amount):
        #check if the amount given is greater than the category balance
        if amount > self.balance:
            return False
        else:
            return True
        
    def __str__(self):
        #create the header
        header = str("*"*30)
        title = self.name
        header = header[int(len(title)):]
        if len(header) < 30 and len(title) == len(self.name):
            header = header[:int(len(header)/2)] + str(self.name) + header[int(len(header)/2):]
            
        #prepare the chart
        chart = list()
        #loop through the ledger list by index
        for index in range(len(self.ledger)):
            #line string is where each withdraw or deposite will be presented,adjust the position of the amount to be aligned to the right, opposite of the description, without exceeding the lenght of the entire header
            line = str(self.ledger[index]['description']) + str(f"{self.ledger[index]['amount']:.2f}").rjust(len(header)-len(self.ledger[index]['description']))
            #once extraced, add it to a list
            chart.append(line)    
            
        #loop through the chart list(by index) which has each line of discripton and amount as an a string item.
        result = ""
        for index in range(len(chart)):
            #each time the loop runs, it adds a line from the list to the initial result until there are no more items.
            #check if an indivisual line length is longer than the header.
            if len(chart[index]) > len(header):
                #if it has brackets, break it into two lines
                if ")" in chart[index] or "(" in chart[index]:
                    #split the discription into two lines
                    first = chart[index].split("(")[0]
                    second = chart[index].split("(")[1]
                    second = second.split(")")[0]
                    #adjust the number value to the right without exceeding the header's length (dont forget to subtract the 2 brackets from the rjust(-2))
                    num = chart[index].split(")")[1].rjust(len(header)-len(second)-2)
                    chart[index] = f"{first}\n({second}){num}"
                #more conditional statements could be added here if needed
                else:
                    sign = chart[index].find("-")
                    description = chart[index][:sign-1]
                    num = chart[index][sign:]
                    description = description[0:len(header)-len(num)]
                    chart[index] = f"{description[:-1]} {num}"

            else:
                pass
            result = f"{result}{chart[index]}\n"
                
        #add the header to the final output
        output = f"{header}\n{result}Total: {self.balance}"
        return output

#a dictionary that saves each category as key and the percentage base as value
percentage_dict = dict()
#list to save each category name's length to use in the chart
category_names_length = list()
def create_spend_chart(z):
    total_withdrawal = 0
    for key,value in Category.total_spent.items():
        #add the total withdrawn, remove the minus sign from the string
        total_withdrawal = total_withdrawal + abs(value)
    #calculate the percentage of the spent amount
    for cat in z:
        #only go through the categories the are spent from (categories stored in total spend dictionary)
        if f"{cat.name}" in Category.total_spent:
            #take the percentage spent for each category relative to the -total withdrawals-
            quotient = abs(Category.total_spent[f"{cat.name}"])/ total_withdrawal
            percent = quotient * 100
            percentage_dict[f"{cat.name}"] = int(percent)
            #add the lenght of each category name to a list
            category_names_length.append(len(f"{cat.name}"))

    per_pin = [0,10,20,30,40,50,60,70,80,90,100]
    #per chart is a dictrionary that saves the percentage based(category:percentage)
    per_chart = dict()
    for x in per_pin:
        for cat,num in percentage_dict.items():
            if num > x:
                per_chart[f"{cat}"] = x + 10
    #per_chart is the dictionary that rounds up the percentage numbers

    #markers to add to the chart, based on the percentage spent
    marker = f"  o"
    #create header
    header = "Percentage spent per category"
    #create seperating line
    per_line = f"    {'-'*(len(Category.categories)+9)}"
    #create the upper part of the chart
    upper = ""
    upper_list= []
    #for each item in the spent categories
    for item in per_chart:
        #go through the list of numbers[0,100]
        pos = 0
        for x in reversed(per_pin):
            if len(upper_list) < 11:
                if x == 100:
                    upper_list.append(f"{x}|")
                elif x == 0:
                    if per_chart[item] >= x:
                        upper_list.append(f"  {x}|{marker}")
                    else:
                        upper_list.append(f"  {x}|")
                else:
                    if per_chart[item] >= x:
                        upper_list.append(f" {x}|{marker}")
                    else:
                        upper_list.append(f" {x}|")
            else:
                if per_chart[item] >= x:
                    upper_list[pos] = upper_list[pos] + marker
            pos = pos + 1

    for line in upper_list:
        upper = upper + line + "\n"

    lower = ""
    #loop through the letters is each category
    for i in range(max(category_names_length)):
        try:
            lower = lower+ 6*" "
            for cat in z:
                if i >= len(cat.name):
                    #once the position exceedes the length of given category (all category letters have been printed)
                    lower = lower + "   "
                    continue
                lower = lower + cat.name[i] + "  "
            lower = lower + "\n"
        except Exception as exception:
            print(exception)
    result = f"{header}\n{upper}{per_line}\n{lower}"
    print(result)

#create some objects
food = Category("Food")
entertainment=Category("Entertainment")
business=Category("Business")

#test several functions (deposit, withdraw and transfer)
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55,"carb sources")
food.transfer(120,business)
entertainment.withdraw(33.40)
business.withdraw(10.99)

#print some objects
print(business)
print(food)

#test the create spent chart
create_spend_chart(Category.categories)

#the loop keeps going several times after the intended iterations, even if its not printing (needs to be fixed later!)
