# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(text, markers):
    rows_list = text.split("\n")                    # Creates a list with all rows
    for row in rows_list:
        new_row = ''                                # Creates a new row without commented text
        for el in row:
            if el not in markers:                   # Appends an element to a new row if it's not a comment character
                new_row += el
            else:                                   # Breaks a loop and ends a row if the element is a comment character
                break
        new_row = new_row.rstrip()                  # Strips whitespaces at the end of a new row
        rows_list[rows_list.index(row)] = new_row   # A new row replaces an old one
    return '\n'.join(rows_list)                     # Concatenates a list back into a string