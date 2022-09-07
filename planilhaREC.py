from openpyxl import load_workbook
from funcs import organizador
from datetime import datetime

planilha = load_workbook('exped_rec.xlsx')
plan = planilha.active

r = ['/OP1', 'CI:10', 'TODAS-AS-FLORES', 'VTR:M015', 'M40-oooooo/aaaaaaaaaa-123456/HL1-123456/HL2', 'HMI1200-654321/HL3-654321/HL4-dasdsad/kdskadk']
x = organizador(r)

plan['D5'] = datetime.now().strftime('%H:%M:%S')

for v in range(len(x[0])):

    plan[f'C1{v}'] = f'{x[0][v]}'
    plan[f'E1{v}'] = f'{x[1][v]}'
    plan[f'G1{v}'] = f'{x[2][v]}'


planilha.save(filename= 'teste.xlsx')