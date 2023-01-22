class Shkaf:
    """Это класс шкафа"""
    def __init__(self, name):
        self.name = name
        self.status = 'close'

    def __str__(self):
        s_str = f'статус шкафчика: {self.status} '
        return s_str

# открыть / закрыть шкаф
    def action(self, st):
        self.status = st
