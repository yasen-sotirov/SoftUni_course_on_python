# comments are here for guidance
# you can delete them before the demo

# 1. Positional Arguments
def repeat_txt(txt, times):
    return txt * times


# a function must be called with exactly as many arguments as it expects
print(repeat_txt('-', 10))

# not less (uncomment for error)
# print(repeat_txt('-'))

# or not more
# print(repeat_txt('-', 2, 'something else'))

# 2. Keyword Arguments
# argument names can be used to specify what value is passed
# still, it requires exactly two
print(repeat_txt(txt='-', times=20))
print(repeat_txt(times=20, txt='-'))

# 3 Default arguments


def format_paragraph(txt, title='No title', column_width=10):
    rows = [title.upper()]  # first row is the title

    start = 0
    while start < len(txt):
        next_row = txt[start: start + column_width]
        rows.append(next_row)
        start = start + column_width

    rows.append(' ')  # last row is empty

    return '\n'.join(rows)


print(format_paragraph('Python supports default arguments'))
print(format_paragraph(
    'You can specify only one of the default arguments', column_width=15))
print(format_paragraph('Or, you can specify both default arguments',
      title='Some title', column_width=8))

# *, means that all params must be added as keyword args


def format_paragraph_keyword_only(*, txt, title='No title', column_width=10):
    rows = [title.upper()]  # first row is the title

    start = 0
    while start < len(txt):
        next_row = txt[start: start + column_width]
        rows.append(next_row)
        start = start + column_width

    rows.append(' ')  # last row is empty

    return '\n'.join(rows)


print(format_paragraph_keyword_only(txt='This is valid'))
print(format_paragraph_keyword_only(txt='This is also valid', column_width=30))
# print(format_paragraph_keyword_only('This is not valid, keyword expected. This will cause an error'))
