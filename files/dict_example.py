example = {} # creates empty dict.
example = dict() # creates empty dict.

'''
case sensitive and the key needs to be unique, if the key is the same it will overwrite the list
'''

example["horror"] = "Alien"
example["romcom"] = "When Harry Met Sally"
example["thriller"] = "The Manchurian Candidate"
example["music video"] = "Thriller"
example["horror"] = "Friday the 13th"
example["Horror"] = "Nightmare on Elm street"

print(example)
# example.pop('horror') # removes horror
horrorFilm = example.pop("horror") #took it out of the dictionary and stashed it in the variable
# print(f"{horrorFilm}"), # {example["horror"]}")

costumeDrama = example.get('costume drama') # should produce none
costumeDrama = example.get('costume drama', "Alexander") # will give Alexander as the default
print(costumeDrama)

del example["music video"] # deletes the key and value

print(example)
# example.clear() # delete the whole dictionary
print(list(example.keys())) # changes the dict keys into a list

numbers = [1,2,3,4,3,2,3,1,3,2,3,4,1,1,1,4,1]
counter = dict() # empty to count in

for nums in numbers:
    if nums in counter:
        counter[nums] +=1
    else:
        counter[nums] = 1
# print(counter)

all_values = sorted(counter.values())
highest_frequency = all_values [-1]
for kv_pair in counter.items(): # for key value pair in the dictionary 'counter'
    if highest_frequency == kv_pair[1]:
        print("Mode is " + str(kv_pair[0]))
for kv_pair in counter: # for key value pair in the dictionary 'counter'
    print(kv_pair)

for kv_pair in counter.keys(): # for key in key value pair in the dictionary 'counter'
    print(kv_pair)

for kv_pair in counter.values(): # for value in key value pair in the dictionary 'counter'
    print(kv_pair)