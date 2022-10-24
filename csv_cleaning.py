import csv
import xlrd
import re
import pandas as pd


def convert_to_csv(filename):
    print("file name in convert to csv")
    print('{}.xlsm'.format(filename))
    workbook = xlrd.open_workbook('{}.xlsm'.format(filename))
    # workbook = pd.read_excel('{}.xlsm'.format(filename), engine='openpyxl')
    for sheet in workbook.sheets():
        with open('{}.csv'.format(filename), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sheet.row_values(row) for row in range(sheet.nrows))


def is_bad_company(name):
    with open("reference_files\\bad_companies.csv") as list:
        csv_reader = csv.reader(list, delimiter=',')
        for row in csv_reader:
            if len(row) == 0:
                continue
            if row[0].lower() in name.lower():
                return True
    return False


def is_business(name):
    to_match = re.findall(r"[\w']+", name)
    to_match = [x.lower() for x in to_match]
    with open("reference_files\\corp_terms_list.csv") as list:
        csv_reader = csv.reader(list, delimiter=',')
        for row in csv_reader:
            if len(row) == 0:
                continue
            if row[0] in to_match:
                return True
    return False


def clean_csv(filename, cleanedFilename, format):
    key_nature1_formula = '=IF(ISNUMBER(SEARCH("Balboa Capital",G2)),"Balboa Capital Lawsuit Against Your Company",IF(ISNUMBER(SEARCH("Creditors Adjustment",G2)),"Creditors Adjustment Bureau Lawsuit Against Your Company",IF(ISNUMBER(SEARCH("contract",I2)),"Contract Dispute Against Your Company",IF(ISNUMBER(SEARCH("labor",I2)),"Labor Dispute Filed Against Your Company",IF(ISNUMBER(SEARCH("employment",I2)),"Labor Dispute Filed Against Your Company",IF(ISNUMBER(SEARCH("banking",I2)),"Banking, Finance & Collections Lawsuit Filed Against Your Company",IF(ISNUMBER(SEARCH("landlord",I2)),"Tenant Dispute Filed Against Your Company",IF(ISNUMBER(SEARCH("unfair",I2)),"Unfair Competition Lawsuit Filed Against Your Company",IF(ISNUMBER(SEARCH("intellectual",I2)),"IP Lawsuit Filed Against Your Company",IF(ISNUMBER(SEARCH("FRAUD",I2)),"Lawsuit Claiming Fraud Filed Against Your Company",I2))))))))))'
    match = re.search(r'[0-9]+', key_nature1_formula)
    if not format is "csv":
        convert_to_csv(filename)
    rows = []
    with open("{}.csv".format(filename), newline='') as to_clean:
        csv_reader = csv.reader(to_clean, delimiter=',')
        line_count = 0
        Flag = False
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                del row[1]
                del row[-1:-4:-1]
                row.append("Key Nature1")
                rows.append(row)
                line_count += 1
            elif is_business(row[0]) and not is_bad_company(row[0]):
                del row[1]
                del row[-1:-4:-1]
                key_nature1 = key_nature1_formula.replace(match.group(0), str(line_count))
                row.append(key_nature1)
                row[0] = row[0].title()
                rows.append(row)
                line_count += 1

    with open('{}.csv'.format(cleanedFilename), 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":
    clean_csv("westlaw_24092020", "cleanFile", 'xlsm'),