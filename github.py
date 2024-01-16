import datetime
import os
import schedule
import time

# Замените эти значения на свои данные
github_token = "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"
repo_url_with_token = f"https://Nurbolottop:{github_token}@github.com/Nurbolottop/GitAutoPush.git"

def job():
    file_path = '/home/binniev/activy/script.py'

    # Добавление новой строки с текущей датой
    new_line = f"# New line for {datetime.datetime.now()}\n"
    with open(file_path, 'a') as file:
        file.write(new_line)

    # Изменить URL репозитория на версию с токеном (только первый раз)
    os.system(f'git -C /home/binniev/activy remote set-url origin {repo_url_with_token}')

    # Команды Git для добавления, коммита и пуша изменений
    os.system(f'git -C /home/binniev/activy add {file_path}')
    os.system(f'git -C /home/binniev/activy commit -m "Add new line for {datetime.datetime.now().date()}"')
    os.system('git -C /home/binniev/activy push')

# Запланировать выполнение функции job каждую минуту
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
