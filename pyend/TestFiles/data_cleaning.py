import pandas as pd
from ast import literal_eval

with open("pyend/data.csv") as file:
    file_content = file.readlines()  # getting the lines from the csv file

header = file_content[0:1][0].split("#")  # data headers
header = [
    element.strip() for element in header
]  # deleting whitespaces from each string


data_row = file_content[1:]

for i, row in enumerate(data_row):
    row_content = row.split("#")

    genre = []

    genre_str = row_content[5].strip()

    # avoiding empty strings error in literal_eval()
    if genre_str:
        genre = literal_eval(genre_str)

    # Object represeting a record
    new_row = {
        header[0]: int(row_content[0]),
        header[1]: row_content[1],
        header[2]: row_content[2],
        header[3]: "{:,}".format(int(row_content[3])),
        header[4]: row_content[4],
        header[5]: genre,
    }

    # Replacing the record with an actual clean record
    data_row[i] = new_row


data_frame = pd.DataFrame(data_row)

data_frame.to_csv("pyend/cleaned_data.csv", index=False)
