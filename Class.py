class Demonstration:
    def __init__(self, tr_list):
        self.tr_list = tr_list

    def looking_for_last_five_executed(self):
        last_five = []
        for i in self.tr_list:
            if i['state'] == 'EXECUTED':
                last_five.append(i)
        print(f'Это последние 5 -- {last_five[-5:]}')



