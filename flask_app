from flask import Flask, request, render_template_string
from pokemon_randomizer import Pokemon
import re

app = Flask(__name__)

main_page = """
<html>
	<body>
		<form method="POST" action="/">
			<input type="submit" value="Randomize"><br><br>
			<label>Pokemon:</label><br><br>
            <label>Ability:</label><br><br>
            <label><b>Moves</b></label><br><br>
		</form>
	</body>
</html>
"""

main_page2 = re.sub("(Pokemon:)", "\\1 {{ name }}", main_page)
main_page2 = re.sub("(Ability:)", "\\1 {{ ability }}", main_page2)
main_page2 = re.sub("(<b>Moves</b>)", "\\1<br>{{ moves|safe }}", main_page2)

@app.route("/", methods=["GET"])
def index():
	return main_page

@app.route("/", methods=["GET", "POST"])
def random_pokemon():
	if request.method == "POST":
		pkmn = Pokemon()
		template_data = {"name": pkmn.get_pokemon(), "ability": pkmn.get_ability(), "moves": pkmn.get_moves().replace("\n", "<br>")}
		return render_template_string(main_page2, **template_data)

if __name__ == "__main__":
	app.run()
