def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
    "+" :add,
    "-" :sub,
    "*" :mul,
    "/" :div,
}

def calculator():

    repetition=True

    num1=float(input("what is your first number:"))
    while(repetition):
        
        for operator in operations:
            print(operator)

        operator=input("please select operator:")
        num2=float(input("What is your second number:"))
        res=operations[operator](num1,num2)
        print(res)
        choice=input("Type 'yes' if you want to continue or 'no' :")
        if choice=='yes':
            num1=res
        else:
            repetition=False
            print("\n"*20)  #This gives the only empty lines for understanding that means withour´t clearing, it gives space lines.
            
calculator()