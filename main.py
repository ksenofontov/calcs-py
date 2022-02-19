from datetime import datetime


class Record:
  def __init__(self, amount, comment, date):
    record = {
      "amount": amount,
      "comment": comment,
      "date": datetime.strptime(date, '%b %d %Y %I:%M%p')
    }


class Calculator:
  self.records = []
  def __init__(self, limit):
    self.limit = limit

  def add_record(record):
    if not type(record) is Record:
      raise TypeError('Wrong record format')
    self.records.append(record)

  def get_today_stats():


