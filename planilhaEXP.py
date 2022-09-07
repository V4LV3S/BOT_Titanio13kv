from openpyxl import load_workbook

def verificador_plan(arquivo):
    planilha = load_workbook(f'REC_{arquivo}.xlsx')
    plan = planilha.active

    cab = []
    ativ = []
    hl = []

    for v in range(10, 39):
        if (plan[f'C{v}'].value != None):
            cab.append(plan[f'C{v}'].value)
            ativ.append(plan[f'E{v}'].value)
            hl.append(plan[f'G{v}'].value)
    
    """cab_formatado = []
    for nome in cab:
        if nome not in cab_formatado:
            cab_formatado.append(nome)
    print(cab_formatado)"""
    info = []
    for x in range(len(cab)):
        info.append(f"{cab[x]}-{ativ[x]}-{hl[x]}")
    return info  #  ['M40-oooooo-aaaaaaaaaa', 'M40-123456-HL1', 'M40-123456-HL2', 'HMI1200-654321-HL3', 'HMI1200-654321-HL4', 'HMI1200-dasdsad-kdskadk']
