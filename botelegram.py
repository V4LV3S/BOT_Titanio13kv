import telebot
from openpyxl import load_workbook
from funcs import organizador, sep_ci, elim_vtr, sep_pgm, sep_vtr
from datetime import datetime

#BOT CONFIG
CHAVE_API = "5794326949:AAF1Jywq9pxuqlrPtBFI4mEmlfK2H8qFjaM"
bot = telebot.TeleBot(CHAVE_API)

# Planilha
planilha = load_workbook('exped_rec.xlsx')
plan = planilha.active



@bot.message_handler(commands = ['REG'])
def registrar(mensagem):

    texto ="""
Registre o recebimento com o comando /REC

(---------------EXEMPLO----------------)
/REC CI:07 CINE-HOLLIUDY VTR:M030

REFLETOR1-ATIVO1/HORA1-ATIVO2/HORA2

REFLETOR2-ATIVO1/HORA1-ATIVO2/HORA2

É necessário seguir essa formatação perfeitamente, caso contrário vai dar merda!
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands = ['BASE'])
def texto_base(mensagem):
    texto ="""
/REC CI:XX PGM VTR:M0XX

HMI575-

HMI1200-

AS18-

ARRIX-

4KW-

M40-
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands = ['REC'])
def recebimento(mensagem):

    try:
        recebimento = mensagem.text
        recebimento = recebimento.split()  # ['/OP1', 'CI:10', 'TODAS-AS-FLORES', 'VTR:M015', 'M40-123456/HL1-123456/HL2', 'HMI1200-654321/HL3-654321/HL4']
        x = organizador(recebimento)

        plan['D2'] = f'{sep_pgm(recebimento[2])}'
        plan['D3'] = f'{(recebimento[1])}'
        plan['D4'] = f'{elim_vtr(recebimento[3])}'
        plan['D5'] = datetime.now().strftime('%H:%M:%S')
        
        for v in range(len(x[0])):

            plan[f'C1{v}'] = f'{x[0][v]}'
            plan[f'E1{v}'] = f'{x[1][v]}'
            plan[f'G1{v}'] = f'{x[2][v]}'


        planilha.save(filename= f'{sep_ci(recebimento[1])}.xlsx')
        print(f'RECEBIMENTO // {recebimento[1]} // {sep_pgm(recebimento[2])} // {sep_vtr(recebimento[3])}')
        bot.reply_to(mensagem, "CI registrada!")
    except:
        bot.reply_to(mensagem, "Ocorreu algum erro! Verifique a formatação da mensagem")
    


# Final do código (MENSAGEM PADRAO)

def verificar(mensagem):  
    '''Verifica a mensagem que manda e retorna True pra qualquer mensagem'''
    return True


@bot.message_handler(func = verificar)
def responder(mensagem):

    texto = """
Escolha uma opção: 

/REG Registrar CI

/BASE Pegar o texto base das CIs


Responder qualquer outra coisa não irá funcionar!
    """
    bot.reply_to(mensagem, texto)


bot.polling()