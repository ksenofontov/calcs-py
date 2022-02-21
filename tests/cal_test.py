from main import CaloriesCalculator, Record


def test_today_cal():
    cal_calculator = CaloriesCalculator(1000)
    cal_calculator.add_record(Record(amount=145, comment='кофе'))
    cal_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cal_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
    assert cal_calculator.get_today_stats() == 555
