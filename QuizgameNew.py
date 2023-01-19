# this is a Quiz Game that is word puzzles and trivia. the game has a theme. the games can be configured: 
# number of players and type of game can be selected


#data sets
general_knowledge = { "What is the capital of France?": "Paris", "What is the currency of Japan?": "Yen", "What is the highest mountain in the world?": "Mount Everest", "What is the largest ocean in the world?": "Pacific Ocean", "What is the smallest country in the world?": "Vatican City", "What is the largest mammal in the world?": "Blue Whale", "What is the most populous city in the world?": "Tokyo", "What is the longest river in the world?": "Nile River", "What is the tallest mammal in the world?": "Giraffe", "What is the most populous country in the world?": "China", "What is the capital of Australia?": "Canberra", "What is the currency of Canada?": "Canadian dollar", "What is the highest peak in North America?": "Denali", "What is the largest desert in the world?": "Antarctic Desert", "What is the smallest continent in the world?": "Australia", "What is the largest bird in the world?": "Ostrich", "What is the most populous continent in the world?": "Asia", "What is the capital of Germany?": "Berlin", "What is the currency of Mexico?": "Mexican peso", "What is the highest point in Africa?": "Mount Kilimanjaro" }

british_history = { "Who was the first Tudor monarch of England?": "Henry VII", "Who was the first Stuart monarch of England?": "James I", "Who was the last Tudor monarch of England?": "Elizabeth I", "Who was the last Stuart monarch of England?": "Anne", "When did the War of the Roses end?":"1485", "What was the name of the treaty that established the end of the Hundred Years' War?": "Treaty of Troyes", "When did the Magna Carta signed?": "1215", "Who was the leader of the Roundheads during the English Civil War?":"Oliver Cromwell", "When was the Battle of Waterloo fought?": "1815", "What was the name of the queen who ruled England before Victoria?": "Elizabeth II", "When was the Great Fire of London?": "1666", "What was the name of the queen who ruled England before Elizabeth II?": "Elizabeth I", "When was the Industrial Revolution in Britain?":"1760-1840", "Who was the leader of the Jacobites during the Jacobite Rising of 1745?": "Charles Edward Stuart", "When was the Battle of Britain fought?":"1940", "What was the name of the queen who ruled England before Elizabeth I?":"Mary I", "When was the Battle of Trafalgar fought?":"1805", "Who was the leader of the Jacobites during the Jacobite Rising of 1689?":"Viscount Dundee", "When was the Battle of Agincourt fought?":"1415", "What was the name of the queen who ruled England before Mary I?":"Jane Grey" }

kings_and_queens_of_rock = { "Who is known as the 'King of Rock and Roll'?": "Elvis Presley", "Who is known as the 'Queen of Rock and Roll'?": "Tina Turner", "Who is known as the 'Godfather of Soul'?": "James Brown", "Who is known as the 'King of the Blues'?": "B.B. King", "Who is known as the 'Queen of Soul'?": "Aretha Franklin", "Who is known as the 'King of Pop'?": "Michael Jackson", "Who is known as the 'Queen of Pop'?": "Madonna", "Who is known as the 'King of Punk'?": "Iggy Pop", "Who is known as the 'Queen of Punk'?": "Patti Smith", "Who is known as the 'King of Metal'?": "Ozzy Osbourne", "Who is known as the 'Queen of Metal'?": "Lita Ford", "Who is known as the 'King of Rockabilly'?": "Elvis Presley", "Who is known as the 'Queen of Rockabilly'?": "Wanda Jackson", "Who is known as the 'King of Country'?": "George Strait",}

game_theme = input("Select 1 for General Knowledge, 2 for British History, 3 for Kings and Queens of Rock!  ")
print (game_theme)
game_data = {}
if game_theme == "1":
    game_data = general_knowledge
else:
    if game_theme == "2":
        game_data = british_history
    else:
        if game_theme == "3":
            game_data = kings_and_queens_of_rock

print (game_data)
#if (game_theme != 1) and (game_theme != 2) and (game_theme != 3):
#    print ("Bad selection try again")


