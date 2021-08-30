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

B=genfromtxt('height.csv',delimiter=',',skip_header=1) # Is an array of heights got from the csv file
C=genfromtxt('weight.csv',delimiter=',',skip_header=1) # Is an array of weights got from the csv file

print("The height details of data is")  # Calling the respective function for heights array
Bmean=calmean(B)
Bmedian=calmedian(B)
Bmode=calmode(B)
Bvar=calvar(B)
Bstd=calstd(B)
print("The mean is",Bmean)
print("The median is",Bmedian)
print("The mode is",Bmode)
print("The variance is",Bvar)
print("The standard deviation is",Bstd)
