from datetime import datetime


def looking_for_last_five_executed(operations):
    """Собираем последние 5 операций"""
    last_five = []

    for i in operations:
        if i['state'] == 'EXECUTED':
            last_five.append(i)
    #print(f'Это последние 5 -- {last_five[-5:]}')
    return last_five


def collect_and_present_data(g, formate_time="%d.%m.%Y"):
    """Берём последние 5 операций и организуем вывод,
    приводим дату к нужному формату,
    выражаем остальное в нужном формате"""
    for i in (g[-5:]):
        date_str = i['date']
        date_format = datetime.fromisoformat(date_str)
        description = i['description']
        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']
        if 'from' in i:
            fromm = i['from']
            fromm_lst = fromm.split(' ')
            fromm_format = fromm_lst[1][0:4] + " " + fromm_lst[1][4:6] + "** ****" + " " + fromm_lst[1][-4:]
        else:
            fromm_lst = ['Нет']
            fromm_format = 'данных'
        if 'to' in i:
            to = i['to']
            to_lst = to.split(' ')
            to_format = '**' + to_lst[1][-4:]
        else:
            to_lst = ['Нет']
            to_format = 'данных'
        print(f'{date_format.strftime(formate_time)} {description}\n{fromm_lst[0]} {fromm_format} -> '
              f'{to_lst[0]} {to_format}\n{amount} {currency}\n')



