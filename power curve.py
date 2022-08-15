

#box 1
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

#box 2
xaxis = "Value of mean"
yaxis = "P(Fail to reject Ho)"

u0 = float(input("Enter (assumed) population mean. "))
u1 = float(input("Enter sample/target mean. "))

unitfinder = ( - (u1 - rangehalf) * 1.5) / 20

yeppers = abs(u0 - u1)

if u0 > u1:
    unitfinder = (u0 - u1) /  20
    test = np.arange(u1 - yeppers, u0 + yeppers, unitfinder)
else:
    unitfinder = (u1 - u0) / 20
    test = np.arange(u0 - yeppers, u1 + yeppers, unitfinder)
	
#box 3
alpha = float(input("Enter alpha level. "))
sampsize = float(input("Enter number of samples. "))
estSD = float(input("Enter the estimted SD. "))
df = sampsize - 1
tppf = abs(stats.t.ppf(alpha,df))

#need to add alpha detail here
#box 4
yvals = []
for val in test:
    a = (stats.t.cdf((u0 + tppf * (estSD / np.sqrt(sampsize)) - val) / (estSD / np.sqrt(sampsize)), df))
    yvals.append(a)

plt.plot(test,yvals)
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.title(f"Sensitivity to Type II Error at Alpha = {alpha}")
plt.show()

#box 5
ok = 1 - np.array(yvals)
thing = pd.DataFrame({xaxis: test,"P(Type II Error)": yvals, "Power": ok})
#thing.columns['xaxis','yaxis']
thing