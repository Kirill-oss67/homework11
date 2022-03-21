import json


# Первый шаг
def load_candidates_from_json():  # возвращает список всех кандидатов
    with open("candidates.json", "r", encoding='UTF-8') as f:
        list_candidates = json.load(f)
        return list_candidates

# ЗАГРУЗКА ВОПРОСОВ в список
list_candidates = load_candidates_from_json()

def get_candidate(candidate_id):# возвращает одного кандидата по его id
    for candidate in list_candidates:
        if candidate['id'] == candidate_id:
            return {
                'name' : candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found' : 'Не существует'}

def get_candidates_by_name(candidate_name):  # возвращает кандидатов по имени
   return [candidate for candidate in list_candidates if candidate_name.lower()  in candidate['name'].lower() ]


def get_candidates_by_skill(skill_name):# возвращает кандидатов по навыку
    our_list = []
    for candidate in list_candidates:
        skills = candidate['skills'].lower().split(', ') #получаем на итерации список скиллов данного персонажа
        if skill_name.lower() in skills:
            our_list.append(candidate)
    return our_list
