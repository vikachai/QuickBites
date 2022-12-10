from posixpath import split
import json

#Getting recipes data from json file:
with open('Recipes.json', "r", encoding='utf-8') as f:
    recipes_json = json.load(f)
recipes = recipes_json["Recipes"]

# getting unique Recipes Categories
List_of_Categories = []
for i in range(len(recipes)):
  List_of_Categories.append(recipes[i]["Category"])
Set_of_Categories = set(List_of_Categories)

# function to find all recipes, where list of ingredients
#  can be fully found in provided list of products by a user
def match_recipes_list_to_the_user_list_UserOption1(a_user_list):
  list_to_offer = []

  for d in recipes:
    ings = d["Ingredients"]  
    for item in ings:
      x = True
      if item in a_user_list:
        continue
      else:
        x = False
        break
    if x == True:  
      list_to_offer.append(d)
  
  dict_to_offer ={}
  for i in range(len(list_to_offer)):
    dict_to_offer[i+1] = list_to_offer[i]
  return dict_to_offer

#Storing input(products in a user's fridge) in a list
#Formating this list
## Not done yet -  add lowercase to input_values
def take_user_input_UserOption1():
    while True:
      input_values = input("what's cookin, good lookin. what's edable in your kitchen? ")
      if not input_values :
        continue
      input_values = input_values.split(",")
      formated_input_values = [i.strip() for i in input_values] + ['salt','pepper','oil', 'vinegar', 'water']
      return formated_input_values

# When there are no results for a user, he/she can run the program again
def try_again():
  input_try_again = input("\n Would you like to try again? Press 'y' if YES, press 'q' if you want to QUIT.")
  if input_try_again == 'y' or input_try_again == 'Y':
      _main_()
  elif input_try_again == 'q' or input_try_again == 'Q':
    return print("\n Come back soon!")
  else:
    print("\n Please, follow the instructions:")
    try_again()




# function to add to JSON
def write_json(new_data, filename='Recipes.json'):
    with open(filename,'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data["Recipes"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, ensure_ascii=False, indent = 4)
 

# function to take data(recipe) from a user 
# and to create python object from that data to be appended to json file

      ###User Input
def take_input_recipe_from_user():
  Name = input("\n What is the Name of your recipe? \n")
  Ingredients_raw = input("\n List all ingredients for this recipe, separeting by comma \n")
  Ingredients = Ingredients_raw.split(",")
  Ingredients = [i.strip() for i in Ingredients]
  Category = input(f"\n Write a Category from existing categories, or write your own.\n Existing Categories: {Set_of_Categories} \n")
  Instructions_raw = input("\n Write your text instructions here. In case you want to provide only a link to Video instructions -> Press 'v' \n")
  if Instructions_raw == "v" or Instructions_raw =="V":
    Instructions = "Not available"
  else:
    Instructions = Instructions_raw
  Video_link_raw = input("\n Provide a link to video instructions here. If it is not available, press 'n' \n")
  if Video_link_raw == "n" or Video_link_raw == "N":
    Video_link = "Not available"
  else:
    Video_link = Video_link_raw
  Picture_link_raw = input("\n Provide a link to a picture of your dish. If it is not available, press 'n' \n")
  if Picture_link_raw == "n" or Picture_link_raw == "N":
    Picture_link = "Not available"
  else:
    Picture_link = Picture_link_raw
  Id = len(recipes)+1

      ###An element to append
  Recipe_to_append = {
      "Id" : Id,
      "Name" : Name,
      "Category" : Category,         
      "Instructions" : Instructions,
      "Picture_link" : Picture_link,
      "Video_link" : Video_link,
      "Ingredients" : Ingredients
    } 
  return Recipe_to_append


###Function Checking with a user if the provided data by him is correct:
def Check_input_with_user(user_input):
    for key, value in user_input.items():
      print(f"\n {key}: {value}")
    check_correct_input = input(f"\n Is this recipe correct? If YES -> Press 'y', if you would like rewrite it -> Press 'r'.\n")
    if check_correct_input == "r" or check_correct_input =="R":
      new_recipe_from_a_user()
    elif check_correct_input == "y" or check_correct_input =="Y":
      write_json(user_input)
      print("\n Your recipe is stored")
    else: 
      print("\n Please, follow the instructions:")
      Check_input_with_user(user_input)

####------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 1 :
##Not done yet - to add an option to choose a category?
def based_on_fridge_recipes():
  output = match_recipes_list_to_the_user_list_UserOption1(take_user_input_UserOption1())
  if(len(output) == 0):
    print("\n really! that's all?? look in your cabinets! THIS IS NOT ENOUGH!")
    try_again()  
  else:
    for key,values in output.items():
      print("\n")
      print(f"Dish Name #{str(key)}: {values['Name'].capitalize()} \n")
      print("Dish ingredients:" + str(values['Ingredients'])+ "\n")
      print(f"Video link: {values['Video_link']} \n")
      print(f"Picture link: {values['Picture_link']} \n")
      print("Instructions to follow: " + values['Instructions']+ "\n")
      print("Enjoy your meal.")
  

#Option 2 - Not done yet:
def core_ingredients_recipes():
  pass

#Option 3:
# Adding new recipe from a user to json file
def new_recipe_from_a_user():
  Recipe_to_append_to_json = take_input_recipe_from_user()
  Check_input_with_user(Recipe_to_append_to_json)


###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Start of quick bites
def _main_():
  intro_input = input("\n If you want to see possible recipes based only on what you have in your fridge: Press '1'.\n If you want to cook from the core ingredients, which you already know: Press '2'.\n If you want to store your own recipe for the future usage: Press '3'.\n If you want to quit: Press 'q'\n")
  if intro_input == '1' :
    based_on_fridge_recipes()
  elif intro_input == '2' :
    core_ingredients_recipes()
  elif intro_input == '3' :
    new_recipe_from_a_user()
  elif intro_input == 'q' or intro_input == "Q" :
    return print("\n Come back soon!")
  else:
    print("\n Please, follow the instructions:")
    _main_()
  
_main_()  

