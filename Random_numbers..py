import random
def random_number():
    my_list=[]
    even_number=0
    for i in range(100):
        x= random.randint(1,101)
        my_list.append(x)
    print(my_list)
    for i in my_list:
        if i%2==0:
            even_number+=1
    print("You have %s even numbers!"%even_number)
random_number()
