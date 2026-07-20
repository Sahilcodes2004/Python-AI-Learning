questions=[["which language was used to create fb?","Python","French","Javascrropt","Php","Nond",4],
           ["which language was used to create fb?","Python","French","Javascrropt","Php","Nond",4],
           ["which language was used to create fb?","Python","French","Javascrropt","Php","Nond",4],
           ["which language was used to create fb?","Python","French","Javascrropt","Php","Nond",4],]
levels=[1000,2000,5000,10000,50000,100000,500000,1000000,2000000,5000000]

for i in range(0,len(questions)):
    question=questions[i]
    print(f" Question for Rs.{levels[i]}")
    print(f"a.{question[1]}                 b.{question[2]}")
    print(f"c.{question[3]}                 d.{question[4]}")
    reply=int(input("Enter you answer (1-4)"))
    if(reply==question[-1]):
        print(f"Correct answer you won {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=5000000
        elif(i==7):
            money=1000000
    else:
        print("Wrong Answer!")
        break
print(f"your take home money is {money}")