team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s." % team1_num)
print('Итого сегодня в командах участников: %s и %s.' % (team1_num, team2_num))
score_2 = 42
team2_time = 18015.2
team1_time = 17056.5
print('Команда Волшебники данных решила задач: {}.'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задачи.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print(f'Результат битвы: {result}.')
task_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / task_total, 3)
print(f'Сегодна было решено - {task_total}, среднее время решения - {time_avg} с.')
