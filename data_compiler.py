
# remove the following comment line after implementing
# it is just there to temporarily suppress a warning in the unimplemented function


def compile_data(stopping_voltages, photocurrents):

    # We have two data arrays. The photocurrents are the independent (y) values. The stopping voltages
    # are the dependent (x) values.

    # These need to be compiled into a single dictionary whose keys are the x values and whose values are
    # tuples containing the sum of y values, the sum of the squares of the y values, and their count.

    # NOT YET IMPLEMENTED.
    # Follow the above comments to turn the two arrays above into a single dictionary. with the keys and values
    # as described.
    x_and_y_dict = dict()

    sum_of_y = 0

    sum_of_squares_of_y = 0

    count = 0

    for y in photocurrents:
        sum_of_y += y
        sum_of_squares_of_y += y*y
        count += 1

    for each in stopping_voltages:
        x_and_y_dict[each] = sum_of_y, sum_of_squares_of_y, count

    return x_and_y_dict
