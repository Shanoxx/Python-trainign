movies=["The Holy Grail", "Thr Life of brian", "The Meaning of Life"]
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(6, 1983)
print(movies)

for game_changer in movies:
    print(game_changer)

count=0
while count <len(movies):
    print(movies[count])
    count=count +1

names=['Lukasz', 'Magdalena', ['John', 'Noemi', ['Beatrix', 'Whitney', [1,2,3]]]]
isinstance(names, list)
licz_names=len(names)
isinstance(licz_names, list)

print(names[1])

for each_item in names:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for inner_list in nested_item:
                    if isinstance(inner_list, list):
                        for numbers in inner_list:
                            print(numbers)
                    else:
                        print(inner_list)
            else:
                print(nested_item)
    else:
        print(each_item)
the_list=[4,5,6]

def print_lol(the_list):
    for new in the_list:
        if isinstance(new, list):
            print_lol(new)
        else:
            print(new)
print_lol(names)