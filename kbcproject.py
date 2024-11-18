questions = [
    ["Which city is known as the Pink City of India?","banglore","hyderabad","mumbai","jaipur","None",4
        ],
    ["Who wrote India's National Anthem?","RK Narayan","Lal Bahadur Shastri","Chetan Bhagat","Rabindranath Tagore","None",4
        ],
    ["What does not grow on tree according to a popular Hindi saying?","fruits","flowers","leaves","money","None",4
        ],
    [" Which country is the largest producer of coffee in the world?","ethiopia","colombia","vietnam","Brazil","None",4
        ],
    ["Where is India Gate located?","Punjab","Agra","Mumbai","New Delhi","None",4
        ],
    ["Which of the following is not a state of India?","Tamil Nadu","Mumbai","Goa","Vrindachal","None",4
        ],
    ["Which Indian city hosts Indian movie industry?","Goa","hyderabad","chennai","mumbai","None",4
        ],
    ["Which city is known as the 'Silicon Valley Of India'?","delhi","hyderabad","chennai","Banglore","None",4
        ],
    ["Which country is the largest by land area?","india","china","United States","Russia","None",4
        ],
    ["Taj Mahal was made of?","cement","brick","Granite","Marble","None",4
        ],
    ["Which planet is known as the 'Red Planet'?","earth","jupiter","neptune","mars","None",4
        ],
    ["Which animal is known as the 'King of the Jungle'?","ant","wolf","tiger","lion","None",4
        ],
    ["In which year did India gain independence?","1945","1946","1948","1947","None",4
        ],
    [" Who is the current Prime Minister of India (as of 2024)?","Pranathi","man mohan singh","rahul gandhi","narendra modi","None",4
        ],
    ["Who is the author of the book 'Harry Potter'?"," J.R.R. Tolkien","George R.R. Martin","srija"," J.K. Rowling","None",4
        ]
    
    ]
    
levels = [1000,3000,5000,10000,25000,50000,100000,1000000,10000000]

options = [1,2,3,4]

money = "0"



for i in range (0,len(questions)):
    question = questions[i]
    print(f"\n\nthe question for Rs. {levels[i]} is")
    print(f"{question[0]}")
    print(f"{options[0]} {question[1]}       {options[1]} {question[2]}")
    print(f"{options[2]} {question[3]}       {options[3]} {question[4]}")
    try:
        reply = int(input("enter the number: "))
        if (reply == question[-1]):
            print(f"correct answer!,you won Rs.{levels[i]}")
            if(i==4):
                money = "10,000"
            elif(i==9):
                money = "50,000"
            elif(i==12):
                money = "1,00,000"
            elif(i==14):
                money = "1,00,00,000"
                    
        else:
            print("Wrong answer!")
            break
    except ValueError:
        print("enter the valid input")
        break

print("You won Rs.",money)
            
            
            
            
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
