import random
mood_lists=["happy","sad","energetic","calm"]
random_mood=random.choice(mood_lists)
print(random_mood)

#2
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
moods_lists=["Happy","Sad","Enraged"]
time_day=["morning","afternoon","night"]
for days in week_days:
    for time in time_day:
        print(f"This {days} im feeling {random.choice(moods_lists)} during this {time}")

#3
counter=0
while counter >= 0:
    print("this is an infinite loop")
    counter +=1
    if counter >=5:
        break
while counter <10:
        counter += 1
        print(counter)

    

#4
game=["Apex","Elden Ring","Helldivers2","Ocarina Of Time"]

while True:
    rando_game=random.choice(game)
    user_guess=input("Please guess the game or enter quit to quit " )
    if user_guess=="quit":
         print("Thanks for playing")
         break
    elif user_guess==rando_game:
         print("Youve guessed the game correctly")
    else:
         print("Youre wrong")

#5
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
     genre=input("Please enter a genre: ")
     if genre=="Jazz":
          print(f"This is the second best genre")
     if genre=="Rock":
          print(f"This ones ok")
     if genre=="Hip-hop":
          print(f" THis is the best one")
     if genre=="Classical":
          print(f"Im good")
     if genre=="quit":
          break
print(genres)
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
while True:
     genre=input("Please enter a genre: ")
     if genre=="Jazz":
          print(f"This is the second best genre")
     if genre=="Rock":
          print(f"This ones ok")
     if genre=="Hip-hop":
          print(f" THis is the best one")
     if genre=="Classical":
          print(f"Im good")
     if genre=="quit":
          break

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
cut_genres=genres[1:]
for genres in cut_genres:
    print(cut_genres)










       

