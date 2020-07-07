"""
This program creates an aural interpretation of
a bifurcating logistic graph

Created by Madeline Scott
17 June 2020
"""

import numpy as np
import matplotlib.pyplot as plt
from synthesizer import Player, Synthesizer, Waveform
import math

player = Player()
player.open_stream()


synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# Play A4

wav1 = synthesizer.generate_constant_wave(440.0, 0.1)
wav2 = synthesizer.generate_constant_wave(340.0, 0.1)
wav4 = np.concatenate((wav1, wav2))
print(wav4)
wav3 = wav1 + wav2
print(type(wav3))
player.play_wave(wav4)

#%%
"""
Global variables
"""
TIME_LENGTH = 3 #in seconds
DIVISIONS = 500
DT = TIME_LENGTH * 1.0 / DIVISIONS

#%%

fig = plt.figure()
plt.plot(x, func1(x))
plt.plot(x, func2(x))

#%%
def func1(t):
    return(2*t**3 -19*t**2 + t + 500)

def func2(t):
    return(45*t +300)

x = np.linspace(0, 10, DIVISIONS)

fig = plt.figure()
plt.plot(x, func1(x))
plt.plot(x, func2(x))

funcs_arr = [func1, func2]

"""
for each value in the funcs array, add all the wawvs together
"""
def sum_funcs(f_arr, t):
    all_wav_inst = synthesizer.generate_constant_wave(0, DT) 
    for f in f_arr:
        wav = synthesizer.generate_constant_wave(f(t), DT)
        all_wav_inst = all_wav_inst + wav
    return all_wav_inst

"""
concatenates all the individual t-waves to create a sound
"""
def sum_over_time(x_vals, f_arr):
    f = -1
    i = 0
    for t in x_vals:
        print(i)
        i = i+1
        t_wav = sum_funcs(f_arr, t)
        
        
        
        if type(f) == int:
            f = t_wav
        else:
            f = np.concatenate((f, t_wav))
    return f

#%%
attempted_wav_1 = sum_over_time(x, funcs_arr)

#%%
player.play_wave(attempted_wav_1)

#%%
def func1(t):
    return(2*t**3 -19*t**2 + t + 500)

def func2(t):
    return(45*t +300)

x = np.linspace(0, 10, 20)

fig = plt.figure()
plt.plot(x, func1(x))
plt.plot(x, func2(x))

funcs_arr = [func1, func2]
#%%

print(x)

#temp_t_equals_0 = sum_funcs(funcs_arr, 0)
#player.play_wave(temp_t_equals_0)
all_wav_inst = np.zeros((4410, 1))
player.play_wave(all_wav_inst)
y0 = funcs_arr[0](0)
y0_wav = synthesizer.generate_constant_wave(y0, 0.5)
player.play_wave(y0_wav)
y1 = funcs_arr[1](0)
y1_wav = synthesizer.generate_constant_wave(y1, 0.5)
player.play_wave(y1_wav)

y2_wav = y1_wav + y0_wav
player.play_wave(y2_wav)

#%%
all_wav_inst = np.zeros((4410, 1))
player.play_wave(all_wav_inst)
y0 = funcs_arr[0](3)
y0_wav = synthesizer.generate_constant_wave(y0, 0.5)
player.play_wave(y0_wav)
y1 = funcs_arr[1](3)
y1_wav = synthesizer.generate_constant_wave(y1, 0.5)
player.play_wave(y1_wav)

y2_wav = y1_wav + y0_wav
player.play_wave(y2_wav)

#%%
plt.plot(np.linspace(0, 220, 220), y0_wav)

plt.plot(np.linspace(0, 220, 220), y1_wav)
plt.plot(np.linspace(0, 220, 220), y2_wav)

#%%
temp = synthesizer.generate_constant_wave(0, 0.5) 
for f in funcs_arr:
    
    wav = synthesizer.generate_constant_wave(f(0), 0.5)
    print(wav.shape)
    print (f(0))
    temp = temp + wav
    
print(temp.shape)
player.play_wave(temp)

