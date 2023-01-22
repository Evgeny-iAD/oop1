import human as h

class Person(h.Human):
    """Это класс персоны"""
    # Способ создания объекта (конструктор)
    def __init__(self, full_name, pol, data_b):
        super().__init__(pol, data_b)
        self.full_name = full_name
        self.pred = ''
        self.list_chil = []

    def __str__(self):
        s_str = f'{self.full_name} {h.Human(self.pol, self.data_b)}'
        return s_str

    def add_chil(self, per):
        if per.pol == 'м':
            per.pred = f'сын {self.full_name}'
            self.list_chil.append(per)
        else:
            per.pred = f'дочь {self.full_name}'
            self.list_chil.append(per)

    def get_list_chil(self):
        return self.list_chil

    # def format_text(f):
    #     buf = '\033'+'[33m'+'{}'+'\033[0m'
    #     return buf.format(f)