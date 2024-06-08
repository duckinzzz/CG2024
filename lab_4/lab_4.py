import argparse
import csv
import xlsxwriter


def csv_to_xlsx_converter(input_file, output_file, delimiter):
    with open(input_file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=delimiter)
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()
        for row_idx, row in enumerate(csv_reader):
            for col_idx, data in enumerate(row):
                worksheet.write(row_idx, col_idx, data)
        workbook.close()


parser = argparse.ArgumentParser(description='CSV to XLSX Converter')
parser.add_argument('input_file', type=str, help='Input CSV file')
parser.add_argument('output_file', type=str, help='Output XLSX file')
parser.add_argument('-d', '--delimiter', type=str, default=';', help='CSV delimiter (";" by default)')
args = parser.parse_args()
csv_to_xlsx_converter(args.input_file, args.output_file, args.delimiter)
