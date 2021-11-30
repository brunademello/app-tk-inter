from tkinter import *
from tkinter.font import BOLD

list_equipamento = ['Fabricante', 'Modelo', 'Número de série']
list_campo = ['d1', 'd2', 'd3', 'd4', 'd5']
list_padrao = ['dp1', 'dp2', 'dp3', 'dp4', 'dp5']
list_dados_corrigidos = ['dr1', 'dr2', 'dr3', 'dr4', 'dr5']

def frame_construct(root):

    entries = {}

    # dados do equipamento

    frame_equipamento = Frame(root, width=100, highlightbackground='silver', highlightthickness=1)
    frame_equipamento.grid(row=0, column=0, padx=10, pady=20, ipadx=20, ipady=20)

    lab = Label(frame_equipamento, fg='black', text='Especificação do Instrumento', font=("Arial", 12, BOLD))
    lab.grid(row=0, column=0, padx=10, pady=10, columnspan=2, rowspan=2)

    row_number=2

    for field in list_equipamento:
        lab = Label(frame_equipamento, text=field+":", fg='black', font=("Arial", 12))
        lab.grid(row=row_number, column=0, padx=10, pady=10)

        ent=Entry(frame_equipamento,fg='black',font=("Arial", 10), width=20)
        ent.grid(row=row_number,column=1,ipadx=5, ipady=5)

        entries[field]=ent
        row_number=row_number+1

    # dados de campo e padrao

    frame_campo_padrao = Frame(root, width=100, highlightbackground='silver', highlightthickness=1)
    frame_campo_padrao.grid(row=0,column=1, padx=10, pady=20, ipadx=20, ipady=20)

    lab = Label(frame_campo_padrao, fg='black', text='Valores de Campo', font=("Arial", 12, BOLD))
    lab.grid(row=0, column=1, padx=10, pady=10)

    row_number=1

    for field in list_campo:
        lab = Label(frame_campo_padrao, fg='black', text=str(row_number)+".", font=("Arial", 12))
        lab.grid(row=row_number, column=0, padx=10, pady=10)

        ent=Entry(frame_campo_padrao,fg='black',font=("Arial", 10), width=14)
        ent.grid(row=row_number,column=1,ipadx=5, ipady=5)

        entries[field]=ent
        row_number=row_number+1

    row_number=1

    lab = Label(frame_campo_padrao, fg='black', text='Valores Padrão', font=("Arial", 12, BOLD))
    lab.grid(row=0, column=4, padx=10, pady=10)

    for field in list_padrao:
        lab = Label(frame_campo_padrao, fg='black', text=str(row_number-1)+".", font=("Arial", 12))
        lab.grid(row=row_number, column=4, padx=10, pady=10)

        ent=Entry(frame_campo_padrao,fg='black',font=("Arial", 10), width=14)
        ent.grid(row=row_number,column=4,ipadx=5, ipady=5)

        entries[field]=ent
        row_number=row_number+1


    # Distancias ajustadas

    frame_resposta = Frame(root, width=100, highlightbackground='silver', highlightthickness=1)
    frame_resposta.grid(row=1,column=0, padx=10, pady=20, ipadx=20, ipady=20, columnspan=2)

    lab = Label(frame_resposta, fg='black', text='Valores corrigidos', font=("Arial", 12, BOLD))
    lab.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    row_number=1

    for field in list_dados_corrigidos:
        lab = Label(frame_resposta, fg='black', text=str(row_number)+".", font=("Arial", 12))
        lab.grid(row=row_number, column=0, padx=10, pady=10)

        ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
        ent.grid(row=row_number,column=1,ipadx=5, ipady=5)

        entries[field]=ent
        row_number=row_number+1

    # Erro de zero

    lab = Label(frame_resposta, fg='black', text="Erro de zero = ", font=("Arial", 12, BOLD))
    lab.grid(row=1, column=3, padx=10, pady=10)

    ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    ent.grid(row=1,column=4,ipadx=5, ipady=5)

    entries['e1'] = ent

    lab = Label(frame_resposta, fg='black', text="mm  ±", font=("Arial", 12))
    lab.grid(row=1, column=5, padx=10, pady=10)

    ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    ent.grid(row=1,column=6,ipadx=5, ipady=5)

    entries['e2'] = ent

    lab = Label(frame_resposta, fg='black', text="mm", font=("Arial", 12))
    lab.grid(row=1, column=7, padx=10, pady=10)

    # Fator de Escala 

    lab = Label(frame_resposta, fg='black', text="Fator de escala = ", font=("Arial", 12, BOLD))
    lab.grid(row=3, column=3, padx=10, pady=10)

    ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    ent.grid(row=3,column=4,ipadx=5, ipady=5)

    entries['f1'] = ent

    lab = Label(frame_resposta, fg='black', text="ppm ±", font=("Arial", 12))
    lab.grid(row=3, column=5, padx=10, pady=10)

    ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    ent.grid(row=3,column=6,ipadx=5, ipady=5)

    entries['f2'] = ent

    lab = Label(frame_resposta, fg='black', text="ppm", font=("Arial", 12))
    lab.grid(row=3, column=7, padx=10, pady=10)

    # Acurácia

    lab = Label(frame_resposta, fg='black', text="Acurácia = ", font=("Arial", 12, BOLD))
    lab.grid(row=5, column=3, padx=10, pady=10)

    ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    ent.grid(row=5,column=4,ipadx=5, ipady=5)

    entries['A'] = ent

    lab = Label(frame_resposta, fg='black', text="mm", font=("Arial", 12))
    lab.grid(row=5, column=5, padx=10, pady=10)

    # Tendência

    #lab = Label(frame_resposta, fg='black', text="Tendência = ", font=("Arial", 12, BOLD))
    #lab.grid(row=4, column=3, padx=10, pady=10)

    #ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    #ent.grid(row=4,column=4,ipadx=5, ipady=5)

    #entries['T'] = ent

    #lab = Label(frame_resposta, fg='black', text="mm", font=("Arial", 12))
    #lab.grid(row=4, column=5, padx=10, pady=10)

    # Precisão

    #lab = Label(frame_resposta, fg='black', text="Precisão = ", font=("Arial", 12, BOLD))
    #lab.grid(row=5, column=3, padx=10, pady=10)

    #ent=Entry(frame_resposta,fg='black',font=("Arial", 10), width=14)
    #ent.grid(row=5,column=4,ipadx=5, ipady=5)

    #entries['P'] = ent

    #lab = Label(frame_resposta, fg='black', text="mm", font=("Arial", 12))
    #lab.grid(row=5, column=5, padx=10, pady=10)

    return entries
