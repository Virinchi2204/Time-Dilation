#Aim : To Depict relativity of time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Function to calculate Lorentz Factor
def lorentz_factor(c, v):
    gamma = 1 / (np.sqrt(1 - ((v / c) ** 2)))
    return gamma

# Function to generate sine wave data
def generate_sine_wave(x, amplitude, frequency, phase):
    return amplitude * np.sin(2 * np.pi * frequency * x + phase)
amplitude1 = 1.0
frequency1 = 1.0  # Adjust this value to change the speed of the first sine wave
phase1 = 0.0

# Parameters for the second sine wave
amplitude2 = 1.0
frequency2 = 1.0  # Adjust this value to change the speed of the second sine wave
phase2 = 0.0

# Create figure and axis for the first sine wave
fig1, ax1 = plt.subplots()
ax1.set_xlim(0, 2 * np.pi)
ax1.set_ylim(-1.5, 1.5)
line1, = ax1.plot([], [], lw=2, color='blue', label='Time flow on earth')
ax1.legend()

# Create figure and axis for the second sine wave
fig2, ax2 = plt.subplots()
ax2.set_xlim(0, 2 * np.pi)
ax2.set_ylim(-1.5, 1.5)
line2, = ax2.plot([], [], lw=2, color='red', label='Time flow on reference frame')
ax2.legend()

ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])

# Initialization function for the first sine wave
def init1():
    line1.set_data([], [])
    return line1,

# Initialization function for the second sine wave
def init2():
    line2.set_data([], [])
    return line2,

# Animation function for the first sine wave
def animate1(i):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = generate_sine_wave(x, amplitude1, frequency1, phase1 + 0.1 * i)  # Adjust speed here
    line1.set_data(x, y)
    return line1,

# Animation function for the second sine wave
def animate2(i):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = generate_sine_wave(x, amplitude2, frequency2, phase2 + 0.1 * i)  # Adjust speed here
    line2.set_data(x, y)
    return line2,

c = 3e8
v = float(input("Enter velocity of reference frame: "))
gamma = lorentz_factor(c, v)

# Create FuncAnimation objects
ani1 = FuncAnimation(fig1, animate1, init_func=init1, frames=200, interval=50)
ani2 = FuncAnimation(fig2, animate2, init_func=init2, frames=200, interval=50 * gamma) #interval adjusted to show time dilating effect in the animation

# Show the animated plots
plt.show()
