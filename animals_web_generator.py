
import json

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"



def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_htlm(template):
    with open(template,"r") as file:
        return file.read()

def animal_display(animals_data):
    output =""
    for animal in animals_data:
        output += f'name: {animal["name"]}\n'
        output += f'diet: {animal["characteristics"]["diet"]}\n'
        output += f'location: {animal["locations"][0]}\n'
        if "type" in animal["characteristics"]:
            output += f'type: {animal["characteristics"]["type"]}\n'
    return(output)

def create_html(replace_data):
    with open("animals.html", "w") as new_file:
        return new_file.write(replace_data)

def main():
    animals_data = load_data('animals_data.json')
    print(animals_data)
    html=load_htlm("animals_template.html")
    output = animal_display(animals_data)
    replace_data = html.replace("__REPLACE_ANIMALS_INFO__", output)
    animals_html = create_html(replace_data)



if __name__ == "__main__":
    main()