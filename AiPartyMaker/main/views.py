from django.shortcuts import render
from .AiLogic.ai_users import ai_users_list
import json

game = None
def index(request):
    return render(request, 'main/index.html')


def setup_mafia(request):
    if request.method == "POST":
        game = "mafia"
    return render(request, 'main/setup_mafia.html', {'all_models': ai_users_list})

def start_game(request):
    raw_data = request.POST.get('final_order')
    queue = json.loads(raw_data)

    with open('mafia.json', 'r', encoding='utf-8') as file:
        full_data = json.load(file)

    full_data['players_queue'] = new_queue
    with open('mafia.json', 'w', encoding='utf-8') as file:
        json.dump(full_data, file, ensure_ascii=False, indent=4)