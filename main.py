#this program calculate emplployees productivity bounuss

#declare you veriable (input):
bonus=0
bonus_1=50
bonus_2=75
bonus_3=100
bonus_4=200.00

#input:
#ask the user to enter employee name, number of shifts, number of transaction,and transaction dollar value.
employee_name= input("enter employee's name ")
shiftsstring= input("enter number of shifts ")
transactionstring= input("enter number of transactions ") 
dollarvaluestring= input("enter employee's transaction dollar value ")

# create your own variables to calculate the prodiuctivity score.
# assgin the new veriables to the value the user input:
numbershifts=float(shiftsstring)
numbertransaction=float(transactionstring)
transactiondollarvalue=float(dollarvaluestring)

# determaine the productivity score by dividing the dollar value by the number of transactions and divid the result by 
productivtiy_score = (transactiondollarvalue/ numbertransaction)/numbershifts

# write your if statement:
if productivtiy_score<= 30:
  bonus= bonus_1
elif productivtiy_score >=31 and productivtiy_score <=69:
    bonus= bonus_2
elif productivtiy_score >=70 and productivtiy_score<=199:
      bonus=bonus_3
elif productivtiy_score >= 200:
        bonus=bonus_4
  
  ##print the employee name, and the productivity score (output).
print("employee name: "+str(employee_name))
print("employee bounc: $"+str(bonus))
   
  

  
  

