MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []
title = input("Enter the movie title: ")
director = input("Enter the movie director: ")
year = input("Enter the movie release year: ")

movies.append({
    'title': title,
    'director': director,
    'year': year
})


while MENU_PROMPT !='q'
    if MENU_PROMPT =='l'
        print(movies)
    if MENU_PROMPT == 'f'
    input("Enter the movie title: ")
    

movies = []
title = input("Enter movie title: ")
director = input("Enter movie director: ")
year = input("Enter the movie release year: ")
                

selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        pass
    elif selection == "l":
        pass
    elif selection == "f":
        pass
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


movies = []
title = input("Enter movie title: ")
director = input("Enter movie director: ")
year = input("Enter the movie release year: ")
               
