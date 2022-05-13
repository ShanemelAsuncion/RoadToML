# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plotting using plt
x = [i for i in range(10)]
y = [2*i for i in range(10)]
print('x =',x,' y =',y)

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel("y-axis")
plt.scatter(x,y)

# %%
