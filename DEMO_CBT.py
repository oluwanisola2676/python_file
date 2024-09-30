# THIS IS A CBT EXAMINATION
score = 0
def chemistry_questions():
    chemistry = [
        {
            'question': 'What is the chemical formula for methane?',
            'options': ['A) CH4', 'B) C2H6', 'C) CO2', 'D) CH3OH'],
            'answer': 'A'
        },
        {
            'question': 'Which element has the chemical symbol Au?',
            'options': ['A) Silver', 'B) Gold', 'C) Iron', 'D) Copper'],
            'answer': 'B'
        },
        {
            'question': 'What is the pH value of pure water at 25°C?',
            'options': ['A) 1', 'B) 7', 'C) 14', 'D) 10'],
            'answer': 'B'
        },
        {
            'question': 'Which acid is found in vinegar?',
            'options': ['A) Hydrochloric Acid', 'B) Acetic Acid', 'C) Sulfuric Acid', 'D) Nitric Acid'],
            'answer': 'B'
        },
        {
            'question': 'What is the common name for sodium chloride?',
            'options': ['A) Baking Soda', 'B) Table Salt', 'C) Epsom Salt', 'D) Cream of Tartar'],
            'answer': 'B'
        },
        {
            'question': 'Which gas is commonly used in balloons?',
            'options': ['A) Hydrogen', 'B) Helium', 'C) Oxygen', 'D) Nitrogen'],
            'answer': 'B'
        },
        {
            'question': 'What is the main component of natural gas?',
            'options': ['A) Ethylene', 'B) Methane', 'C) Propane', 'D) Butane'],
            'answer': 'B'
        },
        {
            'question': 'What type of bond is formed between two hydrogen atoms?',
            'options': ['A) Ionic Bond', 'B) Covalent Bond', 'C) Metallic Bond', 'D) Hydrogen Bond'],
            'answer': 'B'
        },
        {
            'question': 'Which element is essential for respiration in humans?',
            'options': ['A) Carbon', 'B) Oxygen', 'C) Nitrogen', 'D) Hydrogen'],
            'answer': 'B'
        },
        {
            'question': 'What is the chemical formula of sulfuric acid?',
            'options': ['A) H2SO4', 'B) HCl', 'C) HNO3', 'D) CH3COOH'],
            'answer': 'A'
        }
    ]
    for trials in chemistry:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        
        if answer == trials["answer"]:
            global score
            score += 10
        else:
        
            score += -10
def Biology_question():




    questiion =[
        {"question":"1.The process in which complex substances are broken down into simpler ones is referred to as",
         "option":["A.catabolism", "B.metabolism", "C.Tropism", "D.Anabolism"],
         "Answer":"A"
        },
        {"question":"2.The organ which is sensitive to light in Euglena is the",
         "option":["A.flagellum", "B.chloroplast", "C.eyespot", "D.gullet"],
         "Answer":"B"
        },
        {"question":"3.one of the function of the xylem is?",
         "option":["A.strengthening the stem", "B.manufacturing food", "C.reducing loss of water", "D.conducting manufactured food"],
         "Answer":"A"  
        },
        {"question":"4.which of the following is not characteristic of wind pollinated flowers?",
         "option":["A.stigmas are usually large and feathery", "B.nectar is usually absent", "C.the pollengrains have rough spiny surfaces", "D.the flowers are not scented"],
         "Answer":"C"
        },
        {"question":"5.some of the feathers of an animal are scales, teeth, nare and backbones.The animal is likely to be a?",
         "option":["A.toad", "B.bird", "C.lizard", "D.rat"],
         "Answer":"C"
        },
        {"question":"6.choose the sequence which represents the correct order of organisims in a food chain",
         "option":["A.Grass, snake, toad, grasshopper, hawk", "B.Grass, grasshopper, toad, hawk", "C.grass, grashopper, snake, toad, hawk", "D.grass, snake, toad, hawk"],
         "Answer":"B"
        },
        {"question":"7.which of the following is not regarded as a pollutant on a land or in air",
         "option":["A.smoke","B.nitrogen","C.noise","D.sulphur dioxide"],
         "Answer":"B"
        },
        {"question":"8.in the mammalian respiratory system.exchange of gases occur in the ?",
         "option":["A.lungs","B.bronchi","C.bronchioles","D.alveoli"],
         "Answer":"D"
        },
        {"question":"9.Aged erythrocytes are destroyed in the",
         "option":["A.pancreas","B.liver","C.lymph nodes","D.kidney"],
         "Answer":"B"
        },
        {"question":"10.which of the following food substances will produce a brick red colour when warmed with benedict's solution?",
         "option":["A.glucose","B.starch","C.egg white","D.maltose"],
         "Answer":"A"
        },
  
    ]
    for trials in questiion:
        print(trials["question"])
        for opt in trials["option"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        
        if answer == trials["Answer"]:
            global score
            score += 10
        else:
            
            score += -10
    print(score)
def physic_questions():

    physics = [
        {
            'question': 'What is the SI unit of force?',
            'options': ['A) Pascal', 'B) Newton', 'C) Joule', 'D) Watt'],
            'answer': 'B'
        },
        {
            'question': 'What is the acceleration due to gravity on the surface of the Earth?',
            'options': ['A) 9.8 m/s^2', 'B) 10 m/s^2', 'C) 8.9 m/s^2', 'D) 9.0 m/s^2'],
            'answer': 'A'
        },
        {
            'question': 'Which law states that for every action there is an equal and opposite reaction?',
            'options': ['A) Newton\'s First Law', 'B) Newton\'s Second Law', 'C) Newton\'s Third Law', 'D) Law of Universal Gravitation'],
            'answer': 'C'
        },
        {
            'question': 'What is the speed of light in a vacuum?',
            'options': ['A) 3 x 10^8 m/s', 'B) 1.5 x 10^8 m/s', 'C) 3 x 10^6 m/s', 'D) 3 x 10^10 m/s'],
            'answer': 'A'
        },
        {
            'question': 'What is the formula for calculating kinetic energy?',
            'options': ['A) KE = 1/2 mv^2', 'B) KE = mv', 'C) KE = mgh', 'D) KE = 1/2 mv'],
            'answer': 'A'
        },
        {
            'question': 'What does Ohm’s Law state?',
            'options': ['A) V = IR', 'B) P = IV', 'C) F = ma', 'D) E = mc^2'],
            'answer': 'A'
        },
        {
            'question': 'Which type of wave requires a medium to travel through?',
            'options': ['A) Electromagnetic Waves', 'B) Sound Waves', 'C) Light Waves', 'D) Radio Waves'],
            'answer': 'B'
        },
        {
            'question': 'What is the unit of electric resistance?',
            'options': ['A) Ohm', 'B) Ampere', 'C) Volt', 'D) Watt'],
            'answer': 'A'
        },
        {
            'question': 'Which principle explains the working of an airfoil?',
            'options': ['A) Bernoulli\'s Principle', 'B) Archimedes\' Principle', 'C) Pascal\'s Principle', 'D) Newton\'s Law of Cooling'],
            'answer': 'A'
        },
        {
            'question': 'What is the energy stored in a capacitor known as?',
            'options': ['A) Magnetic Energy', 'B) Electrical Energy', 'C) Kinetic Energy', 'D) Potential Energy'],
            'answer': 'B'
        },
        {
            'question': 'Which quantity is a measure of the amount of matter in an object?',
            'options': ['A) Mass', 'B) Weight', 'C) Volume', 'D) Density'],
            'answer': 'A'
        }
    ]
    for trials in physics:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        
        if answer == trials["answer"]:
            global score
            score += 10
        else:
            
            score += -10
def English_questions():
    english = [
        {
            'question': 'What is the past tense of "eat"?',
            'options': ['A) Eated', 'B) Ate', 'C) Eaten', 'D) Eating'],
            'answer': 'B'
        },
        {
            'question': 'Which of the following is a synonym for "happy"?',
            'options': ['A) Sad', 'B) Joyful', 'C) Angry', 'D) Bored'],
            'answer': 'B'
        },
        {
            'question': 'Choose the correct sentence:',
            'options': ['A) She don\'t like apples.', 'B) She doesn\'t like apples.', 'C) She doesn\'t likes apples.', 'D) She not like apples.'],
            'answer': 'B'
        },
        {
            'question': 'Which punctuation mark is used to show excitement?',
            'options': ['A) Period', 'B) Comma', 'C) Exclamation Mark', 'D) Question Mark'],
            'answer': 'C'
        },
        {
            'question': 'What is the plural form of "child"?',
            'options': ['A) Childs', 'B) Children', 'C) Childes', 'D) Childern'],
            'answer': 'B'
        },
        {
            'question': 'Which word is an adjective?',
            'options': ['A) Quickly', 'B) Happiness', 'C) Beautiful', 'D) Run'],
            'answer': 'C'
        },
        {
            'question': 'What is the antonym of "difficult"?',
            'options': ['A) Hard', 'B) Easy', 'C) Complicated', 'D) Challenging'],
            'answer': 'B'
        },
        {
            'question': 'Which of these is a proper noun?',
            'options': ['A) city', 'B) car', 'C) London', 'D) book'],
            'answer': 'C'
        },
        {
            'question': 'Identify the subject in the sentence: "The dog barks loudly."',
            'options': ['A) dog', 'B) barks', 'C) loudly', 'D) The'],
            'answer': 'A'
        },
        {
            'question': 'Which sentence is written in passive voice?',
            'options': ['A) The chef cooked the meal.', 'B) The meal was cooked by the chef.', 'C) The chef is cooking the meal.', 'D) The chef will cook the meal.'],
            'answer': 'B'
        },
        {
            'question': 'What is the correct form of the verb in the sentence: "She ___ to school every day."?',
            'options': ['A) go', 'B) goes', 'C) going', 'D) gone'],
            'answer': 'B'
        },
        {
            'question': 'Which word is a verb?',
            'options': ['A) House', 'B) Beautiful', 'C) Run', 'D) Happiness'],
            'answer': 'C'
        },
        {
            'question': 'Choose the correctly spelled word:',
            'options': ['A) Accross', 'B) Across', 'C) Aross', 'D) Arosss'],
            'answer': 'B'
        },
        {
            'question': 'Which of the following sentences is correct?',
            'options': ['A) He don\'t have any money.', 'B) He doesn\'t have no money.', 'C) He doesn\'t have any money.', 'D) He don\'t has any money.'],
            'answer': 'C'
        },
        {
            'question': 'What is the function of an adverb in a sentence?',
            'options': ['A) To describe a noun', 'B) To describe a verb', 'C) To connect clauses', 'D) To replace a noun'],
            'answer': 'B'
        },
        {
            'question': 'Identify the verb in the sentence: "She sings beautifully."',
            'options': ['A) She', 'B) sings', 'C) beautifully', 'D) the'],
            'answer': 'B'
        },
        {
            'question': 'What is the opposite of "accept"?',
            'options': ['A) Reject', 'B) Embrace', 'C) Receive', 'D) Approve'],
            'answer': 'A'
        },
        {
            'question': 'Which sentence is a question?',
            'options': ['A) It is raining.', 'B) I am tired.', 'C) Where are you going?', 'D) She sings well.'],
            'answer': 'C'
        },
        {
            'question': 'What is the correct form of the adjective in the sentence: "This book is ___ than that one."?',
            'options': ['A) more interesting', 'B) most interesting', 'C) interesting', 'D) interestinger'],
            'answer': 'A'
        },
        {
            'question': 'Choose the correct article for the sentence: "___ apple a day keeps the doctor away."',
            'options': ['A) A', 'B) An', 'C) The', 'D) No article'],
            'answer': 'B'
        },
        {
            'question': 'What is the plural of "mouse"?',
            'options': ['A) Mouses', 'B) Mice', 'C) Mouse', 'D) Mices'],
            'answer': 'B'
        },
        {
            'question': 'Which of the following is a preposition?',
            'options': ['A) Run', 'B) Under', 'C) Happy', 'D) Quickly'],
            'answer': 'B'
        },
        {
            'question': 'What is the past perfect form of the verb "to eat"?',
            'options': ['A) Eat', 'B) Eaten', 'C) Had eaten', 'D) Eating'],
            'answer': 'C'
        }
    ]
    for trials in english:
        print(trials["question"])
        for opt in trials["options"]:
            print(opt)
        print(" ")
        answer = input("ENTER CHOSEN OPTION HERE:").upper()
        
        if answer == trials["answer"]:
            global score
            score += 10
        else:
            
            score += -10

def intro_duc_tion():
    print("WELCOME TO ELEGANCE 2024 CBT EXAMINATION")
    print("THIS EXAMINATION CONTAINS  4 SUBJECTS AND 50 QUESTION ")
    print("THE GENERAL BIOLOGY CONTAINS 20 QUESTIONS AND OTHERS SUCH AS ENGLISH,CHEMISTRY AND PHYSICS CONTAINS 10 EACH")
    print(" ")

    print("""INSTRUCTION:1.DO NOT START UNTIL YOU TOLD TO DO SO
                2.DO NOT CHOOSE TWO OR MORE ANSWER IN ONE QUESTION
                3.DO NOT ENGAGED IN MALPRACTICE AS THIS AS SEVERE CONSEQUENCES 
                4.Answer should only be A,B,C or D""")
def command_to_start():
    print("Enter 'start' to begin")
    reply = input("ENTER HERE:").lower()
    if reply == "start":
        def start_again():
            print("what subject would like to start with")
            answer = input("ENTER HERE:").lower()
            if answer == "biology":
                Biology_question()
            elif answer == "physics":
                physic_questions()
            elif answer == "chemistry":
                chemistry_questions()
            elif answer == "english":
                English_questions()
            else:
                print("wrong input:Subject is not Available")
                start_again()
            def the_subject():
                print("what subject would like to do next")
                subject = input("ENTER:")
                if subject == answer:
                    print("you've have done or attempted this subject")
                elif answer == "physics":
                    physic_questions()
                elif subject == "chemistry":
                    chemistry_questions()
                elif subject == "english":
                    English_questions()
                elif subject == "biology":
                    Biology_question()
                else:
                    print("wrong input:Subject is not Available")
                    start_again()
                the_subject()
            the_subject()
    else :
        print('wrong input')
        command_to_start()
    start_again()
                
        

            

intro_duc_tion()
command_to_start()
Biology_question()
physic_questions()
English_questions()
chemistry_questions()


print(score)


    
 
       

        
            





