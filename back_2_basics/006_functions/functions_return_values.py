#8-6

#Function that returns the value of a string (formats it with title() method first)
def city_country(city, country):
    """Returns a formatted string of City, Country"""

    location = f"{city}, {country}"
    return location.title() 

#New variable set to the value returned by function
formatted_country = city_country('atlanta', 'USA')
print(formatted_country)

formatted_country = city_country('madrid', 'SPAIN')
print(formatted_country)

formatted_country = city_country('kingston', 'JamAIca')
print(formatted_country)


#8-7, 8
def make_album(artist_name, album_title, song_amount=None):
    """Returns dictionary with album information. Amount of songs optional"""

    album = {'artist' : artist_name, 'album' : album_title,}
    #Only add the song_amount value to the dictionary if it is provided
    #Value of "None" is false in a boolean condition
    if song_amount:
        album['songs'] = song_amount
    
    return album

discography = make_album('Kanye West', "My Beutiful Dark Twisted Fantasy")
print(discography)

discography = make_album('50 Cent', 'Get Rich or Die Tryin')
print(discography)

discography = make_album('Lish Speaks', 'Please Use Exact Change', 10)
print(discography)

#Taking user input and passing using those values as function parameters
#Infinite loop without the break points
while True:
    print("\nPlease enter the artists' name and album title: ")
    print("(enter q at any time to quit)")

    artist = input("Artist Name: ")
    if artist == "q":
        break

    album = input('Album Title: ')
    if album == 'q':
        break

    songs_known = input("Do you know the number of songs? y or n: ")
    if songs_known == 'q':
        break
    elif songs_known == 'y':
        songs_num = input("Enter the number of songs on the album: ")

        discography = make_album(artist, album, songs_num)
    else:
        discography = make_album(artist, album)

    print(discography)