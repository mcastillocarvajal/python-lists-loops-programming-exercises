def lyrics_generator(list):
    lyrics = ""
    count = 0

    for i in list:
        if i == 0:
            lyrics += "Boom "
        else:
            lyrics += "Drop the base "
            count += 1
            if count == 3:
                lyrics += "!!!Break the base!!! "
                count == 0
    return lyrics

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))