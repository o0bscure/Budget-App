
from traceback import print_tb
from unicodedata import category
from unittest import result


class Category:
    #a class attribute that can be used on all this class objects
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
        Category.categories.append(self) #or self .name ?! , i'll have to look at the latest function requirement later

    def deposit(self,amount,description=""):
        #keep track of all deposited money
        Category.total_deposite = Category.total_deposite + amount
        #keeping track of the balance
        self.balance = self.balance + amount
        #created a "data" dictionary for each category object, containing its value and description
        data = dict()
        #okay maybe make a condition to add the key and value if the disctionary doesnt exist to avoid overwriting it
        #you'll have tp manipulate existing ledger in case you wanna deposite twice 
        data["amount"] = float(amount)
        data["description"] = description
        #adding the dictionary to the ledger list
        #hmmm maybe find a way to write that on a csv file (fun)
        self.ledger.append(data)
        
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
            data["amount"] = float(data["amount"])
            data["description"] = description
            self.ledger.append(data)
            
            #add each amount spent in a separate dictionary, to calculate the percentage spent for each category
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
            #check if the amount to be transfered is available in the target caegory
            if self.check_funds(amount) == False:
                print(f"not enough balance in {self.name} category")
                return False
            else:
                description = f"Transfer to {destination.name}"
                self.withdraw(amount,description)
                data = dict()
                data["amount"] = "-"+ str(amount)
                data["amount"] = float(data["amount"])
                #self.ledger.append(data)
                #check within the categories list if the category you're transfering to exists
                for object in Category.categories:
                    if destination == object:
                        #if the targetted category(object) exist, deposite the money you trasfered
                        description = f"Transfer from {self.name}"
                        object.deposit(amount,description)
                        data = dict()
                        data["amount"] = amount
                        data["description"] = description
                        return True       
    
    #a function that tells you if the input amount is availble for that particular category
    def check_funds(self,amount):
        #check if the amount given is greater than the category balance or not
        if amount > self.balance:
            return False
        else:
            return True
        
    def __str__(self):
        header = str("*"*30)
        title = self.name
        header = header[int(len(title)):]
        if len(header) < 30 and len(title) == len(self.name):
            header = header[:int(len(header)/2)] + str(self.name) + header[int(len(header)/2):]
            #header is ready, now do the rest
        chart = list()
        #need to make a loop inside that return statement, a loop which goes through the ledger list by index, then print the description and amount keys from each disctionary
        for index in range(len(self.ledger)):
            #next line is where each withdraw or deposite will be presented
            #adjust the position of the amount to be aligned on the right, opposite of the description, without exceeding the lenght of the entire header
            line = str(self.ledger[index]['description']) + str(f"{self.ledger[index]['amount']:.2f}").rjust(len(header)-len(self.ledger[index]['description']))
            #once extraced, add it to a list so u can pick from that list later in order to print the result
            chart.append(line)
            
        #go through the chart list (by index) which has each line of discripton and amount as an a string item.
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
                #i could add more conditional statements here, if i want to maniuplute other strings than the brackets
                else:
                    sign = chart[index].find("-")
                    description = chart[index][:sign-1]
                    print(description)
                    num = chart[index][sign:]
                    description = description[0:len(header)-len(num)]
                    chart[index] = f"{description[:-1]} {num}"

            else:
                pass
            result = f"{result}{chart[index]}\n"
                
        #finally add the header to the final output
        output = f"{header}\n{result}Total: {self.balance}"
        return output



#a dictionary that saves each category as key and the percentage base as value
percentage_dict = dict()
#list to save each category name's length to use in the chart
category_names_length = list()
def create_spend_chart(x):
    #calculate the percentage of the spent amount(did that for one category only)
    for cat in x:
        #only go through the categories the are spent from (categories stored in total spend dictionary)
        if f"{cat.name}" in Category.total_spent:
            #remember youre only taking the percentage of each money spend on each category relative to the ENITIRE BUDGET
            quotient = abs(Category.total_spent[f"{cat.name}"])/ Category.total_deposite
            percent = quotient * 100
            percentage_dict[f"{cat.name}"] = int(percent)
            #add the lenght of each category name to a list
            category_names_length.append(len(f"{cat.name}"))

    per = 100
    rows = ""
    upper_chart = list()
    per_pin = [0,10,20,30,40,50,60,70,80,90,100]
    per_chart = dict()
    for catpin in per_pin:
        for cat,num in percentage_dict.items():
            if num > catpin:
                per_chart[f"{cat}"] = catpin + 10
    #per_chart is the dictionary u should rely on now (it has the normalize version of the percentage chart with values like 0,10,20 .... 100)
    
    #while there are still items in the per chart dictionary
    while len(per_chart)>0:
        for row in range(12+max(category_names_length)):
            if len(str(per)) == 2:
                per_line = f"{rows} {per}|"
            elif len(str(per)) == 1:
                per_line = f"{rows}  {per}|"
            else:
                per_line = f"{rows}{per}|"
            per = per - 10    
            if per < 0:
                per_line = f"    {'-'*(len(Category.categories)+7)}"
                upper_chart.append(f"{per_line}\n")
                break
            upper_chart.append(f"{per_line}\n")
        print(upper_chart)
        line = ""
        for cat in per_chart:
            x = f"{cat[0]}  "
            line = x + x
        #removing each category item form the dictionary as it gets to printed to stop the while loop
        per_chart.pop(f"{cat}")
        print(per_chart)

        


    
    
    #create empty rows
    #rows = f"{ '9' * (len(categories)+7)}"
    #columns = f'''
   #100|{' '*(len(categories)+7)}
    #90|{' '*(len(categories)+7)}
    #80|{' '*(len(categories)+7)}
    #70|{' '*(len(categories)+7)}
    #60|{' '*(len(categories)+7)}
    #50|{' '*(len(categories)+7)}
    #40|{' '*(len(categories)+7)}
    #30|{' '*(len(categories)+7)}
    #20|{' '*(len(categories)+7)}
    #10|{' '*(len(categories)+7)}
     #0|{' '*(len(categories)+7)}
       #{"-"*(len(categories)+7)}
        #{categories[0][0]}  {categories[1][0]}  {categories[2][0]}
        #{categories[0][1]}  {categories[1][1]}  {categories[2][1]}
        #{categories[0][2]}  {categories[1][2]}  {categories[2][2]}
        #{categories[0][3]}  {categories[1][3]}  {categories[2][3]}
           #{categories[1][4]}  {categories[2][4]}
           #{categories[1][5]}  {categories[2][5]}
           #{categories[1][6]}  {categories[2][6]}
           #{categories[1][7]}  {categories[2][7]}
              #{categories[2][8]}
              #{categories[2][9]}
              #{categories[2][10]}
              #{categories[2][11]}
              #{categories[2][12]}
        
        #'''
    
    
    #create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
    #return str()
#print this method later


food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")
auto = Category("Auto")

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20,entertainment)
food.transfer(50,clothing)
clothing.withdraw(20,"hat")


#add total to the table

print(create_spend_chart(Category.categories))
