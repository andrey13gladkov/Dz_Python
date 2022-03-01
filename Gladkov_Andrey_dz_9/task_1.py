# Задание № 1


import time


class TrafficLight:
    __color = [('Красный', 5), ('Желтый', 2), ('Зеленый', 5)]

    def running(self):
        print('Светофор рабоатет:')
        for color, sec in self.__color:
            print(f'{color} cвет! Осталось:\n{sec} сек')
            time.sleep(1)
            timer = sec - 1
            while timer > 0:
                print(f'{timer} сек')
                time.sleep(1)
                timer -= 1




if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
