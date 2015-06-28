from __future__ import division
import sys
import os
import matplotlib.pyplot as plt
import scipy
from scipy import special

mydir = os.path.expanduser("~/")
sys.path.append(mydir + "/GitHub/PeasantMath/Roots/code")
import functions as fxn


ks = [2,3,4,5,6,7,8,9,10]

for i, k in enumerate(ks):

    fig = plt.figure()
    ax = fig.add_subplot(2,2,1)

    x = 2.0
    xs = []
    rts = []
    WLs = []

    for j in range(100):

        xs.append(x)
        y = x**(1.0/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        WLs.append(a)
        x += 1

    plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
    plt.scatter(xs, WLs, color='c', alpha=0.9, label='WHL rule')
    #plt.yscale('log')
    #plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    leg = plt.legend(loc=4,prop={'size':12})
    leg.draw_frame(False)
    #plt.text(-50, 14, "How well does the WHL Rule approximate square roots?", fontsize=16)



    ax = fig.add_subplot(2,2,2)
    x = 2.0
    xs = []
    rts = []
    WLs = []

    for j in range(100):

        xs.append(x)
        y = x**(1/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        WLs.append(a)
        x += 10

    plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
    plt.scatter(xs, WLs, color='c', alpha=0.9, label='WHL rule')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    leg = plt.legend(loc=2,prop={'size':12})
    leg.draw_frame(False)



    ax = fig.add_subplot(2,2,3)
    x = 2.0
    xs = []
    rts = []
    WLs = []

    for j in range(30):

        xs.append(x)
        y = x**(1/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        WLs.append(a)
        x = x*1.5


    plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
    plt.scatter(xs, WLs, color='c', alpha=0.9, label='WHL rule')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    leg = plt.legend(loc=4,prop={'size':12})
    leg.draw_frame(False)



    ax = fig.add_subplot(2,2,4)
    x = 2.0
    xs = []
    rts = []
    WLs = []

    for j in range(30):

        xs.append(x)
        y = x**(1/k)
        rts.append(y)
        a = fxn.WHL_kth(x, k)
        WLs.append(a)
        x = x*2

    plt.scatter(xs, rts, s=50, color='m', facecolors='none', label='root'+str(int(k)))
    plt.scatter(xs, WLs, color='c', alpha=0.9, label='WHL rule')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    leg = plt.legend(loc=4,prop={'size':13})
    leg.draw_frame(False)

    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.subplots_adjust(wspace=0.5, hspace=0.3)
    plt.savefig(mydir+'/GitHub/PeasantMath/Roots/figs/WHL_root'+str(int(k))+'.png', dpi=600)#, bbox_inches = 'tight')#, pad_inches=0)
    print 'finished root',k
    #plt.show()
