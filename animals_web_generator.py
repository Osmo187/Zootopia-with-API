import data_fetcher


def generate_animal_html(animal):
    """Generates an HTML list item for a single animal."""
    characteristics = animal.get("characteristics", {})

    name = animal.get("name", "Unknown")
    diet = characteristics.get("diet", "Unknown")
    location = animal.get("locations", ["Unknown"])[0]

    type_html = ""
    if "type" in characteristics:
        type_html = f"<li><strong>Type:</strong> {characteristics['type']}</li>"

    html = f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <div class="card__text">
            <ul class="animal-details">
                <li><strong>Diet:</strong> {diet}</li>
                <li><strong>Location:</strong> {location}</li>
                {type_html}
            </ul>
        </div>
    </li>
    """
    return html


def generate_website(animal_name, animals):
    """Reads the template and generates the final HTML file."""
    with open("animals_template.html", "r") as f:
        template = f.read()

    if len(animals) == 0:
        animals_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        animals_html = ""
        for animal in animals:
            animals_html += generate_animal_html(animal)

    output = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as f:
        f.write(output)


def main():
    """Main function: asks user for animal name, fetches data, generates website."""
    animal_name = input("Enter a name of an animal: ")
    animals = data_fetcher.fetch_data(animal_name)
    generate_website(animal_name, animals)
    print("Website was successfully generated to the file animals.html.")


main()