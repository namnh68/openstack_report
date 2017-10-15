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


def write_xls(file_name, data, data_xfs):
    book = xlsxwriter.Workbook(file_name)
    format_col = book.add_format({'align': 'center'})
    sheet = book.add_worksheet('OpenStack_hypervisor')
    sheet.set_column('A:A', 20, cell_format=format_col)
    sheet.set_column('B:M', 15, cell_format=format_col)
    sheet.set_default_row(20, format_col)
    sheet = prepare_header(sheet, book)
    row = 6
    for name_com, params in data.items():
        sheet.write(row, 0, name_com)
        sheet.write(row, 1, params.get('memory_mb_used'))
        sheet.write(row, 2, params.get('memory_mb'))
        sheet.write_formula(row, 3, '=B{0}/C{0}'.format(row+1))
        sheet.write(row, 4, params.get('real_memory_used'))
        sheet.write(row, 5, params.get('real_memory_mb'))
        sheet.write_formula(row, 6, '=E{0}/F{0}'.format(row+1))
        sheet.write(row, 7, params.get('vcpus_used'))
        sheet.write(row, 8, params.get('vcpus'))
        sheet.write_formula(row, 9, '=H{0}/I{0}'.format(row+1))
        sheet.write(row, 10, params.get('real_cpu_used'))
        sheet.write(row, 11, params.get('real_cpu'))
        sheet.write_formula(row, 12, '=K{0}/L{0}'.format(row+1))
        row += 1
    book.close()


data = {
    'compute3': {'memory_mb_used': '10', 'memory_mb': '20', 'vcpus_used': '50',
                 'vcpus': '100', 'real_memory_used': '5', 'real_memory_mb':
                     '7', 'real_cpu_used': '30', 'real_cpu': '60'},
    'compute1': {'memory_mb_used': '1', 'memory_mb': '2', 'vcpus_used': '5',
                 'vcpus': '10', 'real_memory_used': '0.5', 'real_memory_mb':
                     '0.75', 'real_cpu_used': '3', 'real_cpu': '6'},
    'compute2': {'memory_mb_used': '10', 'memory_mb': '20', 'vcpus_used': '50',
                 'vcpus': '100', 'real_memory_used': '5', 'real_memory_mb':
                     '7', 'real_cpu_used': '30', 'real_cpu': '60'},

}

filename = '/Users/NamHoai/MyGit/openstack_report/test.xlsx'
write_xls(filename, data=data, data_xfs='b')
