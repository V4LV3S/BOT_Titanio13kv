
# ['/OP1', 'CI:10', 'TODAS-AS-FLORES', 'VTR:M015', 'M40-123456/HL1-123456/HL2', 'HMI1200-654321/HL3-654321/HL4', 'AS18-ativo1/hlat-ativ2/fdsf-ativ4/adsda']

def organizador(registro):

    cab =[]
    ativ = []
    hl = []

    for elementos in registro[4:] :
        
        refletor = elementos.split('-')
        

        for info in refletor[1:]:
            info = info.split('/')
            ativ.append(info[0])
            hl.append(info[1])

        while len(cab) != (len(ativ)):
            cab.append(refletor[0])

    return [cab, ativ, hl]

def sep_vtr(vtr: str)-> str:
    
    if ':' in vtr:
        vtr = vtr.replace(':',' ')
    else:
        vtr = vtr
    return vtr

def elim_vtr(vtr: str)-> str:

    sep = vtr.split(':')

    return sep[1]


def sep_ci(ci: str)-> str:

    if ':' in ci:
        ci = ci.replace(':','_')
    else:
        ci = ci
    return ci

def sep_pgm(pgm: str)-> str:

    if '-' in pgm:
        pgm = pgm.replace('-',' ')
    else:
        pgm = pgm
    return pgm


