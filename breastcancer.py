import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score, balanced_accuracy_score

from tkinter import *
import tkinter
import tkinter.messagebox
url = "https://drive.google.com/uc?id=1r7-u4BC1Dm0YqrPegmWlvt5q20Oyh2mF&export=download"
bc=pd.read_csv(url)

df = bc.copy()
df.drop('id', axis=1, inplace=True)

from sklearn.preprocessing import StandardScaler
df['diagnosis'] = df['diagnosis'].map({'M':1,'B':0})
X_train,X_test,y_train,y_test = train_test_split(df[df.columns.drop('diagnosis')].to_numpy(),df['diagnosis'].to_numpy(),random_state=42,train_size=0.7)
scaler = StandardScaler() #create an instance of standard scaler
scaler.fit(X_train) # fit it to the training data

scaler.transform(X_train) #transform training data
scaler.transform(X_test) #transform validation data
y_train = pd.Series(y_train)

def train_evaluate_model(model, X_train, y_train, X_test,y_test):
  
    model.fit(X_train, y_train)  #fi t the model instance
    predictions = model.predict(X_test) # calculate predictions


lg = LogisticRegression(max_iter=3000)
results = train_evaluate_model(lg, X_train, y_train, X_test, y_test)


def proces():
    number1 = float(Entry.get(E1))
    number2 = float(Entry.get(E2))
    number3 = float(Entry.get(E3))
    number4 = float(Entry.get(E4))
    number5 = float(Entry.get(E5))
    number6 = float(Entry.get(E6))
    number7 = float(Entry.get(E7))
    number8 = float(Entry.get(E8))
    number9 = float(Entry.get(E9))
    number10 = float(Entry.get(E10))
    number11 = float(Entry.get(E11))
    number12 = float(Entry.get(E12))
    number13 = float(Entry.get(E13))
    number14 = float(Entry.get(E14))
    number15 = float(Entry.get(E15))
    number16 = float(Entry.get(E16))
    number17 = float(Entry.get(E17))
    number18 = float(Entry.get(E18))
    number19 = float(Entry.get(E19))
    number20 = float(Entry.get(E20))
    number21 = float(Entry.get(E21))
    number22 = float(Entry.get(E22))
    number23 = float(Entry.get(E23))
    number24 = float(Entry.get(E24))
    number25 = float(Entry.get(E25))
    number26 = float(Entry.get(E26))
    number27 = float(Entry.get(E27))
    number28 = float(Entry.get(E28))
    number29 = float(Entry.get(E29))
    number30 = float(Entry.get(E30))

    numbers_array = []
    numbers_array.append(number1)
    numbers_array.append(number2)
    numbers_array.append(number3)
    numbers_array.append(number4)
    numbers_array.append(number5)
    numbers_array.append(number6)
    numbers_array.append(number7)
    numbers_array.append(number8)
    numbers_array.append(number9)
    numbers_array.append(number10)
    numbers_array.append(number11)
    numbers_array.append(number12)
    numbers_array.append(number13)
    numbers_array.append(number14)
    numbers_array.append(number15)
    numbers_array.append(number16)
    numbers_array.append(number17)
    numbers_array.append(number18)
    numbers_array.append(number19)
    numbers_array.append(number20)
    numbers_array.append(number21)
    numbers_array.append(number22)
    numbers_array.append(number23)
    numbers_array.append(number24)
    numbers_array.append(number25)
    numbers_array.append(number26)
    numbers_array.append(number27)
    numbers_array.append(number28)
    numbers_array.append(number29)
    numbers_array.append(number30)

    outer_array = []
    outer_array.append(numbers_array)

    y_predictlg = lg.predict(outer_array)
    morb = y_predictlg[0]
    if morb == 1:
        answer= 'Malignant'
        
    elif morb == 0:
        answer='Benign'

    else :
        answer='Error'

    Entry.insert(E31,0,answer)
    print(answer)

top = tkinter.Tk()

L0 = Label(top, text="Insert Measurement of Cell Nucleus",bg="yellow",height=2).grid(row=0,column=0)
L1 = Label(top, text="radius_mean").grid(row=1, column=0)
L2 = Label(top, text="texture_mean").grid(row=2, column=0)
L3 = Label(top, text="perimeter_mean").grid(row=3, column=0)
L4 = Label(top, text="area_mean").grid(row=4, column=0)
L5 = Label(top, text="smoothness_mean").grid(row=5, column=0)
L6 = Label(top, text="compactness_mean").grid(row=6, column=0)
L7 = Label(top, text="concavity_mean").grid(row=7, column=0)
L8 = Label(top, text="concave points_mean").grid(row=8, column=0)
L9 = Label(top, text="symmetry_mean").grid(row=9, column=0)
L10 = Label(top, text="fractal_dimension_mean").grid(row=10, column=0)
L11 = Label(top, text="radius_se").grid(row=1, column=2)
L12 = Label(top, text="texture_se").grid(row=2, column=2)
L13 = Label(top, text="perimeter_se").grid(row=3, column=2)
L14 = Label(top, text="area_se").grid(row=4, column=2)
L15 = Label(top, text="smoothness_se").grid(row=5, column=2)
L16 = Label(top, text="compactness_se").grid(row=6, column=2)
L17 = Label(top, text="concavity_se").grid(row=7, column=2)
L18 = Label(top, text="concave points_se").grid(row=8, column=2)
L19 = Label(top, text="symmetry_se").grid(row=9, column=2)
L20 = Label(top, text="fractal_dimension_se").grid(row=10, column=2)
L21 = Label(top, text="radius_worst").grid(row=1, column=4)
L22 = Label(top, text="texture_worst").grid(row=2, column=4)
L23 = Label(top, text="perimeter_worst").grid(row=3, column=4)
L24 = Label(top, text="area_worst").grid(row=4, column=4)
L25 = Label(top, text="smoothness_worst").grid(row=5, column=4)
L26 = Label(top, text="compactness_worst").grid(row=6, column=4)
L27 = Label(top, text="concavity_worst").grid(row=7, column=4)
L28 = Label(top, text="concave points_worst").grid(row=8, column=4)
L29 = Label(top, text="symmetry_worst").grid(row=9, column=4)
L30 = Label(top, text="fractal_dimension_worst").grid(row=10, column=4)
L31 = Label(top, text="Result").grid(row=15, column=2)
L32 = Label(top, text="For WQD7001 GA").grid(row=15, column=0,sticky="sw")
L33 = Label(top, text="By Group 7 - 5A's").grid(row=16, column=0,sticky="nw")

E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)
E5 = Entry(top, bd=5)
E5.grid(row=5, column=1)
E6 = Entry(top, bd=5)
E6.grid(row=6, column=1)
E7 = Entry(top, bd=5)
E7.grid(row=7, column=1)
E8 = Entry(top, bd=5)
E8.grid(row=8, column=1)
E9 = Entry(top, bd=5)
E9.grid(row=9, column=1)
E10 = Entry(top, bd=5)
E10.grid(row=10, column=1)
E11 = Entry(top, bd=5)
E11.grid(row=1, column=3)
E12 = Entry(top, bd=5)
E12.grid(row=2, column=3)
E13 = Entry(top, bd=5)
E13.grid(row=3, column=3)
E14 = Entry(top, bd=5)
E14.grid(row=4, column=3)
E15 = Entry(top, bd=5)
E15.grid(row=5, column=3)
E16 = Entry(top, bd=5)
E16.grid(row=6, column=3)
E17 = Entry(top, bd=5)
E17.grid(row=7, column=3)
E18 = Entry(top, bd=5)
E18.grid(row=8, column=3)
E19 = Entry(top, bd=5)
E19.grid(row=9, column=3)
E20 = Entry(top, bd=5)
E20.grid(row=10, column=3)
E21 = Entry(top, bd=5)
E21.grid(row=1, column=5)
E22 = Entry(top, bd=5)
E22.grid(row=2, column=5)
E23 = Entry(top, bd=5)
E23.grid(row=3, column=5)
E24 = Entry(top, bd=5)
E24.grid(row=4, column=5)
E25 = Entry(top, bd=5)
E25.grid(row=5, column=5)
E26 = Entry(top, bd=5)
E26.grid(row=6, column=5)
E27 = Entry(top, bd=5)
E27.grid(row=7, column=5)
E28 = Entry(top, bd=5)
E28.grid(row=8, column=5)
E29 = Entry(top, bd=5)
E29.grid(row=9, column=5)
E30 = Entry(top, bd=5)
E30.grid(row=10, column=5)
frame = tkinter.Frame(
            master=top,
            relief=tkinter.RAISED,
            borderwidth=1
        )
frame.grid(row=13, column=3, padx=10, pady=10)
E31 = Entry(top, bd=5)
E31.grid(row=15, column=3)
frame2 = tkinter.Frame(
            master=top,
            relief=tkinter.RAISED,
            borderwidth=1
        )
frame2.grid(row=16, column=3, padx=10, pady=10)
frame3 = tkinter.Frame(
            master=top,
            relief=tkinter.RAISED,
            borderwidth=1
        )
frame3.grid(row=11, column=3, padx=8, pady=8)
B=Button(top, text ="Submit",command = proces, width=10, height=2,).grid(row=12,column=3,)

top.mainloop()


