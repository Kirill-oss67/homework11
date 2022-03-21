from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

# ЗАГРУЗКА ВОПРОСОВ в список
list_candidates = load_candidates_from_json()

# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('list.html', items=list_candidates)


@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = get_candidate(uid)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<name>")
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, len_list = len(candidates))


@app.route("/skills/<name_skill>")
def skills(name_skill):
    candidates = get_candidates_by_skill(name_skill)
    return render_template('skill.html', candidates = candidates, len_list = len(candidates),skill = name_skill )


app.run(debug=True)
