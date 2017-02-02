#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import re


def get_rows(filename):
    f = open(filename, 'r')
    contents = f.readlines()
    rows = []
    for row in contents:
        row = row.strip()
        if row:
            rows.append(row)
    return rows


def get_habits(rows):
    habits = {}
    rows = [a.split('|') for a in rows if re.match('habit\|', a)]
    for row in rows:
        # calculate goal
        goal = row[3].split('/')
        goal = float(goal[0]) / float(goal[1])
        # calculate streak
        streak = False
        if row[4] == 'streak':
            streak = True
        habits[row[1]] = {'name': row[2], 'goal': goal, 'streak': streak}
    return habits


def get_habit_days(habits={}, rows=[]):
    '''Return dict with list of days per habit'''
    habit_days = habits
    for habit in habits:
        habit_days[habit]['days'] = []
    rows = [a.split(' ') for a in rows if re.match('\d{4}\-\d{2}\-\d{2}\s', a)]
    for row in rows:
        d = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        habits = row[1:]
        for habit in habits:
            if habit in habit_days.keys():
                habit_days[habit]['days'].append(d)
    return habit_days


def date_to_spark(date, days_on):
    if date in days_on:
        return '▆'
    else:
        return '▁'


def get_streak(days, last_day):
    # no streak yet
    if len(days) <= 1:
        return ', fresh habit'
    if not last_day in days:
        return ', time to start a streak'
    # sort days and calc delta to next day
    days = sorted(days, reverse=True)
    deltas = [(days[a] - days[a+1]).days for a in range(0, len(days) - 1)]
    if deltas[0] != 1:
        return ', 1 day streak'
    breaks = []
    for i in range(2, len(deltas)):
        if i in deltas:
            breaks.append(deltas.index(i))
    return ', current streak %s days' % (min(breaks) + 1)


def report_habit(habit={}, num_days=7):
    today = datetime.datetime.today()
    today = datetime.datetime(today.year, today.month, today.day)
    if max(habit['days']) == today:
        last_day = today
    else:
        last_day = today - datetime.timedelta(days=1)
    if habit.get('streak') is True:
        streak = get_streak(habit.get('days'), last_day)
    else:
        streak = ''
    first_day = min(habit.get('days'))
    if (last_day - first_day).days < num_days:
        num_days = (last_day - first_day).days + 1
    report_days = [last_day - datetime.timedelta(days=i) for i in range(0, num_days)]
    count_days = len([a for a in report_days if a in habit['days']])
    pct = '{0:.0f}%'.format(float(count_days) / float(num_days) * 100)
    goal = habit.get('goal')
    goal = '{0:.0f}%'.format(goal * 100)
    report_days.sort()
    spark = [date_to_spark(date=a, days_on=habit.get('days')) for a in report_days]
    report = '{name}: {count} out of {num} days, {pct} vs goal {goal}{streak}\n{indent}{spark}'
    print report.format(name=habit.get('name'),
                        count=count_days,
                        num=num_days,
                        pct=pct,
                        goal=goal,
                        streak=streak,
                        indent=''.join([' ' for a in range(0, len(habit.get('name'))+2)]),
                        spark=' '.join(spark))


def report(habit_days={}, num_days=10):
    print 'Habit Report %s\n-----------------------' % datetime.datetime.today().strftime('%Y-%m-%d')
    for habit in habit_days:
        report_habit(habit=habit_days[habit], num_days=num_days)
    pass


def main(args):
    rows = get_rows(filename=args.file)
    habits = get_habits(rows=rows)
    habit_days = get_habit_days(habits=habits, rows=rows)
    report(habit_days=habit_days, num_days=int(args.days))
    # report = get_new_report(habits=habits,
    #                         day_habits=day_habits)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--file', '-f',
                   default='habits.txt')
    p.add_argument('--days', '-d', default=10)
    args = p.parse_args()
    main(args=args)
