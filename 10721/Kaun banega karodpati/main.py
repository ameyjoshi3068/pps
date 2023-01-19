import time

print("KBC rules are according to KBC Season 14")
start=input("A question will be asked to you you have to enter question number as input\nYou can exit the game at any time by entering 'End' in the answer\nEnter to start the game\n\n")

prize=0
endContest=False

#Defining questions and answer set
questions=("What is the capital of india?","World Health Day is observed on","Pongal is a popular festival of which state?","The death anniversary of which of the following leaders is observed as Martyrs' Day?","Who is the author of the epic 'Meghdoot'?","'Good Friday' is observed to commemorate the event of","The language of Lakshadweep. a Union Territory of India, is","In which group of places the Kumbha Mela is held every twelve years?","Which of the following is observed as Sports Day every year?","The International Literacy Day is observed on",'Bahubali festival is related to',"Which day is observed as the World Standards  Day?","Which of the following was the theme of the World Red Cross and Red Crescent Day?","September 27 is celebrated every year as","Who is the author of 'Manas Ka-Hans' ?""Who is the author of the book 'Amrit Ki Ore'?","Van Mahotsav was started by")
options=(("New Delhi","Mumbai","Kolkata","Banglore"),("Apr 7","Mar 6","Oct 24","Apr 28"),("Karnataka","Kerala","Tamil Nadu","Andhra Pradesh"),("Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Gandhi","Lal Bahadur Shastri"),("Vishakadatta","Valmiki","Banabhatta","Kalidas"),("birth of Jesus Christ","birth of' St. Peter","crucification 'of Jesus Christ","rebirth of Jesus Christ"),("Tamil","Tamil","Hindi","Malyalam","Telgu"),("Ujjain, Purl, Prayag, Haridwar","Prayag, Haridwar, Ujjain, Nasik","Rameshwaram, Puri, Badrinath, Dwarika","Chittakoot, Ujjain, Prayag, Haridwar"),("22nd April","26th  july","29th August","2nd October"),("Sept 8","Nov 28","May 2","Sept 22"),("Islam","Hinduism","Buddhism","Jainism"),("June 26","Oct 14","Nov 15","Dec 2"),("'Dignity for all - focus on women'","Dignity for all - focus on Children'","Dignity for all - focus on Children'","Nourishment for all-focus on children'"),("Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day"),("Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar"),("Mukesh Kumar","Narendra Mohan","Narendra Mohan","Nirad C. Choudhary"),("Maharshi Karve","Bal Gangadhar Tiiak","K.M. Munshi","Sanjay Gandhi"))
ans_key=[1, 1, 3, 3, 4, 3, 3, 2, 3, 1, 4, 2, 2, 3, 4,3]

def question(i):
    print(f"This is question no {i+1} for {prizemoney[i]} Rs")
    print(questions[i])
    selection=int(input(f"Your options are:\n1){options[i][0]}          2){options[i][1]}\n3){options[i][2]}          4){options[i][3]}\nEnter 0 to end the contest\nYour Answer: "))
    if selection==ans_key[i]:
        return "Correct"
    # elif selection==9:
    #     return "Correct"
    elif selection==0:
        return "End"
    elif selection>4:
        return "Invalid"

def timer(i):
    if i<5:
        print("You have 30 seconds to answer")
        time.sleep(20)
        print("Last ten seconds")
        time.sleep(10)
        print("Time is up!!")
        return prizemoney[i-1],True
    elif i<10:
        print("You have 60 seconds to answer")
        time.sleep(30)
        print("30 seconds left")
        time.sleep(20)
        print("Last ten seconds")
        time.sleep(10)
        print("Time is up!!")
        return prizemoney[i-1],True
    elif i==10:
        print("There is no time limit for questions after this")


prizemoney=(1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000)

def prizeHandle(i):
    ans=question(i)
    if ans=="Correct" and i==16:
        print("Outstanding!!!All answers are correct. You have won 7.5 Crore Rs")
    elif ans=="Correct":
        print(f"Congradulations!! Correct answer!\nYou have won {prizemoney[i]}Rs\n\n")
        return prizemoney[i],False
    elif ans=="End":
        return prizemoney[i-1],True
    elif ans=="Invalid":
        print("Invalid option number\nEnter correct option number")
        prizeHandle(i)
    else:
        print(f"Your answer is wrong!\nThe correct answer for this question was:-{ans_key[i]}) {options[1][ans_key[i]-1]}\n\n")
        if prize<10000:
            return 0,True
        elif prize<320000:
            return 10000,True
        elif prize<7500000:
            return 320000,True
        elif prize<75000000:
            return 7500000,True

def prizeAnnouncement(prize):
    if prize==0:
        print("I am very sorry to say that, You coulden't win prize here")
    else:
        print(f"Congradulations, you have won {prize} Rs")


for i in range(len(questions)):

    prize,endContest=(prizeHandle(i))
    if endContest==True:
        break

prizeAnnouncement(prize)