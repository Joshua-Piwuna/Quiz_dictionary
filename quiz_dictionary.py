#Joshua Piwuna, I certify that the codes/answers of this assignment are entirely my own
import random
def main():
    quiz_answer()

def quiz_answer():
    quiz_ans={}
    fileobj=open('states_capitals.txt','r+')
    #contents=fileobj.read()
    list1= []
    list2=[]
    list3=[]
    counter=0

    
    
    for value in fileobj:
        value= value.strip('\n')
        list1=value.split(':')
        list3.append(list1[0])
        list2.append(list1)
        a,b=list2[counter]
        counter+=1
        quiz_ans[a]=b

    question= 'A'
    while question!= 'Q':
        random_digit=random.randrange(0,30)
        random_state=list3[random_digit]
        question=input('What is the capital of '+random_state+'? (or enter Q to quit):')
        if  question=='Q':
            print('End of Quiz')
        else:
            if quiz_ans[random_state]!= question:
                print('Your answer is not correct.')
            if quiz_ans[random_state]== question:
                print('Your answer is correct.')
        
    #print(list3)
        #counter+=1
main()
