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

    def collect_and_place_data(self):
        for i in (self.last_five[-5:]):
            date = i['date']
            description = i['description']
            if 'from' in i:
                fromm = i['from']
            else:
                fromm = 'Нет данных'
            if 'to' in i:
                to = i['to']
            else:
                to = 'Нет данных'
            print(f'{date} {description}\n{fromm} -> {to}\n*********************')


    #def __repr__(self):
    #    return f'{self.date} {self.description}\n{self.fromm} -> {self.to}'
