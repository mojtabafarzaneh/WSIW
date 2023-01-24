import random
import datetime

movies = ['no country for old man',
          'silence',
          'the tragedy of macbeth',
          'the grit','blue velvet',
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
          'after sun',
          'avatar',
          'das boot',
          'tar',
          'the banshees of inisherin',
          'the fabelmans',
          'top gun maveric',
          'the northman',
          'triangle of sadness',
          ]

this_year = [
    'after sun',
    'avatar',
    'das boot',
    'tar',
    'the banshees of inisherin',
    'the fabelmans',
    'top gun maveric',
    'the northman',
    'triangle of sadness',
]


year = datetime.datetime.today().year 
random_movie = random.choice(movies)
random_this_year =random.choice(this_year)

choice = input(f"if you want to watch a random movie from {year} please enter number 1, if you wanna watch a random movie enter 2:\n")
if choice == '1':
    print(f"so you wanna watch a movie from 2022?\nlet me check what I've for you tonight... you have to watch: {random_this_year}. ")
elif choice == '2':
    print(f"so you have chosen... death.\njust kiddin, this is your movie sir: {random_movie}")