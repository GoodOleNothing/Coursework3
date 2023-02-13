class Demonstration:
    def __init__(self, tr_list):
        self.tr_list = tr_list

    def looking_for_last_five_executed(self):
        last_five = []
        for i in self.tr_list:
            if 'state' in i.keys():
              if i['state'] == 'EXECUTED':
                  #print(i["description"])
                  last_five.append(i)
        print(f'это последние 5 {len(last_five)}')



