from datetime import datetime
def looking_for_executed(operations):
    """Собираем последние 5 операций"""

    #operations = sorted(operations, key=lambda x: x["date"], reverse=True)
    executed = []
    for i in operations:
        if i['state'] == 'EXECUTED':
            executed.append(i)
    executed.sort(key=lambda x: x['date'], reverse=True)
    return executed[:5]


def collect_and_present_data(executed, formate_time="%d.%m.%Y"):
    """Берём последние 5 операций и организуем вывод,
    приводим дату к нужному формату,
    выражаем остальное в нужном формате"""
    for i in executed:
        date_str = i['date']
        date_format = datetime.fromisoformat(date_str)
        description = i['description']
        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']
        if 'from' in i:
            fromm = i['from']
            fromm_lst = fromm.split(' ')
            if len(fromm_lst) < 3:
                fromm_format = fromm_lst[1][0:4] + " " + fromm_lst[1][4:6] + "** ****" + " " + fromm_lst[1][-4:]
            elif len(fromm_lst) == 3:
                fromm_format = fromm_lst[1] + " " + fromm_lst[2][0:4] + " " + fromm_lst[2][4:6] + "** ****" + " " + fromm_lst[2][-4:]
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



