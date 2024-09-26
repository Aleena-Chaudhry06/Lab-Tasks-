# Movie dataset
movies = [("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)]

def calculate_average_budget(movie_list):
    total_budget = 0
    for movie in movie_list:
        total_budget += movie[1] 
    average_budget = total_budget / len(movie_list)
    print("The average movie budget is $",average_budget,",.2f")
    return average_budget

def display_high_budget_movies(movie_list, average_budget):
    count = 0
    for movie in movie_list:
        if movie[1] > average_budget:
            difference = movie[1] - average_budget
            print(movie[0], "has a budget higher than the average by $", difference, ",.2f")
            count += 1
    print("\nNumber of movies with a budget higher than the average: ", count)

def add_movies(movie_list):
    try:
        num_movies = int(input("How many movies would you like to add? "))
        for _ in range(num_movies):
            name = input("Enter the movie name: ")
            budget = int(input("Enter the movie budget: "))
            movie_list.append((name, budget))
    except ValueError:
        print("Please enter valid numbers.")

add_movies(movies)  
average_budget = calculate_average_budget(movies)  
display_high_budget_movies(movies, average_budget)
