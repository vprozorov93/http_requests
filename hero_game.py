import requests


def _get_heroes():
    url = 'https://superheroapi.com/ids.html'
    response = requests.get(url=url, headers={'User-agent': 'prozorov-agent'})
    start_pos = response.text.find('\t\t<!-- Main content -->\n') + 8
    end_pos = response.text.find('</main>')
    hero_list = response.text[start_pos:end_pos].split('\n')
    hero_dict = {}
    last_id = 0
    for item in hero_list:
        if '<td>' in item and '</td>' in item:
            item = item.lstrip()
            item = item.lstrip('<td>')
            item = item.rstrip('</td>')
            if item.isdigit():
                last_id = item
            else:
                hero_dict[last_id] = item
    return hero_dict


def _choose_hero():
    heroes = _get_heroes()
    for index, hero_nickname in heroes.items():
        if int(index) % 100 == 0:
            input('Press any key for look next 100 heroes')
        print(f'[{index}] {hero_nickname}')

    while True:
        hero_num = input('Choose number of hero: ')
        if hero_num.isdigit():
            if heroes.get(hero_num) is not None:
                break
            else:
                print(f'Hero with [{hero_num}] number is not found')
        else:
            print(f'[{hero_num}] is not number of heroes')

    return heroes[hero_num]


def get_hero_stat():
    hero = _choose_hero()
    url = 'https://superheroapi.com/api/2619421814940190/search/' + hero
    response = requests.get(url=url, headers={'User-agent': 'prozorov-agent'})
    return hero, response.json()['results'][0]['powerstats']


class Hero:

    def __init__(self):
        hero_data = get_hero_stat()
        self.name = hero_data[0]
        self.intelligence = hero_data[1]['intelligence']
        self.strength = hero_data[1]['strength']
        self.speed = hero_data[1]['speed']
        self.durability = hero_data[1]['durability']
        self.power = hero_data[1]['power']
        self.combat = hero_data[1]['combat']

    def arm_fight(self, other_hero):
        if isinstance(other_hero, Hero):
            if self.intelligence > other_hero.intelligence:
                print(f'{self.name} defeated {other_hero.name}. {self.name} won')
            elif self.intelligence < other_hero.intelligence:
                print(f'{self.name} amazed by {other_hero.name}. {self.name} lost')
            else:
                print('Draw:(')
        else:
            print(f'{other_hero} is not hero!')

    def brain_fight(self, other_hero):
        if isinstance(other_hero, Hero):
            if self.strength > other_hero.strength:
                print(f'{self.name} is smarter than {other_hero.name}. {self.name} won')
            elif self.strength < other_hero.strength:
                print(f'{self.name} isn\'t smarter than {other_hero.name}. {self.name} lost')
            else:
                print('Draw:(')
        else:
            print(f'{other_hero} is not hero!')


# if __name__ == '__main__':
def hero_game():
    arena = []
    while True:
        menu_text = \
            """
[1] Add hero to arena
[2] Show heroes on arena 
[3] Start brain fight between heroes
[4] Start PvP ARM wrestling
[5] Выход"""

        print(menu_text)
        user_choise = input('Select menu number: ')
        if user_choise == '1':
            arena.append(Hero())
        elif user_choise == '2':
            print('Hero on arena: ', end='')
            for hero in arena:
                print(f'{hero.name}, ', end='')
            input('Press any key: ')
        elif user_choise == '3':
            if len(arena) == 2:
                arena[0].brain_fight(arena[1])
            else:
                print('Brain fight is start!!!')
                dict_hero = {}
                for hero in arena:
                    dict_hero[hero.intelligence] = hero.name
                sorted_dict_hero = sorted(dict_hero, reverse=True)
                print(f'{dict_hero[sorted_dict_hero[1]]} is more clever than other')

        elif user_choise == '4':
            if len(arena) == 2:
                arena[0].arm_fight(arena[1])
            else:
                print('PvG fight is not supported')
        elif user_choise == '5':
            break
