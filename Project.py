from posixpath import split
import json
from colorama import Fore, Style

####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             Getting recipes data from Json file
####------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Getting recipes data from json file:
with open('Recipes.json', "r", encoding='utf-8') as f:
    recipes_json = json.load(f)
recipes = recipes_json["Recipes"]

# getting unique Recipes Categories
List_of_Categories = []
for i in range(len(recipes)):
  List_of_Categories.append(recipes[i]["Category"])
Set_of_Categories = set(List_of_Categories)

####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                Prep Functions for Option 1
####------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#Function to take new kitchen kontent input
def take_NEW_kitchen_content():
    input_values = input("what's cookin, good lookin. what's edable in your kitchen?"+Fore.BLUE+"(format: ingredients,separeted by comma)\n\n" + Fore.GREEN)
    print(Style.RESET_ALL)
    with open('Kitchen_content.txt', 'w') as f:
      f.write(input_values)
    input_values = input_values.lower().split(",")
    formated_input_values = [i.strip() for i in input_values] + ['salt','pepper','oil', 'vinegar', 'water']
    return formated_input_values

#Function to take previous or edited kitchen kontent output
def take_user_input_UserOption1():
  with open('Kitchen_content.txt') as f:
    content = f.read()
  if len(content) == 0:
    return take_NEW_kitchen_content()
  else:
    kitchen_content = input("To provide new kitchen content ->Press 'n'\nTo use kitchen content from the previous time ->Press 'p'\nTo edit previous kitchen kontent ->Press 'e \nTo quit ->Press 'q'\n\n"+Fore.GREEN)
    print(Style.RESET_ALL)
    if kitchen_content == 'n' or kitchen_content =="N":
      return take_NEW_kitchen_content()
    elif kitchen_content == 'p' or kitchen_content =="P":
      with open('Kitchen_content.txt') as f:
        content = f.read()
      input_values = content  
      input_values = input_values.lower().split(",")
      formated_input_values = [i.strip() for i in input_values] + ['salt','pepper','oil', 'vinegar', 'water']
      return formated_input_values
    elif kitchen_content == 'e' or kitchen_content =="E":
      with open('Kitchen_content.txt') as f:
        content = f.read()
      input_values = content 
      print("Here is what you had before:\n\n")
      print(input_values)
      edited_kitchen_content = input("\n\nProvide your edited kitchen content\n\n"+Fore.GREEN)
      print(Style.RESET_ALL)
      with open('Kitchen_content.txt', 'w') as f:
        f.write(edited_kitchen_content)
      input_values = edited_kitchen_content.lower().split(",")
      formated_input_values = [i.strip() for i in input_values] + ['salt','pepper','oil', 'vinegar', 'water']
      return formated_input_values
    elif kitchen_content == 'q' or kitchen_content =="Q":
      print("\n Come back soon!\n\n")
      exit()
    else:
      return take_user_input_UserOption1()



# When there are no results for a user, he/she can run the program again
def try_again():
  input_try_again = input("\n Would you like to try again? Press 'y' if YES, press 'q' if you want to QUIT.\n\n" + Fore.GREEN)
  print(Style.RESET_ALL)
  if input_try_again == 'y' or input_try_again == 'Y':
      _main_()
  elif input_try_again == 'q' or input_try_again == 'Q':
    print("\n Come back soon!\n\n")
    exit()
  else:
    print("\n Please, follow the instructions:\n\n")
    try_again()

####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                Prep Functions for Option 2
####------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Function to find recipes containing main ingredients, provided by user
def find_recipes_with_main_ingredient():
  input_main_ingredients = input("Type your desired main ingredients"+Fore.BLUE+"(through comma, if there are more than one ingredient)\n\n"+Fore.GREEN)
  print(Style.RESET_ALL)
  input_main_ingredients = input_main_ingredients.lower().split(",")
  formated_input_main_ingredients = [i.strip() for i in input_main_ingredients]
  list_to_offer = []
  for j in recipes:
    for i in formated_input_main_ingredients:
      x = True
      if i in j["Ingredients"]:
        continue
      else:
        x = False
        break
    if x == True:
      list_to_offer.append(j)
  return list_to_offer


####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                Prep Functions for Option 3
####------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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
  Name = input("\n What is the Name of your recipe? \n \n" + Fore.GREEN)
  print(Style.RESET_ALL)
  Ingredients_raw = input("\n List all ingredients for this recipe, separeting by comma \n \n" + Fore.GREEN)
  print(Style.RESET_ALL)
  Ingredients = Ingredients_raw.split(",")
  Ingredients = [i.strip() for i in Ingredients]
  Category = input(f"\n Write a Category from existing categories, or write your own.\n Existing Categories: {Set_of_Categories} \n \n" + Fore.GREEN)
  print(Style.RESET_ALL)
  Instructions_raw = input("\n Write your text instructions here. In case you want to provide only a link to Video instructions -> Press 'v'\n \n" + Fore.GREEN)
  print(Style.RESET_ALL)
  if Instructions_raw == "v" or Instructions_raw =="V":
    Instructions = "Not available"
  else:
    Instructions = Instructions_raw
  Video_link_raw = input("\n Provide a link to video instructions here. If it is not available, press 'n' \n \n" + Fore.GREEN)
  print(Style.RESET_ALL)
  if Video_link_raw == "n" or Video_link_raw == "N":
    Video_link = "Not available"
  else:
    Video_link = Video_link_raw
  Picture_link_raw = input("\n Provide a link to a picture of your dish. If it is not available, press 'n' \n \n" + Fore.GREEN)
  print(Style.RESET_ALL)
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
def Check_input_with_user_and_store_it(user_input):
    print(Fore.BLUE + "---------------------------------------------------------------------------------------------------"+Style.RESET_ALL)
    for key, value in user_input.items():
      print(f"\n {Fore.MAGENTA}{key}:{Style.RESET_ALL} {value}")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------------------"+Style.RESET_ALL)
    check_correct_input = input(f"\n Is this recipe correct? If YES -> Press 'y', if you would like rewrite it -> Press 'r'.If you want to quit -> Press 'q'.\n \n" +Fore.GREEN)
    print(Style.RESET_ALL)
    if check_correct_input == "r" or check_correct_input =="R":
      new_recipe_from_a_user()
    elif check_correct_input == "y" or check_correct_input =="Y":
      write_json(user_input)
      print("\n Your recipe is stored\n\n")
    elif check_correct_input == "q" or check_correct_input == "Q":
      print("Come back soon!\n\n")
      return
    else: 
      print("\n Please, follow the instructions:")
      Check_input_with_user_and_store_it(user_input)





####------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                 Option 1 :
####-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def based_on_fridge_recipes():
  input = take_user_input_UserOption1() 
  output = match_recipes_list_to_the_user_list_UserOption1(input)
  if(len(output) == 0):
    print("\n really! that's all?? look in your cabinets! THIS IS NOT ENOUGH!")
    try_again()  
  else:
    for key,values in output.items():
      print("\n")
      print(Fore.BLUE + "---------------------------------------------------------------------------------------------")
      print(Style.RESET_ALL)
      print(f"{Fore.MAGENTA}Dish Name #{str(key)}:{Style.RESET_ALL} {values['Name'].capitalize()} \n")
      print(Fore.MAGENTA + "Dish ingredients:"+Style.RESET_ALL + str(values['Ingredients'])+ "\n")
      print(f"{Fore.MAGENTA}Video link:{Style.RESET_ALL} {values['Video_link']} \n")
      print(f"{Fore.MAGENTA}Picture link:{Style.RESET_ALL} {values['Picture_link']} \n")
      print(Fore.MAGENTA + "Instructions to follow: " + Style.RESET_ALL+ values['Instructions']+ "\n")
      print("Enjoy your meal.")
      print(Fore.BLUE + "---------------------------------------------------------------------------------------------")
      print(Style.RESET_ALL)

  
####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                 Option 2 
####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main_ingredients_recipes():
  recipes_to_offer_list = find_recipes_with_main_ingredient()
  print(f"You can cook the following meals using the entered main ingredient : \n\n")
  for recipe in range(len(recipes_to_offer_list)):
    print(f"{recipe+1} : {Fore.MAGENTA} {recipes_to_offer_list[recipe]['Name']} {Style.RESET_ALL} {recipes_to_offer_list[recipe]['Ingredients']}\n")
  meal_choice = int(input(Fore.BLUE + "Please enter the meal index (like 1, 2, 3) to see its recipe: \n\n"+Fore.GREEN))
  print(Style.RESET_ALL)
  if meal_choice>0 and meal_choice<len(recipes_to_offer_list)+1:
    print(Fore.BLUE + "---------------------------------------------------------------------------------------------")
    print(Style.RESET_ALL)
    print(f"{Fore.MAGENTA}Dish Name #{str(meal_choice)}:{Style.RESET_ALL} {recipes_to_offer_list[meal_choice-1]['Name'].capitalize()} \n")
    print(Fore.MAGENTA + "Dish ingredients:"+Style.RESET_ALL + str(recipes_to_offer_list[meal_choice-1]['Ingredients'])+ "\n")
    print(f"{Fore.MAGENTA}Video link:{Style.RESET_ALL} {recipes_to_offer_list[meal_choice-1]['Video_link']} \n")
    print(f"{Fore.MAGENTA}Picture link:{Style.RESET_ALL} {recipes_to_offer_list[meal_choice-1]['Picture_link']} \n")
    print(Fore.MAGENTA + "Instructions to follow: " + Style.RESET_ALL+ recipes_to_offer_list[meal_choice-1]['Instructions']+ "\n")
    print("Enjoy your meal.")
    print(Fore.BLUE + "---------------------------------------------------------------------------------------------")
    print(Style.RESET_ALL)
    shoping_list_input = input("To see what you have to buy to cook your dish -> Press 'y'.\nTO quit -> Press 'q'\n\n"+Fore.GREEN)
    print(Style.RESET_ALL)
    if shoping_list_input == 'y' or shoping_list_input=='Y':
      with open('Kitchen_content.txt') as f:
        content = f.read()
      kitchen_content = content  
      kitchen_content = kitchen_content.lower().split(",")
      formated_kitchen_content = [i.strip() for i in kitchen_content]
      shoping_list_to_offer = []
      for ingredient in recipes_to_offer_list[meal_choice-1]['Ingredients']:
        if ingredient in formated_kitchen_content:
          continue
        else:
          shoping_list_to_offer.append(ingredient)
      for item in range(len(shoping_list_to_offer)):
        print(f"\n{item+1} : {shoping_list_to_offer[item]} ") 
  else:
    print("There is no such Id in the list\n\n")
    return try_again()

  

####----------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                 Option 3:
####----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Adding new recipe from a user to json file
def new_recipe_from_a_user():
  Recipe_to_append_to_json = take_input_recipe_from_user()
  Check_input_with_user_and_store_it(Recipe_to_append_to_json)




###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             Start of Recipes Finder
###----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def _main_():
  
  intro_input = input("\n If you want to see possible recipes based only on what you have in your fridge: Press '1'.\n If you want to cook from the core ingredients, which you already know: Press '2'.\n If you want to store your own recipe for the future usage: Press '3'.\n If you want to quit: Press 'q'\n \n"+Fore.GREEN)
  print(Style.RESET_ALL)
  if intro_input == '1' :
    based_on_fridge_recipes()
  elif intro_input == '2' :
    main_ingredients_recipes()
  elif intro_input == '3' :
    new_recipe_from_a_user()
  elif intro_input == 'q' or intro_input == "Q" :
    return print("\n Come back soon!\n\n")
  else:
    print("\n Please, follow the instructions:\n\n")
    _main_()
  
_main_()  

