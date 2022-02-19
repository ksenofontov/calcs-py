from datetime import datetime

def make_date(date):
  if type(date) == str:
    return datetime.strptime(date, '%d.%m.%y')
  elif type(date) == datetime:
    return date

class Record:
  def __init__(self, amount, comment, date):
      self.amount = amount
      self.comment = comment
      self.date = make_date(date)


class Calculator:
  def __init__(self, limit=0):
    self.records = []
    self.today = datetime.now()
    self.limit = limit
    USD_RATE = 75
    EUR_RATE = 90


  def add_record(self, record):
    self.records.append(record)

  def get_today_stats(self):
    count = 0
    for record in self.records:
      if record.date.day == self.today.day:
        count += record.amount
    return count

  def get_week_stats(self):
    count = 0
    for record in self.records:
      if self.today.week - 7 < record.date.week <= self.today.week:
          count += record.amount
    return count

class CaloriesCalculator(Calculator):
  def get_calories_remained(self):
    spent = self.get_today_stats()
    if spent < self.limit:
      return "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более " + (self.limit - spent) + " кКал"
    elif spent >= self.limit:
      return "Хватит есть!"


class CashCalculator(Calculator):

  def get_today_cash_remained(self,currency):
    spent = self.get_today_stats()
    if spent < self.limit:
      return ("На сегодня осталось" + (self.limit - spent) + currency)
    elif spent == self.limit:
      return "Денег нет, держись"
    elif spent > self.limit:
      return "Денег нет, держись: твой долг -" (spent - self.limit) + currency





calc = Calculator()
calc.add_record(Record(100, 'comm1', datetime.now()))
calc.add_record(Record(200, 'comm2', datetime.now()))
calc.get_today_stats()
