#Step-1
def main():
    return
if __name__== '__main__':
 main()
#Step-2
full_name = {"full_name": "krunal brahmbhatt" }
student_id = {1: 10266566}
pizza_dict = {"pizza_toppings": ["pepperoni", "mushroom", "olives"]}
movies_dict = {"movies": [{"title": "the dark knight", "genre": "action"}, {"title": "the shawshank redemption", "genre": "drama"}]}
#Step-3
def main():
    movies_dict["movies"].append({"title": "The Godfather", "genre": "action"})
if __name__ == "__main__": 
    main()
#Step-4
def print_student_info(student_data):
    full_name = student_data["full_name"]
    first_name = full_name.split()[0]
    student_id = student_data["student_id"]

    print("My name is krunal_brahmbhatt, but you can call me Sir Krunal.".format(full_name, first_name))
    print("My student ID is 10266566.".format(student_id))

def main():
    student_data = {"full_name": "krunal brahmbhatt", "student_id": "10266566"}
    print_student_info(student_data)
if __name__ == "__main__":
    main()  
#Step-5 
def update_pizza_topings(data_structure, toppings_tuple):
    toppings_list = data_structure["pizza_toppings"]
    toppings_list.extend(toppings_tuple)
    toppings_list.sort(key=lambda s: s.lower())
    data_structure["pizza_toppings"] = [t.lower() for t in toppings_list]

def main():
    data_structure = {"pizza_toppings": ["pepperoni", "mushrooms"]}
    update_pizza_topings(data_structure, ("Onions", "Sausage"))

if __name__ == "__main__":
    main()
#Step-6
def print_pizza_toppings(toppings):
    print("My favourite pizza toppings are:")
    for i, topping in enumerate(toppings, start=1):
        print("-", topping)

# Call the function twice
toppings = ["pepperoni", "mushroom", "olives"]
print_pizza_toppings(toppings)
toppings = ["pepperoni", "mushroom", "olives", "Pineapple", "chicken", "cheese"]
print_pizza_toppings(toppings)
#Step-7
def print_movie_genres(movies):
    genres = [movie["genre"] for movie in movies]
    genres_string = ", ".join(genres[:-1])
    if len(genres) > 1:
        genres_string += " and " + genres[-1]
    else:
        genres_string += genres[0]
    print(f"I like to watch {genres_string} movies.")

# Call the function
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "The Godfather", "genre": "Crime"},
    {"title": "The Dark Knight", "genre": "Action"}
]
print_movie_genres(movies)
#Step-8
def print_favorite_movies(movies):
    titles = [movie["title"].title() for movie in movies]
    titles_string = ", ".join(titles[:-1])
    if len(titles) > 1:
        titles_string += " and " + titles[-1]
    else:
        titles_string += titles[0]
    print(f"Some of my favourite movies are {titles_string}!")

# Call the function
movies = [
    {"title": "the shawshank redemption", "genre": "Drama"},
    {"title": "the godfather", "genre": "Crime"},
    {"title": "the dark knight", "genre": "Action"}
]
print_favorite_movies(movies)