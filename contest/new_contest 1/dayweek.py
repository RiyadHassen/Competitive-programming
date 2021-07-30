class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        name_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday",]
        d = date(year,month,day)
        week_day = d.weekday()
        return name_week[week_day]
        