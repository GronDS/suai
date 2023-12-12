from typing import TextIO

class Events():
    
    def __init__(self,filename: str, data: TextIO) -> None:
        self.__filename: str= filename
        self.__data: TextIO = data
        
    def parse_data(self, event_type):
        event_dict: dict= dict()
        
        for event in self.__data:
            event = event[:-1]
            date, time, status = event.split()
            if status == event_type:
                time = f'{date} {time[:5]}]'
                if time in event_dict.keys():
                    event_dict[time] += 1
                else:
                    event_dict.update({time : 1})
        
        parsed_file = open(f'{self.__filename}_parsed.txt', 'a+')
        for key, value in event_dict.items():
            parsed_file.write(f'{key} {value}\n')
        parsed_file.close()
                    
if __name__ == '__main__':
    filename = 'events'
    filepath = '/home/gron/python_work/suai/suai/module_2/practice_6/events.txt'
    with open(filepath, 'r') as events:
        event_lits = Events(filename, events)
        event_lits.parse_data('NOK')