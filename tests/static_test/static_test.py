import threading
import time


class ListClass:
    _static_list = [1, 2, 3, 4, 5]


class Tester1:

    def print(self):
        print(f'testr 1 {ListClass._static_list}')


class Tester2:

    def print(self):
        print(f'testr 2 {ListClass._static_list}')


class Tester3:

    def print(self):
        print(f'testr 3 {ListClass._static_list}')


if __name__ == '__main__':
    test1 = Tester1()
    test2 = Tester2()
    test3 = Tester3()


    i = 0
    for _ in range(5):
        ListClass._static_list.append(i)

        test1.print()
        test2.print()
        test3.print()

        time.sleep(2)
        i += 1
