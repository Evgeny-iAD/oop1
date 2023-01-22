import shkaf as sh

class Human:
    """Это класс человека"""
    def __init__(self, pol, data_b):
        self.pol = pol
        self.data_b = data_b

    def __str__(self):
        s_str = f'(пол: {self.pol}, родился в {self.data_b} г.)'
        return s_str

# выбор действия со шкафчиком
    def action(self, name, st):
        varible = ['on', 'close']
        shk = sh.Shkaf(name)
        if st in varible:
            shk.action(st)
            return shk.status
        return 'нет такого действия'

