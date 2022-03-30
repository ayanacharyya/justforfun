#Gaussian fitting code

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import exp
from scipy.special import erf
from scipy.optimize import curve_fit
from lmfit.models import SkewedGaussianModel, ConstantModel

#------symmetric gaussian function (normalised)---------
def gaus_sym(x, *p):
    return p[0] + (p[1]/(p[3] * np.sqrt(2*np.pi))) * exp(-((x - p[2]) ** 2) / (2 * p[3] ** 2))

#------cumulative i.e. integration of symmetric gaussian function---------
def cdf(x, *p):
    return p[0] + 0.5 * (1 + erf((x-p[2])/(np.sqrt(2)*p[3])))

#------symmetric gaussian function---------
def gaus_asym(x, *p):
    return p[0] + 2 * (gaus_sym(x, *p[:-1]) - p[0]) * (cdf(p[4] * x, *p[:-1]) - p[0])

# ---------------------read the data----------------------
workdir = '/Users/acharyya/Downloads/'
plotname = workdir + 'gausfit.pdf'
data = pd.read_table(workdir + 'x&y.txt', delim_whitespace=True)
x, y = data['x'].values, data['y'].values
p_init = [0, 1e7, 1e5, 1e4, 1] # initial guesses for continuum, amplitude, centroid, sigma and skewness

# -----------plot data------------------
plt.close('all')
fig = plt.figure()
xarr = np.linspace(np.min(x), np.max(x), 100)
plt.plot(x, y, c='k', label='data', lw=2) # data

# ------------------symmetric fitting---------------------
popt_sym, pcov_sym = curve_fit(gaus_sym, x, y, p0=p_init[:-1])
plt.plot(xarr, gaus_sym(xarr, *popt_sym), c='r', label='Symmetric gaussian', lw=2) # symmetric fit
rms = np.sqrt(np.mean((y - gaus_sym(x, *popt_sym))**2))
print 'Symmetric gaussian fit parameters', popt_sym, 'RMS=', rms

# ------------------asymmetric fitting with self defined functions--------------------
popt_asym, pcov_asym = curve_fit(gaus_asym, x, y, p0=p_init, maxfev=5000)
plt.plot(xarr, gaus_asym(xarr, *popt_asym), c='b', label='Asymmetric gaussian self', lw=2, ls='dashed') # asymmetric fit
rms = np.sqrt(np.mean((y - gaus_asym(x, *popt_asym))**2))
print 'Asymmetric gaussian fit parameters (self defined)', popt_asym, 'RMS=', rms

# ------------------asymmetric fitting with SGM--------------------
gaus_model = SkewedGaussianModel()
cont_model = ConstantModel()
params = cont_model.make_params(c=p_init[0]) + gaus_model.make_params(amplitude=p_init[1], center=p_init[2], sigma=p_init[3], gamma=p_init[4])
model = cont_model + gaus_model
result = model.fit(y, params, x=x)
plt.plot(x, result.best_fit, c='g', label='Assymetric gaussian SGM', lw=2) # asymmetric fit
rms = np.sqrt(np.mean((y - result.best_fit)**2))
print 'Asymmetric gaussian fit parameters (with SGM)', [result.params[quantity].value for quantity in ['c', 'amplitude', 'center', 'sigma', 'gamma']], 'RMS=', rms

# ----------tidying and saving plot----------------------
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
fig.savefig(plotname)
print 'Plot saved as', plotname
plt.show(block=False)

# ------------print disclaimer-----------
print 'Choose the fitted parameters from the best fit (i.e. fit that has lowest RMS value).'
print 'Done!'