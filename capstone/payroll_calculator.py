class PayrollCalculator:
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def calculate_pay(self, hours):
        regular_hours = min(hours, 40)
        overtime_hours = max(0, hours - 40)
        return (regular_hours * self.hourly_rate) + (overtime_hours * self.hourly_rate * 1.5)
