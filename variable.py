#variables

name = 'jane' #string
print(name)

songs = 20  #integer
print(songs)

rating = 8.3   #float
print(rating)

male = True #boolean
print(male)

music_genres = ('Rock', 'EDM', 'Pop', 'Indie')  #tuple
print(music_genres)

band_members = ['stefanie', 'alice', 'james'] #list
print(band_members)

cars = {1: 'Toyota', 2: 'Subaru', 3:'Ford', 4:'Chevrolet'}  #dictionary
print(cars)

#scopes

other_city = 'Mombasa' #init global scope

def place():
    city = 'Mombasa'    #init local scope
    print(city)

place()
print(other_city)