# habits-dot-py

Text file habit tracking and command line reporting

## Examples

    $ ./habits.py -d 10
    Habit Report 2017-02-02
    -----------------------
    Meditate: 9 out of 10 days, 90% vs goal 80%, current streak 6 days
              ▆ ▆ ▆ ▁ ▆ ▆ ▆ ▆ ▆ ▆
    Exercise: 6 out of 10 days, 60% vs goal 60%
              ▁ ▆ ▁ ▆ ▆ ▁ ▆ ▁ ▆ ▆
    $ ./habits.py -d 30
    Habit Report 2017-02-02
    -----------------------
    Meditate: 23 out of 29 days, 79% vs goal 80%, current streak 6 days
              ▆ ▁ ▆ ▆ ▆ ▆ ▆ ▁ ▁ ▁ ▁ ▆ ▆ ▆ ▆ ▆ ▆ ▆ ▆ ▆ ▆ ▆ ▁ ▆ ▆ ▆ ▆ ▆ ▆
    Exercise: 15 out of 25 days, 60% vs goal 60%
              ▆ ▆ ▁ ▆ ▁ ▆ ▁ ▆ ▁ ▆ ▆ ▁ ▁ ▆ ▆ ▁ ▆ ▁ ▆ ▆ ▁ ▆ ▁ ▆ ▆

## Features

- Set goals for each habit
- On/off streak reporting per habit
- Count today if recorded, else count through yesterday
- Report vs goal for any number of days
- Sparklines-style view of history
- Skip days or enter "none"

## Installation and usage

- Clone repository
- Start your own `habits.txt` file
- Set up and track your habits in `habits.txt`
- Report on your habits using `habits.py`

**Usage**

    usage: habits.py [-h] [--file FILE] [--days DAYS]
    
    optional arguments:
      -h, --help            show this help message and exit
      --file FILE, -f FILE
      --days DAYS, -d DAYS

**Format for `habits.txt`**

Blank lines for readability are ok.

Habit lines: Set up each habit with a line like this.

    habit|code|Name|num1/num2|[streak/nostreak]

- The line is pipe delimited
- Start with the _keyword_ "habit"
- Short _code_ you want to use for tracking
- _Name_ for use in reporting
- _Goal_ as a two numbers separated by slash, e.g. 4/5 for "four days out of five"
- _Streak reporting_ use "streak" to report streaks and "nostreak" to skip them

Daily record lines: Each day you do one of your habits record it like this.

    YYYY-MM-DD code [code ...]

You can record each habit on its own line, or you can add multiple habits per line. If you miss all your habits on a day you can skip the record, or write the date and use the code "none".

## Optional

Keep your `habits.txt` file somewhere convenient. I keep mine in `~/Dropbox/Lists/habits_dot_txt.txt`. From there I can edit it wtih nvAlt locally on my Mac, and with 1Writer or other apps on the iPhone or iPad.

Edit `habits.py` to set the default location of your `habits.txt` file. Set that here:

        p.add_argument('--file', '-f',
                       default='/Users/dan/Dropbox/Lists/habits_dot_text.txt')

If you use a `~/bin` directory, a link to `habits.py` to make it more like a built-in command.

    cd && ln -s /path/to/habits.py ~/bin/habits