# -*- coding: utf-8 -*-

import xlsxwriter


def prepare_header(sheet, workbook):
    headers1 = ['Host', 'Ram', 'CPU']
    headers2 = ['Theory', 'Real']*2
    headers3 = ['Used', 'Total', 'Ratio']*4
    header_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'yellow'})
    sheet.merge_range('A4:A6', data=headers1[0], cell_format=header_format)
    sheet.merge_range('B4:G4', data=headers1[1], cell_format=header_format)
    sheet.merge_range('H4:M4', data=headers1[2], cell_format=header_format)
    col2 = 0
    for header2 in headers2:
        row2 = 4
        sheet.merge_range(row2, col2+1, row2, col2+3, header2,
                          cell_format=header_format)
        col2 = col2 + 3
    row3 = 5
    for col3, header3 in enumerate(headers3):
        col3 += 1
        sheet.write(row3, col3, header3, header_format)
    return sheet


def write_xls(file_name, sheet_name, data, data_xfs):
    book = xlsxwriter.Workbook(file_name)
    sheet = book.add_worksheet(sheet_name)
    sheet = prepare_header(sheet, book)
    book.close()

filename = '/Users/NamHoai/MyGit/openstack_report/test.xlsx'
write_xls(filename, sheet_name='Test', data='a', data_xfs='b')
