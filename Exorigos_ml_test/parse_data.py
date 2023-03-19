import csv
from single_point import parse


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """
    final_x_matrix = list()
    final_y_vector = list()
    f = open(data_file_full_path)
 
    with f as fd:
        #read the data/test file
        reader = csv.reader(fd)
        for row in reader:
            try:
                #parse each row and save the result to final matrix/vector
                row = [x.strip(' ') for x in row]
                parsed_row = parse(row)
                final_x_matrix.append(parsed_row[0])
                final_y_vector.append(parsed_row[1])
            except ValueError as e:
                continue
            except IndexError as e:
                continue

    return final_x_matrix, final_y_vector

