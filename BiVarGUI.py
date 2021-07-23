from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from BiVarCode import *
import numpy as np
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms

window = Tk()
window.title("BiVariate Analysis")
window.geometry('1050x370')

#Entry Section Starts
#lbl1 = Label(window, text="Years")
#lbl1.grid(column=0, row=0)
#var =IntVar()
#var.set(5)
#years = Spinbox(window, from_=1, to=10, width=10,textvariable=var) #Entry(window,width=10)
#years.grid(column=1, row=0)
#2
lbl2 = Label(window, text="Variable 1")
lbl2.grid(column=1, row=0)
expenses = Entry(window,width=20)
expenses.grid(column=2, row=0)
expenses.focus()
#3
lbl3 = Label(window, text="Variable 2")
lbl3.grid(column=3, row=0)
saless = Entry(window,width=20)
saless.grid(column=4, row=0)#1

def click():
    #year=list(range(1,int(years.get())+1))
    global exp
    exp=expenses.get()
    global sales
    sales=saless.get()
    if (len(exp)<=0 or len(sales)<=0):
        messagebox.showinfo('Entry Details','Enter Valid Data')
        return 0  
    exp=exp.split(" ")
    exp=list(map(int,exp))
    sales=sales.split(" ")
    sales=list(map(int,sales))
    if len(exp)!=len(sales):
        messagebox.showinfo('Entry Details','Length of Both Variables Should Match')
        return 0
    Make(exp,sales)
    
txt = scrolledtext.ScrolledText(window,width=70,height=20)
txt.grid(column=0,row=0)
txt.insert(INSERT,'             Mean      Variance      Covariance     Correlation Cfft\n')
txt.insert(INSERT,'--------------------------------------------------------------------\n')
txt.insert(INSERT,'--------------------------------------------------------------------\n')

but = Button(window, text="Observe", command=click)
but.grid(column=1, row=2)

def show():
    mat.scatter(exp,sales)
    mat.show()

def show_r():    
    x=[]
    for i in yy_m:
        x.append(float(i[0]))
    mat.scatter(x,sales)
    mat.show()

def show_rline():
    x1=[]
    for i in yy_m:
        x1.append(float(i[0]))
    mat.plot(x1,sales,c='r')
    mat.show()

btn = Button(window, text="Show Scatter Plot", command=show)
btn.grid(column=2, row=2)

btn = Button(window, text="Show Regression Plot", command=show_r)
btn.grid(column=3, row=2)

btn = Button(window, text="Show Regression Line", command=show_rline)
btn.grid(column=4, row=2)
def get(Y,Z):
    X=[]
    for i in Z:
        X.append(1)
        X.append(i)
    Z=np.array(X)
    Z=Z.reshape((-1,2))
    Z=np.asmatrix(Z)
    Y=np.matrix(Y)
    least_sq(Y,Z)
  

def least_sq(Y,Z):
    Y=Y.T
    #BETA
    Z_T=Z.T
    zmul=Z_T*Z
    B=np.linalg.inv(zmul)
    B=B*Z_T
    B=B*Y
    #B=B.astype('int32')
    #RESIDUAL
    e=Y
    zb=Z*B
    e=e-zb
    #e=e.astype('int32')
    #SUM OF RESIDUAL
    Y_T=Y.T
    res=Y_T*Y
    temp=Y_T*zb
    res=res-temp
    #res=res.astype('int32')
    yy=Z*B
    global yy_m
    yy_m=yy
    global residual
    residual=e
    global rsum
    rsum=res
    global beta
    beta=B

def Make(exp,sales):
    mean_exp=mean(exp)
    mean_sales=mean(sales)
    var_exp=variance(exp,mean_exp)
    var_sales=variance(sales,mean_sales)
    covar=covariance(exp, mean_exp, sales, mean_sales)
    corr=correlation(covar,var_exp,var_sales)
    get(exp,sales)
    write(mean_exp,mean_sales,var_exp,var_sales,covar,corr)


def write(mean_exp,mean_sales,var_exp,var_sales,covar,corr):
    txt.delete(1.0,END)
    txt.insert(INSERT,'             Mean      Variance      Covariance     Correlation Cfft\n')
    txt.insert(INSERT,'--------------------------------------------------------------------\n')
    txt.insert(INSERT,'Variable 1   '+'{:.2f}'.format(mean_exp)+'       {:.2f}'.format(var_exp)+'           {:.2f}'.format(covar)+'          {:.2f}'.format(corr)+'\n')
    txt.insert(INSERT,'Variable 2   '+'{:.2f}'.format(mean_sales)+'       {:.2f}'.format(var_sales)+'           {:.2f}'.format(covar)+'          {:.2f}'.format(corr)+'\n')
    txt.insert(INSERT,'--------------------------------------------------------------------\n\n\n')
    txt.insert(INSERT,'Beta Matrix:\n'+str(beta)+'\n\n')
    txt.insert(INSERT,'Residual Matrix:\n'+str(residual)+'\n\n')
    txt.insert(INSERT,'Residual Sum of Squares Matrix:\n'+str(rsum)+'\n\n')
    txt.insert(INSERT,'Response Vector:\n'+str(yy_m)+'\n\n')

window.mainloop()