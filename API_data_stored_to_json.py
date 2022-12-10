
import requests
import json

# list of the English alphabet
import string
alphabet = list(string.ascii_lowercase)

# list of urls
request_url_list = ["https://www.themealdb.com/api/json/v1/1/search.php?f="+i for i in alphabet]

# storing all recipes from api to a list
api_data_list=[]
for request_url in request_url_list:
  response_content = requests.get(request_url).json()
  if type(response_content['meals']) is list:
    api_data_list = api_data_list + response_content['meals']

# making our structure from api data
api_recipes =[]
for list_element in range(len(api_data_list)):
    recipe_list_element = {
                    "Id" : list_element+1,
                    "Name" : api_data_list[list_element]['strMeal'],
                    "Category" : api_data_list[list_element]['strCategory'],         
                    "Instructions" : api_data_list[list_element]['strInstructions'],
                    "Picture_link" : api_data_list[list_element]['strMealThumb'],
                    "Video_link" : api_data_list[list_element]['strYoutube'],
                    "Ingredients" : [api_data_list[list_element]['strIngredient'+str(i+1)].lower() for i in range(20) if (api_data_list[list_element]['strIngredient'+str(i+1)])!="" and type(api_data_list[list_element]['strIngredient'+str(i+1)]) is str],
                                       }
    api_recipes.append(recipe_list_element)

#Creating json file and storing formated api data there
json_recipes = {"Recipes" : api_recipes}

with open('Recipes_.json', 'w', encoding='utf-8') as f:
    json.dump(json_recipes, f, ensure_ascii=False, indent=4)