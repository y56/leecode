#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:32:00 2020

@author: y56
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,500,1000)
y = np.sqrt(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

## Major ticks every 20, minor ticks every 5
#major_ticks = np.arange(0, 101, 1)
#minor_ticks = np.arange(0, 101, 1)
#
#ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
#ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)
#
## And a corresponding grid
#ax.grid(which='both')
#
## Or if you want different settings for the grids:
#ax.grid(which='minor', alpha=0.2)
#ax.grid(which='major', alpha=0.5)

plt.plot(x,y)
plt.plot(x,np.floor(y))

# %%


x = 35
l = 2
r = x // 2
plt.plot([x],[x**.5 + 1], 'go')
plt.plot([r**2],[r], 'ro')
plt.plot([l**2],[l], 'bo')
while r >= l:
    m = (l + r) // 2
    plt.plot([m**2],[m], 'k.')
    m2 = m ** 2
    if m2 > x:
        r = m - 1
        plt.plot([r**2],[r], 'ro')
    elif m2 < x:
        l = m + 1
        plt.plot([l**2],[l], 'bo')
    else: # ==   
        break
# r

plt.show()