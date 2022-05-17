import csv


class CSVSaver():
    """A class that stores the data into a csv file"""
    def __init__(self, data, filename, columns):
        self.data = data
        self.filename = filename
        self.columns = columns


    def convert(self):
        """Stores the data into a csv file"""
        try:
            with open(self.filename, 'w') as self.filename:
                writer = csv.DictWriter(self.filename, fieldnames=self.columns)
                writer.writeheader()
                for data_row in self.data:
                    writer.writerow(data_row)
        except IOError:
            print("I/O error")