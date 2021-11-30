from tkinter import *
import numpy as np
from frames import frame_construct


def calculando_afericao(entries):

    results = {'dr1': 0, 'dr2': 0, 'dr3': 0, 'dr4': 0, 'dr5': 0, 'e1': 0, 'e2':0, 'f1': 0, 'f2': 0, 'A': 0} #'T': 0, 'P': 0}

    #d = np.array([31.245, 104.736, 274.545, 574.702, 1200.105])
    #dp = np.array([31.253, 104.740, 274.555, 574.708, 1200.105])

    try:
        d = np.array([float(entries['d1'].get()), float(entries['d2'].get()), float(entries['d3'].get()), float(entries['d4'].get()), float(entries['d5'].get())])
        dp = np.array([float(entries['dp1'].get()), float(entries['dp2'].get()), float(entries['dp3'].get()), float(entries['dp4'].get()), float(entries['dp5'].get())])

        zipped_lists = zip(d, dp)

        res = np.array([x - y for (x,y) in zipped_lists])

        A1 = np.ones(5).transpose()
        A = np.array([[x,y] for (x,y) in zip(A1, d)])

        Xa1 = np.linalg.inv(A.transpose().dot(A))
        Xa2 = Xa1.dot(A.transpose())
        Xa = Xa2.dot(res)
        Xa = [round(x,8) for x in Xa]

        v = [(x - y) for (x,y) in zip(np.matmul(A, Xa), res)]

        Varp = np.matmul(np.array(v).transpose(), v)

        P1 = np.power(np.abs(v), -2)

        P = [[P1[0], 0, 0, 0, 0],
                [0, P1[1], 0, 0, 0],
                [0, 0, P1[2], 0, 0],
                [0, 0, 0, P1[3], 0],
                [0, 0, 0, 0, P1[4]],
                ]

        Xa1 = A.transpose().dot(P)
        Xa11 = Xa1.dot(A)
        Xa2 = np.linalg.inv(Xa11)
        Xa3 = Xa2.dot(A.transpose())
        Xa4 = Xa3.dot(P)
        Xa = Xa4.dot(res)

        v1 = A.dot(Xa)

        v = np.array([x - y for (x,y) in zip(v1, res)])

        Varp1 = v.transpose().dot(P)

        Varp = Varp1.dot(v) 

        Xa1 = A.transpose().dot(P)
        Xa11 = Xa1.dot(A)
        somatorio_Xa = np.linalg.inv(Xa11)

        sigma_Xa = np.sqrt(np.diag(somatorio_Xa))

        Xa22 = Xa[1]*(-1) + 1
        Xa2 = [Xa[0]*(-1), Xa22]

        La = A.dot(Xa2)

        # Acurácia
        Ac = np.sqrt((res.transpose().dot(res))/len(res))

        # Tendencia 
        #e = np.mean(res)*(-1)            

        # Precisão
        #p = np.std(res)        

        results = {'dr1': int(La[0] * 10**3)/10**3,
                   'dr2': int(La[1] * 10**3)/10**3,
                   'dr3': int(La[2] * 10**3)/10**3, 
                   'dr4': int(La[3] * 10**3)/10**3, 
                   'dr5': int(La[4] * 10**3)/10**3, 
                   'e1': float(round(Xa[0]*(-1)*1000, 2)),
                   'e2': float(round(sigma_Xa[0]*1000, 2)),
                   'f1': float((int(Xa2[1] * 10**3)/10**3)),
                   'f2': float(int((sigma_Xa[1]*1000000) * 10**3)/10**3),
                   'A': float((int(Ac * 10**4)/10**4)*1000)}
                   #'T': float(round(e*1000,1)),
                   #'P': float(round(p*1000,1))}

        #deletando resultados e printando de acordo com cada entrada

        for key in results:
            entries[key].delete(0,END)
            entries[key].insert(0, results[key])
        
    
    except:
        #raise Exception 
        for key in results:
            entries[key].insert(0, results[key])

if __name__ == '__main__':
   root = Tk()
   root.title('Aferição de EDM segundo a ISO 17123-4')   
   ents = frame_construct(root)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Calcular', font=("Arial", 12), command=(lambda e = ents: calculando_afericao(e)))
   b1.grid(row =2, column = 0, columnspan=2, padx=20, pady=20)
   b2 = Button(root, text = 'Sair', font=("Arial", 12), command = root.quit)
   b2.grid(row =3, column = 0, columnspan=2, padx=5, pady=5)
   root.mainloop()
