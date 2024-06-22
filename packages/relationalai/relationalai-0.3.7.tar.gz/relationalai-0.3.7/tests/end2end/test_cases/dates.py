import datetime as dt

import pytest
import relationalai as rai
from relationalai import std

alias = std.alias

model = rai.Model(name=globals().get("name", "test_dates"), config=globals().get("config"))

# Check that 'date' works.
# DataFrame should have one row for each case.
with model.query() as select:
    with model.match(multiple=True) as matched:
        with model.case():
            date = std.dates.date(2024, 1, 1)
            std.dates.Date(date)
            matched.add(date, id=1)
        with model.case():
            ord = dt.date(2024, 1, 1).toordinal()
            date = std.dates.date.fromordinal(ord)
            std.dates.Date(date)
            matched.add(date, id=2)
        with model.case():
            _dt = dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc)
            date = std.dates.date.fromdatetime(_dt)
            std.dates.Date(date)
            matched.add(date, id=3)
        with model.case():
            _dt = std.dates.datetime(2024, 1, 1)
            date = std.dates.date.fromdatetime(_dt)
            std.dates.Date(date)
            matched.add(date, id=4)
    select(matched.id, alias(matched, "date"))

# Check that 'datetime' works.
# DataFrame should have one row for each scope in the union.
with model.query() as select:
    with model.match(multiple=True) as matched:
        with model.case():
            datetime = std.dates.datetime(2024, 1, 1, 6, 30, 0, 0, "UTC")
            std.dates.DateTime(datetime)
            matched.add(datetime, id=1)
        with model.case():
            ord = dt.date(2024, 1, 1).toordinal()
            datetime = std.dates.datetime.fromordinal(ord)
            std.dates.DateTime(datetime)
            matched.add(datetime, id=2)
        with model.case():
            _date = dt.date(2024, 1, 1)
            datetime = std.dates.datetime.fromdate(_date)
            std.dates.DateTime(datetime)
            matched.add(datetime, id=3)
        with model.case():
            _date = std.dates.date(2024, 1, 1)
            datetime = std.dates.datetime.fromdate(_date)
            std.dates.DateTime(datetime)
            matched.add(datetime, id=4)
    select(matched.id, alias(matched, "datetime"))

# Check that 'date_add' and 'date_subtract' work.
# DataFrame should have one row for each case.
for func in [
    std.dates.date_add,
    std.dates.date_subtract
]:
    with model.query() as select:
        with model.match(multiple=True) as matched:
            with model.case():
                date = dt.date(2024, 1, 1)
                p = std.dates.days(1)
                matched.add(func(date, period=p), id=1)
            with model.case():
                date = dt.datetime(2024, 1, 1, 6, 30, 45, tzinfo=dt.timezone.utc)
                p = std.dates.weeks(1)
                matched.add(func(date, period=p), id=2)
            with model.case():
                date = std.dates.date(2024, 1, 1)
                p = std.dates.months(1)
                matched.add(func(date, period=p), id=3)
            with model.case():
                date = std.dates.datetime(2024, 1, 1, 6, 30, 45)
                p = std.dates.years(1)
                matched.add(func(date, period=p), id=4)
        select(matched.id, alias(matched, "date"))

# Check that date parts work.
for func in [
    std.dates.year,
    std.dates.month,
    std.dates.day,
    std.dates.week,
    std.dates.weekday,
    std.dates.isoweekday,
    std.dates.quarter,
    std.dates.dayofyear,
]:
    with model.query() as select:
        with model.match(multiple=True) as matched:
            with model.case():
                date = dt.date(2024, 1, 1)
                matched.add(func(date), id=1)
            with model.case():
                date = std.dates.date(2024, 1, 1)
                matched.add(func(date), id=2)
        select(matched.id, alias(matched, func.__name__))

    # Check that passing an invalid argument raises a TypeError.
    with pytest.raises(TypeError):
        with model.query():
            func("INVALID")

# Check that datetime parts work.
for func in [
    std.dates.year,
    std.dates.month,
    std.dates.day,
    std.dates.hour,
    std.dates.minute,
    std.dates.second,
    std.dates.week,
    std.dates.weekday,
    std.dates.isoweekday,
    std.dates.quarter,
    std.dates.dayofyear,
]:
    with model.query() as select:
        with model.match(multiple=True) as matched:
            with model.case():
                datetime = dt.datetime(2024, 1, 1, 6, 30, 45, tzinfo=dt.timezone.utc)
                matched.add(func(datetime), id=1)
            with model.case():
                datetime = std.dates.datetime(2024, 1, 1, 6, 30, 45)
                matched.add(func(datetime), id=2)
        select(matched.id, alias(matched, func.__name__))

    # Check that passing an invalid argument raises a TypeError.
    with pytest.raises(TypeError):
        with model.query():
            func("INVALID")

# Check that period constructors work
with model.query(dynamic=True) as select:
    time = std.dates.datetime(2024, 1, 1)
    with model.match(multiple=True, dynamic=True) as matched:
            for (ix, period) in enumerate([
                std.dates.microseconds,
                std.dates.milliseconds,
                std.dates.seconds,
                std.dates.minutes,
                std.dates.hours,
                std.dates.days,
                std.dates.weeks,
                std.dates.months,
                std.dates.years,
            ]):
                with model.case():
                    matched.add(std.dates.date_add(time, period(1)), id=ix)
    select(matched.id, matched)

# Check that the date_range function works.
for kwargs in [
    {"start": dt.date(2024, 1, 1), "end": dt.date(2024, 1, 7)},
    {"start": dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc), "end": dt.datetime(2024, 1, 2, tzinfo=dt.timezone.utc), "freq": "H"},
    {"start": dt.date(2024, 1, 1), "end": dt.date(2024, 1, 2), "freq": "H"},
    {"start": dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc), "periods": 12, "freq": "M"},
    {"end": dt.date(2024, 1, 7), "periods": 7, "freq": "D"},
]:
    with model.query() as select:
        dates = std.dates.date_range(**kwargs)
        select(dates)
