import datetime as dt


# Можно использовать аннотации типов
# для обозначения типов входных аргументов и выходных значений
# Это позволит не путаться в типах данных,
# принимаемых функциями или методами, когда код начнёт разрастаться.
# Плюс, тебе самому будет проще разобраться, что куда должно идти

class Record:

    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    # Docstring для метода
    def add_record(self, record):
        self.records.append(record)

    # Docstring для метода
    def get_today_stats(self):
        today_stats = 0
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # Можно использовать += для инкремента переменных
                today_stats = today_stats + Record.amount
        return today_stats

    # Docstring для метода
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                    # Сравнения можно писать в виде A >= B >= C
                    (today - record.date).days < 7 and
                    (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Нужно оформить комментарий к методу в виде Docstring
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            # Лишние скобки
            return ('Хватит есть!')


class CashCalculator(Calculator):
    # Названия переменных говорят сами за себя, комментарии
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    # Названия аргументов функции должны быть в нижнем регистре
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        # Используй один регистр для обозначения валюты
        # Переменные на русском языке лучше не вводить - пиши на английском
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Сравнение вместо деления
            cash_remained == 1.00
            currency_type = 'руб'
        # Ставь пробелы после длинных условных конструкций:будет удобнее читать
        if cash_remained > 0:
            # Округление лучше вынести в отдельную операцию
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        # Нет необходимости прописывать последнее условие, т.к.
        # Области "больше 0" и "Равно 0" ты уже обработал:
        # У тебя автоматически останется область "меньше 0"
        elif cash_remained < 0:
            # Используй f-строку
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        # Метод ничего не возвращает
        # В родительском классе он уже прописан,
        # так что в дочернем классе можно не переопределять
        super().get_week_stats()

# Можно прописать сценарии использования и прохождение различных ветвлений,
# чтобы показать, что всё работает
