import random

my_favorite_songs = [
['Waste a Moment', 3.03],
['New Salvation', 4.02],
['Staying\' Alive', 3.40],
['Out of Touch', 3.03],
['A Sorta Fairytale', 5.28],
['Easy', 4.15],
['Beautiful Day', 4.04],
['Nowhere to Run', 2.58],
['In This World', 4.02],
]

random_songs = random.sample(my_favorite_songs, 3) 
total_time = sum(song[1] for song in random_songs) 

print(f"Три песни звучат {total_time:.0f} минут") 

#Пункт B.
my_favorite_songs_dict = {
'Waste a Moment': 3.03,
'New Salvation': 4.02,
'Staying\' Alive': 3.40,
'Out of Touch': 3.03,
'A Sorta Fairytale': 5.28,
'Easy': 4.15,
'Beautiful Day': 4.04,
'Nowhere to Run': 2.58,
'In This World': 4.02,
}

random_songs_dict = random.sample(list(my_favorite_songs_dict.items()), 3) # случайные три песни
total_time_dict = sum(song[1] for song in random_songs_dict) # общее время звучания трех песен

print(f"Три песни звучат {total_time_dict:.0f} минут")

#Пункт C.
import random

my_favorite_songs = [
['Waste a Moment', 3.03],
['New Salvation', 4.02],
['Staying\' Alive', 3.40],
['Out of Touch', 3.03],
['A Sorta Fairytale', 5.28],
['Easy', 4.15],
['Beautiful Day', 4.04],
['Nowhere to Run', 2.58],
['In This World', 4.02],
]

random_songs = [random.choice(my_favorite_songs) for _ in range(3)] # случайные три песни
total_time = sum(song[1] for song in random_songs) # общее время звучания трех песен

print(f"Три песни звучат {total_time:.0f} минут")