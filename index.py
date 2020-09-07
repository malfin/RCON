import factorio_rcon
from time import sleep
from colorama import Fore, Back, Style, init
init()

title = (Fore.YELLOW + 'RCON_CONNECT_v0.1.3')
mcpc_mcpe = (Fore.RED + '\nПредназначена для: MCPE и MCPC!')
author_vk = (Fore.LIGHTBLUE_EX + '\nVK: vk.com/alex_nicke')
print(title)
print(mcpc_mcpe)
print(author_vk)
print(Fore.RESET + '\nВведите IP или Домен')
ip = input()
print('\nВведите RCON_PORT')
port = input()
while True:
    if len(port) < 5:
        print(Fore.RED + '\nERROR', "Короткий порт!")
        print("\nПерезапустите программу!")
        print("\nНапишите порт правильно!")
        sleep(5)
        exit()
    if port:
        break
while True:
    if len(port) > 5:
        print(Fore.RED + '\nERROR', "Слишком длинный порт!")
        print("\nПерезапустите программу!")
        print("\nНапишите порт правильно!")
        sleep(5)
        exit()
    if port:
        break
print('\nВведите RCON_PASSWORD')
ron_password = input()
print(Fore.GREEN + '\n\nИдёт соеденение с', ip, ':', int(port))
client = factorio_rcon.RCONClient(ip, int(port), ron_password)
print(Fore.RED + '\nВводите команды без /')
for i in range(99999):
    print(Fore.RESET + '\nВведите команду:')
    command = input()
    response = client.send_command(command)
    if command == '//wand':
        print('\nКомманда вводится в игре!')
    elif command == 'info':
        print('\nКоманда вводится в игре!')
    elif command == 'tell':
        print('\nИспользуйте: tell ник_игрока сообщение')
    elif command == ('/' + command):
        print(Fore.RED + '\nВведите без / !')
    else:
        console = str(response).replace('§a', '').replace('§f', '').replace('§6', '').replace('§c', '').replace('/',
                                                                                                                '').replace(
            '§5', '').replace('§d', '').replace('§r', '').replace('§4', '').replace('§7', '').replace('§b', '').replace(
            '§e', '')
        if console == 'None':
            print(Fore.YELLOW + '\n[RCON]', 'Команда отправлена!')
        elif command == 'stop':
            print(Fore.GREEN + 'Вы успешно выключили сервер!')
            print(Fore.RED + '\nЗакройте программу!')
            sleep(0.10)
            exit()
        elif command == 'reload':
            print(Fore.LIGHTRED_EX + 'Вы перезагружаете сервер!')
            print(Fore.RED + 'Закройте программу и введите всё заново!')
            sleep(0.10)
            exit()
        else:
            print(Fore.YELLOW + '\n[RCON]', console)
exit()
