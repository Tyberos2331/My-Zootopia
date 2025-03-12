
import json

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def animal_display(animals_data):
    for animal in animals_data:
        print(f'name: {animal["name"]}'  )
        print(f'diet: {animal["characteristics"]["diet"]}' )
        print(f'location: {animal["locations"][0]}')
        if "type" in animal["characteristics"]:
            print(f'type: {animal["characteristics"]["type"]}')
        print()



def main():
    animals_data = load_data('animals_data.json')
    print(animals_data)
    animal_display(animals_data)


if __name__ == "__main__":
    main()