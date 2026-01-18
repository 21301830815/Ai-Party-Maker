import os
import random
import json
from .AiLogic.ai_users import ai_users_list

def appointed_roles():
    mafia_members = random.sample(ai_users_list, 2)
    mafia_list = [player.name for player in mafia_members]
    if not os.path.exists('private_data'):
        os.makedirs('private_data')
    for player in mafia_list:
        player.mafia = True
    for player in ai_users_list:
        private_info = {
            "name": player.name,
            "mafia": player.mafia,
            "role_description": "Ты мафия и должен убивать и не вызывать подозрений" if player.mafia else "Ты мирный и должен найти мафию"
        }

    with open(f'private_data/{player.name}.json', 'w', encoding='utf-8') as file:
        json.dump(private_info, file, ensure_ascii=False, indent=4)

    return [player.name for player in ai_users_list]
