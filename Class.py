from datetime import datetime
class Demonstration:
    def __init__(self, tr_list):
        self.tr_list = tr_list

    def looking_for_last_five_executed(self):
        last_five = []
        for i in self.tr_list:
            if i['state'] == 'EXECUTED':
                last_five.append(i)
        print(f'Это последние 5 -- {last_five[-5:]}')
        self.last_five = last_five

    def collect_and_present_data(self, format ="%d.%m.%Y"):
        for i in (self.last_five[-5:]):
            date_str = i['date']
            date_format = datetime.fromisoformat(date_str)
            #date_lst = date_str[0:10].split('-')
            #date_format = date(int(date_lst[0]), int(date_lst[1]), int(date_lst[2]))
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
            print(f'{date_format.strftime(format)} {description}\n{fromm_lst[0]} {fromm_format} -> {to_lst[0]} {to_format}\n{amount} {currency}\n')



