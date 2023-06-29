import random
import datetime

random.seed()

movies = [
          'the grit',
          'blue velvet',
          'lost highway',
          'mulholland drive',
          'the elephant man',
          'the straight story',
          'wild at heart',
          'a short film about killing',
          'a short film about love', 
          'the double life of veronique',
          'three colors blue',
          'three colors red',
          'three colors white',
          'goodbye lenin',
          'night and fog',
          'the battle of algiers',
          'the young karl marx',
          'z',
          'boogie nights',
          'inherent vice',
          'licorice pizza',
          'magnolia',
          'phantom thread',
          'a serious man',
          '21',
          'groundhog day',
          'the hateful eight',
          'casino',
          'horible bosses',
          'thirst',
          'the handmaiden',
          'decision to leave',
          'in the mood for love',
          'chungking express',
          'fallen angels',
          'happy together',
          '2046',
          'days of being wild',
          'my bluebarry nights',
          'incendies',
          'the nights of cabiria',
          'late spring',
          'eternity and a day',
          'alein',
          'the third man',
          'all that jazz',
          'red beard',
          'double indemnity',
          'network',
          'throne of blood',
          'the celebration',
          'rashomon',
          'rocco and his brothers',
          'a special day',
          'whos afraid of virginia woolf?',
          'the man who shot liberty valance',
          'high and low',
          'yi yi',
          'a brighter summer day',
          'ikiru',
          'la haine',
          'the human condition trilogy',
          'tokyo story',
          'woman in the dunes',
          'mishima',
          'mr klein',
          'cure'
          ]

this_year = [
    'after sun',
    'tar',
    'the banshees of inisherin',
    'the fabelmans',
    'the northman',
    'avatar 2', 
    'dont worry darling',
]

stand_up = [
    'norms hitlers dog gossip and tricker',
    'norms nothing especial',
    'louis c.k back at the garden'
]

year = datetime.datetime.today().year 
random_movie = random.choice(movies)
random_this_year =random.choice(this_year)
random_stand_up = random.choice(stand_up)

choice = input(f"if you want to watch a random movie from {year} please enter number 1, if you wanna watch a random movie enter 2 and if you wanna watch stand-up comedy enter 3:\n")

if choice == '1':
    print(f"so you wanna watch a movie from {year}?\nlet me check what I've for you tonight... you have to watch: {random_this_year}. ")
    
elif choice == '2':
    print(f"so you have chosen... death.\njust kiddin, this is your movie sir: {random_movie}")

elif choice == '3':
    print(f"here is your special for the night sire: {random_stand_up}")
