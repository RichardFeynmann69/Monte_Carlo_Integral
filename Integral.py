import random
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import configparser


config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

def f(x):
    value_string= config["EQ"]["value"]
    value= eval(value_string)
    return value

up_limit = float(config["EQ"]["up_limit"])
low_limit = float(config["EQ"]["low_limit"])

bounds = [(low_limit, up_limit)]
result = minimize(lambda x: -f(x), x0=0, bounds=bounds)

if result.success:
    max_x = result.x
    max_y = -result.fun  # Restore the original sign

else:
    print("Failed to find the maximum.")

iteration = 100000
under = 0
for i in range(iteration):
    random_numberx = random.uniform(low_limit,up_limit)
    fun_value = f(random_numberx)
    under += fun_value

field = (up_limit-low_limit)*(under/iteration)
field_round=round(field,3)
file = open("Output.txt", "w")
file.write(f"Field under the function: {field_round}")
file.close()  

plt.style.use('_mpl-gallery')

# make data
x_plot = np.linspace(low_limit, up_limit, 100)
y = f(x_plot)

# plot
fig, ax = plt.subplots()

ax.plot(x_plot, y, linewidth=2.0)

ax.set(xlim=(low_limit, up_limit), xticks=np.arange(low_limit, up_limit),
       ylim=(0, max_x), yticks=np.arange(0, 5))

plt.fill_between(x_plot, y1=f(x_plot) ,color= "b", alpha= 0.2)

plt.savefig("Output.pdf",format="pdf",bbox_inches="tight")

