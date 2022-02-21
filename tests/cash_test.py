from main import CashCalculator, Record


def test_today_cash():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
    assert cash_calculator.get_today_stats() == 5550
