class Phone:
    """
       Класс Phone
       атрибуты 'brand', 'model', 'issue_year'
       методы:
            - инициализатор
            - receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
            - get_info, который будет возвращать кортеж (brand, model, issue_year)
            - метод __str__, который выводит на экран информацию об устройстве:
                Бренд: {}
                Модель: {}
                Год выпуска: {}

    """
    brand: str
    model: str
    issue_year: str

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f'Звонит {name}')

    def get_info(self):
        print(tuple(vars(self)))

    def __str__(self):
        for key in vars(self):
            if key == 'brand':
                print(f'Бренд:', {vars(self)[key]})
            elif key == 'model':
                print(f'Модель:', {vars(self)[key]})
            else:
                print(f'Год выпуска:', {vars(self)[key]})


phone = Phone("nokia", "3310", 2001)

# phone.get_info()
phone.__str__()
