# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:31:05 2020

@author: mtsco
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
LOW_FREQ = 100
HIGH_FREQ = 5000
TIME_LENGTH = 3 #in seconds
DIVISIONS = 10000
DT = TIME_LENGTH * 1.0 / DIVISIONS

#the domain on the graph to be played
X_MIN = 2.5
X_MAX = 4

# from synthesizer import Player, Synthesizer, Waveform
# player = Player()
# player.open_stream()
# synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# player.play_wave(synthesizer.generate_constant_wave(HIGH_FREQ, 1))

#%%


#%%
plt.figure(dpi = 500)
plt.title("Bifurcating Logistic Graph")
def logistic(r, x):
    return r * x * (1 - x)

iterations = 1000
x_vals = np.linspace(X_MIN, X_MAX, DIVISIONS)
y_vals = np.ndarray((x_vals.shape[0], iterations))


last = 100
condition = 1e-5 * np.ones(DIVISIONS)
for i in range(iterations):
    condition = logistic(x_vals, condition)
    # We display the bifurcation diagram.
    if i >= (iterations - last):
        plt.plot(x_vals, condition, ',k')


#%%
iterations = 1000
x_vals = np.linspace(X_MIN, X_MAX, DIVISIONS)
y_vals = np.ndarray((x_vals.shape[0], iterations))

plt.figure(dpi = 1000)
last = 100
condition = 1e-5

for t in range(x_vals.shape[0]):
    x = x_vals[t]
    
    for i in range(iterations):
        condition = logistic(x, condition)
        # We display the bifurcation diagram.
        if i >= (iterations - last):
            plt.plot(x, condition, ',k')
            #if condition not in y_vals[t]:
                #y_vals[t].append(condition)
#%%

iterations = 1000
x_vals = np.linspace(X_MIN, X_MAX, DIVISIONS)
y_vals = np.ndarray((x_vals.shape[0], iterations))


last = 100
condition = 1e-5 * np.ones(DIVISIONS)
for i in range(iterations):
    condition = logistic(x_vals, condition)
    # We display the bifurcation diagram.
    print(i)
    if i >= (iterations - last):
        plt.plot(x_vals, condition, ',k')
        for t in range(condition.shape[0]):
            print(t)
            if condition[t] not in y_vals[t]:
                y_vals[t].append(condition(t))



