import json, os

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

os.makedirs("data", exist_ok=True)

def get_file_path(filename):
    with open(f"data/{filename}", "w", encoding="utf-8") as file:
        json.dump(chess_players, file, indent=4, ensure_ascii=False)
        return file.name


def read_file_content(filename):
    with open(f"data/{filename}", "r", encoding="utf-8") as file:
        return json.load(file)

def add_player(filename, player_dict):
    with open(f"data/{filename}", "r", encoding="utf-8") as file:
        data = json.load(file)

    data.append(player_dict) 
    with open(f"data/{filename}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def update_player(filename, player_id, updated_data):
    with open(f"data/{filename}", "r", encoding="utf-8") as file:
        data = json.load(file)

    for player in data:
        if player["id"] == player_id:
            player.update(updated_data)
            break

    with open(f"data/{filename}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



file_name = "chess_players.json"


path = get_file_path(file_name)
print(f"address: {path}\n")


new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

for player in new_players:
    add_player(file_name, player)


update_player(file_name, 84, {'rating': 2888, 'age': 35})


final_data = read_file_content(file_name)
print(json.dumps(final_data, indent=4, ensure_ascii=False))