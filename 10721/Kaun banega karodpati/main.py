print("KBC rules are according to KBC Season 14")
start=input("A question will be asked to you you have to enter question number as input\nEnter to start the game")

prize=0
endContest=False

#Defining questions and answer set
questions=("What is the capital of india?","The International Literacy Day is observed on","The language of Lakshadweep. a Union Territory of India, is","In which group of places the Kumbha Mela is held every twelve years?",'Bahubali festival is related to',"Which day is observed as the World Standards  Day?","Which of the following was the theme of the World Red Cross and Red Crescent Day?","September 27 is celebrated every year as","Who is the author of 'Manas Ka-Hans' ?","The death anniversary of which of the following leaders is observed as Martyrs' Day?","Who is the author of the epic 'Meghdoot'?","'Good Friday' is observed to commemorate the event of","'Good Friday' is observed to commemorate the event of","Which of the following is observed as Sports Day every year?","World Health Day is observed on","Pongal is a popular festival of which state?","Van Mahotsav was started by")
options=(("New Delhi","Mumbai","Kolkata","Banglore"),("Sept 8","Nov 28","May 2","Sept 22"),("Tamil","Tamil","Hindi","Malyalam","Telgu"),("Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot", "Ujjain","Prayag","Haridwar"),("Islam","Hinduism","Buddhism","Jainism"),("June 26","Oct 14","Nov 15","Dec 2"),("'Dignity for all - focus on women'","Dignity for all - focus on Children'","Dignity for all - focus on Children'","Nourishment for all-focus on children'"),("Teachers' Day","National Integration Day","World Tourism Day","International Literacy Day"),("Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar"),("Smt. Indira Gandhi","PI. Jawaharlal Nehru","Mahatma Oandhi","Lal Bahadur Shastri"),("Vishakadatta","Valmiki","Banabhatta","Kalidas"),("birth of Jesus Christ","birth of' St. Peter","crucification 'of Jesus Christ","rebirth of Jesus Christ"),("Mukesh Kumar","Narendra Mohan","Narendra Mohan","Nirad C. Choudhary"),("22nd April","26th  july","29th August","2nd October"),("Apr 7","Mar 6","Oct 24","Apr 28"),("Karnataka","Kerala","Tamil Nadu","Andhra Pradesh"),("Maharshi Karve","Bal Gangadhar Tiiak","K.M, Munshi","Sanjay Gandhi"))
ans_key=(1,1,3,2,4,2,2,3,4,3,4,3,2,3,1,3,3)

def question(i):

    print(f"Question no {i+1}")
    print(questions[i])
    selection=int(input(f"Your options are:\n1){options[i][0]}          2){options[i][1]}\n3){options[i][2]}          4){options[i][3]}\nEnter 0 to end the contest\nYour Answer: "))
    if selection==ans_key[i]:
        return "Correct"
    elif selection==0:
        return "End"
    elif selection>4:
        return "Invalid"

def timer():
    pass

prizemoney=(1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000)

def prizeHandle(i):
    ans=question(i)
    if ans=="Correct":
        print(f"Congradulations!! Correct answer!\nYou have won {prizemoney[i]}Rs\n\n")
        return prizemoney[i],False
    elif ans=="End":
        return prizemoney[i-1],True
    elif ans=="Invalid":
        print("Invalid option number\nEnter correct option number")
        prizeHandle(i)
    else:
        print("Your answer is wrong!\n\n")
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
#Added for start and for end