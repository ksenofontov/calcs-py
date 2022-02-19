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

  def add_record(self, record):
    self.records.append(record)

  def get_today_stats(self):
    count = 0
    for record in self.records:
      if record.date.day == self.today.day:
        count += record.amount
    print(count)

  def get_week_stats(self):
    count = 0
    for record in self.records:
      if self.record.date

class CaloriesCalculator(Calculator):
  def get_calories_remained(self):



class CashCalculator(Calculator):
  def get_today_cash_remained(currency):



calc = Calculator()
calc.add_record(Record(100, 'comm1', datetime.now()))
calc.add_record(Record(200, 'comm2', datetime.now()))
calc.get_today_stats()
