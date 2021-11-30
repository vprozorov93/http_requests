from hero_game import hero_game
from loader_to_ya_disk import start_loader
from stackoverflow_request import get_questions_with_py_tags

if __name__ == '__main__':

    menu_text = """
          [1] Start superhero game
          [2] Start Ya file loader
          [3] Start something
          [5] Exit
          """
    while True:
        print(menu_text)
        user_choise = input('Choose menu number: ')

        if user_choise == '1':
            hero_game()
        elif user_choise == '2':
            start_loader()
        elif user_choise == '3':
            get_questions_with_py_tags()
        elif user_choise == '4':
            break

