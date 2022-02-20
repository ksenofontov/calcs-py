from datetime import datetime


class Record:
    def __init__(self, amount, comment, date=datetime.now()):
        self.amount = amount
        self.comment = comment
        self.date = date if isinstance(date, datetime) else datetime.strptime(date, '%d.%m.%Y')


class Calculator:
    def __init__(self, limit=0):
        self.records = []
        self.today = datetime.now()
        self.limit = limit

    def add_record(self, record):
        """Добавляет запись в список."""
        self.records.append(record)

    def get_today_stats(self):
        """Возвращает количество потраченных за сегодняшний день единиц"""
        count = 0
        for record in self.records:
            if record.date.day == self.today.day:
                count += record.amount
        return count

    def get_week_stats(self):
        """Возвращает количество потраченных за неделю единиц"""
        count = 0
        for record in self.records:
            if self.today.day * 7 - 7 < record.date.day * 7 <= self.today.day * 7:
                count += record.amount
        return count


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        """Возвращает ответ об оставшихся калориях в зависимости от лимита"""
        spent = self.get_today_stats()
        if spent < self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - spent} кКал"
        elif spent >= self.limit:
            return "Хватит есть!"


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        self.CUR = {'usd': 1/75, 'eur': 1/90, 'rub': 1}

    def get_today_cash_remained(self, currency):
        """Возвращает ответ об оставшихся средствах в зависимости от лимита"""
        spent = self.get_today_stats()
        if spent < self.limit:
            return f"На сегодня осталось {(self.limit - spent)*self.CUR[currency]} {currency}"
        elif spent == self.limit:
            return "Денег нет, держись"
        elif spent > self.limit:
            return f"Денег нет, держись: твой долг - {(spent - self.limit)*self.CUR[currency]} {currency}"


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
