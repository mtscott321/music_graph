# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:31:05 2020

@author: mtsco
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
from synthesizer import Player, Synthesizer, Waveform, Writer
player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
writer = Writer()
#%%
LOW_FREQ = 100
HIGH_FREQ = 5000
TIME_LENGTH = 3 #in seconds
DIVISIONS = 10000
DT = TIME_LENGTH * 1.0 / DIVISIONS

#the domain on the graph to be played
X_MIN = 2.5
X_MAX = 4

#the range on the graph expected
Y_MIN = 0
Y_MAX = 1

DILATION = (1.0 *HIGH_FREQ - LOW_FREQ) / (Y_MIN - Y_MAX)

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
"""
x_vals is an array with all of the x values in it that are plugged into the
graph. y_vals is a 2d array where each index (as many as there are x_vals) has space
for 100 values, each of all the y values 
"""

iterations = 1000
x_vals = np.linspace(X_MIN, X_MAX, DIVISIONS)
y_vals = np.ndarray((x_vals.shape[0], last))
how_many = np.zeros(x_vals.shape[0])


last = 100
condition = 1e-5 * np.ones(DIVISIONS)
for i in range(iterations):
    condition = logistic(x_vals, condition)
    
    #only do the last 100 so we can make sure it's stabilized
    if i >= (iterations - last):
        
        plt.plot(x_vals, condition, ',k')
        for t in range(condition.shape[0]):
            print(t)
            """
            rounding so that very small differences don't get stored as independent
            stability/convergence points. only doing here so we don't mess up the
            recursion
            """
            temp = np.around(condition, decimals=3)
            if temp[t] not in y_vals[t]:
                print("adding new value")
                index = how_many[t]
                y_vals[t, int(index)] = temp[t]
                how_many[t] = how_many[t] + 1

#%%
"""
just so i can have a backup in case I run smth stupid so that I 
won't lose the data
"""
save = y_vals
#%%
#just making a holder that we can concatenate to
all_wavs = synthesizer.generate_constant_wave(0, DT)
#for every index of the x values value

for x in range(y_vals.shape[0]):
    total_for_x = synthesizer.generate_constant_wave(0, DT)
    for i in range(0, last):
        print("%dth y value for %dth x value" % (i, x))
        temp = synthesizer.generate_constant_wave(DILATION * y_vals[x, i], DT)
        total_for_x = total_for_x + temp
    all_wavs = np. concatenate((all_wavs, total_for_x))
    print(x)


#%%
player.play_wave(all_wavs)
#%%
path = r"C:\Users\mtsco\OneDrive\Documents\Miscellaneous\Misc_Code\Summer_19_Music_proj"
writer.write_wave(path + "\\bifurcating_logistic1.wav", all_wavs)





