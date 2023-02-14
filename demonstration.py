from datetime import datetime


def looking_for_last_five_executed(operations):
    """Собираем последние 5 операций"""
    last_five = []
    for i in operations:
        if i['state'] == 'EXECUTED':
            last_five.append(i)

    dated_list = []
    for i in last_five:
        rrr = datetime.fromisoformat(i['date']).strftime("%d.%m.%Y")
        i['date'] = rrr

    srtd = lambda x: (sorted(i['date'] for i in last_five))
        #dated = lambda x: (sorted)
        #dated_list.append(dated(i))
    #    dated = datetime.fromisoformat(str(i['date']))
    #    dated_list.append(dated.strftime("%d.%m.%Y"))
    print(last_five)
    print(srtd(last_five))
    srtd_last_five = srtd(last_five)

    #srt_by_time= lambda x: (sorted(dated_list))
    #print(last_five)
    #print(srt_by_time(dated_list))
    return srtd_last_five


def collect_and_present_data(last_five, formate_time="%d.%m.%Y"):
    """Берём последние 5 операций и организуем вывод,
    приводим дату к нужному формату,
    выражаем остальное в нужном формате"""
    for i in (last_five[-5:]):
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



