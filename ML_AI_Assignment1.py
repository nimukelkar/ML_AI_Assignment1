# Nirmayi Kelkar
# 31141
import numpy as np
from scipy import stats
from numpy import genfromtxt
from matplotlib import pyplot as plt



def calmean(A): # Function to calculate mean
    mean=np.mean(A)
    return mean
def calmedian(A): # Calculates median
    median=np.median(A)
    return median
def calmode(A):    # Calculates median
    x=stats.mode(A)
    return(x[0])
def calvar(A):     #Calculates variance
    var=np.var(A)
    return var
def calstd(A):      # Calculates standard deviation
    std=np.std(A)
    return std
def calcovariance(X,Y):
    covar=np.cov(X,Y)[0,1]
    return covar
def corrcoeff(X,Y):
    corcoef=np.corrcoef(X,Y)[0,1]
    return corcoef
def calerror(B):
    stderr=np.std(B,ddof=1)/np.sqrt(np.size(B))
    return stderr

B=genfromtxt('height.csv',delimiter=',',skip_header=1) # Is an array of heights got from the csv file
C=genfromtxt('weight.csv',delimiter=',',skip_header=1) # Is an array of weights got from the csv file

print("The height details of data is")  # Calling the respective function for heights array
Bmean=calmean(B)
Bmedian=calmedian(B)
Bmode=calmode(B)
Bvar=calvar(B)
Bstd=calstd(B)
Berror=calerror(B)
print("The mean is",Bmean)
print("The median is",Bmedian)
print("The mode is",Bmode)
print("The variance is",Bvar)
print("The standard deviation is",Bstd)
print("The standard error in heights is",Berror)

plt.hist(B)   # Plots the histogram for mode, mean, median
measurements=[Bmode,Bmedian,Bmean]
names=["mode","median","mean"]
colors=["green","blue","orange"]
for measures,name,color in zip(measurements,names,colors):
    plt.axvline(x=measures,linestyle='--',linewidth=2.5,label='{0} at {1}'.format (name,measures),c=color)
plt.legend()
plt.show()  # Displays the histogram
print("\n\n")
print("The weight details of data is")  # Calls the function for the weights data
Cmean=calmean(C)
Cmedian=calmedian(C)
Cmode=calmode(C)
Cvar=calvar(C)
Cstd=calstd(C)
Cerror=calerror(C)
print("The mean is",Cmean)  #Displays required quantities
print("The median is",Cmedian)
print("The mode is",Cmode)
print("The variance is",Cvar)
print("The standard deviation is",Cstd)
print("The standard error in weights is",Cerror)

plt.hist(C)  #Plots histogram for weight
measurements=[Cmode,Cmedian,Cmean]
names=["mode","median","mean"]
colors=["green","blue","orange"]
for measures,name,color in zip(measurements,names,colors):
    plt.axvline(x=measures,linestyle='--',linewidth=2.5,label='{0} at {1}'.format(name,measures),c=color)
plt.legend()
plt.show()

cov=calcovariance(B,C)
corcoef=corrcoeff(B,C)

print("\n\n")

print("The calculated covariance in height and weight is",cov)
print("The calculated correlation coefficient for height and weight is",corcoef)





