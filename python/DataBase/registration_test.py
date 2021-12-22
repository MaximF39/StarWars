from time import sleep
# from .Player.Player import Player


def test_con_main():
    a = {
        'name': 'max2',
        'passwd': '123'
    }

    def wait(cnt: int):
        if cnt < 10:
            sleep(3)
        else:
            sleep(10 ** 3)  # отключить соединение от айпи на час
            del b
        pass

    count_attempts = 0
    # b = Player(a['name'])
    b.reg(a['passwd'])
    if not b.reg_bool:
        print('del name')
        del b
    else:
        while True:
            if b.entry(a['passwd']):
                print('регистрация прошла успешно')
                b.delete()
                break
            else:
                print("don't reg")
                count_attempts += 1
                if count_attempts > 5:
                    wait(count_attempts)
    # print(b)
