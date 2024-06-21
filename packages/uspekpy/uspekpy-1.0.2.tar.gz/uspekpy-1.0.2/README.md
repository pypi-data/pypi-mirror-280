<h1><img style="float:left;" width="50" height="40" src="assets/letter-u.png" alt="USpekPy icon">USpekPy</h1>

## Radiation protection quantities for x-rays with uncertainties

![Static Badge](https://img.shields.io/badge/Date-Jun_24-teal)
![Static Badge](https://img.shields.io/badge/Version-1.0.2-teal)
![Static Badge](https://img.shields.io/badge/Maintenance-Active-teal)

[![Static Badge](https://img.shields.io/badge/Surce_code-GitHub-blue)](https://github.com/lmri-met/uspekpy)
[![Static Badge](https://img.shields.io/badge/Documentation-README-blue)](https://github.com/lmri-met/uspekpy#README)
[![Static Badge](https://img.shields.io/badge/Contribute-Issues-blue)](https://github.com/lmri-met/uspekpy/issues)
[![Static Badge](https://img.shields.io/badge/Organization-LMRI--Met-blue)](https://github.com/lmri-met/)

[![Static Badge](https://img.shields.io/badge/Distribution-PyPi-orange)](https://pypi.org/project/uspekpy/)
[![Static Badge](https://img.shields.io/badge/License-GPLv3.0-orange)](https://choosealicense.com/licenses/gpl-3.0/)
![Static Badge](https://img.shields.io/badge/Tests-Passing-green)
![Static Badge](https://img.shields.io/badge/CodeCov-65%25-green)

## Table of Contents

- [What is USpekPy?](#what-is-uspekpy)
- [Main features of USpekPy](#main-features)
- [How to install USpekPy?](#installation)
- [Quick user guide](#quick-user-guide)
  - [Units and uncertainties](#units-and-uncertainties)
  - [Compute mean radiation protection quantities](#compute-mean-radiation-protection-quantities)
  - [Compute mean radiation protection quantities with uncertainties](#compute-mean-radiation-protection-quantities-with-uncertainties)
  - [Compute batch simulation for several x-ray spectra](#compute-batch-simulation-for-several-x-ray-spectra)
  - [Data files](#data-files)
- [How to get support?](#how-to-get-support)
- [Documentation](#documentation)
- [Contributors](#contributors)
- [License](#license)
- [Contributing to USpekPy](#contributing-to-uspekpy)

## What is USpekPy?

**USpekPy** is a Python package that allows to compute mean radiation protection quantities 
for a simulated x-ray spectrum with uncertainties using Monte Carlo techniques.
It is an open source, GPLv3-licensed library for the Python programming language.
It is compatible with Python 3.
**USpekPy** is based on the [SpekPy](https://bitbucket.org/spekpy/spekpy_release/src/master/) package, 
which is a Python software toolkit for modelling the x-ray spectra from x-ray tubes.

## Main features of USpekPy 

**USpekPy** provides three features:
- Compute **mean values of radiation protection quantities** of an x-ray spectrum simulated using SpekPy. 
  Specifically, it allows to compute the mean energy, the air kerma and the mean air kerma-to-dose-equivalent 
  conversion coefficient.
- Compute **mean radiation protection quantities** of an x-ray spectrum simulated using SpekPy 
  **with uncertainties** using Monte Carlo techniques.
  Specifically, it allows to compute the first and second half-value layer for aluminium and copper, 
  the mean energy, the air kerma and the mean air kerma-to-dose-equivalent conversion coefficient.
- Perform **batch simulation** to compute the mean values and uncertainties of radiation protection quantities
  for **several x-ray spectra** simulated with SpekPy.

## How to install USpekPy?

**USpekPy** can be installed from the [Python Package Index (PyPI)](https://pypi.org/project/uspekpy/) 
by running the following command from a terminal:

```bash
pip install uspekpy
```

## Quick user guide

### Units and uncertainties

All the uncertainties are standard uncertainties, i.e., with a coverage factor of k = 1.
The units of relative uncertainties are expressed as fraction of one.
The next table shows the units of the quantities used in the package.

| Quantity                                      | Unit  |
|-----------------------------------------------|-------|
| Distance                                      | mm    |
| Voltage                                       | kV    |
| Angle                                         | deg   |
| Energy                                        | keV   |
| Fluence                                       | 1/cm² |
| Mass energy transfer coefficients of air      | cm²/g |
| Air kerma                                     | uGy   |
| Mono-energetic K to H conversion coefficients | Sv/Gy |

### Compute mean radiation protection quantities

This first example shows how to compute the mean values of some radiation protection quantities 
of an x-ray spectrum simulated using SpekPy.
The considered x-ray spectrum is the one corresponding to the radiation quality N-60, 
which is obtained using 60 KeV of peak kilovoltage in the x-ray tube and filters of aluminum (4 mm) and copper (0.6 mm).
The considered operational quantity is ambient dose equivalent, H*(10), 
with a radiation incidence angle of 0º at a distance of 1 m from the x-ray tube.
The tool that **USpekPy** provides to do this is the **SpekWrapper** class.

The next python script shows how to compute the first and second half-value layers for aluminium and copper, 
the mean energy, the air kerma and the mean air kerma-to-dose-equivalent conversion coefficient.

```python
from uspekpy import SpekWrapper

# Define x-ray beam parameters for radiation quality N-60 (filter thickness, peak kilovoltage and anode angle)
my_filters = [
  ('Al', 4),  # mm
  ('Cu', 0.6),  # mm
  ('Sn', 0),  # mm
  ('Pb', 0),  # mm
  ('Be', 0),  # mm
  ('Air', 1000)  # mm
]
my_kvp = 60  # kV
my_th = 10  # deg

# Define path to CSV file containing mass energy transfer coefficients of air in terms of the energy
my_mu_csv = 'data/mu_tr_rho.csv'

# Define path to CSV file containing the monoenergetic air kerma-to-dose-equivalent conversion coefficients for H*(10)
my_hk_csv = 'data/h_k_h_amb_10.csv'

# Initialize an SpeckWrapper object and add filters
spectrum = SpekWrapper(kvp=my_kvp, th=my_th)
spectrum.multi_filter(my_filters)

# Calculate half-value layers for aluminum and copper
hvl1_al = spectrum.get_hvl1()
hvl2_al = spectrum.get_hvl2()
hvl1_cu = spectrum.get_hvl1(matl='Cu')
hvl2_cu = spectrum.get_hvl2(matl='Cu')

# Calculate mean energy
mean_energy = spectrum.get_mean_energy()

# Calculate mean air kerma
mean_kerma = spectrum.get_air_kerma(mass_transfer_coefficients=my_mu_csv)

# Calculate mean air kerma-to-dose-equivalent conversion coefficient for H*(10)
mean_hk = spectrum.get_mean_conversion_coefficient(
  mass_transfer_coefficients=my_mu_csv, conversion_coefficients=my_hk_csv)

# Print results
print(f'First HVL for Al: {hvl1_al} mm')
print(f'Second HVL for Al: {hvl2_al} mm')
print(f'First HVL for Cu: {hvl1_cu} mm')
print(f'Second HVL for Cu: {hvl2_cu} mm')
print(f'Mean energy: {mean_energy} keV')
print(f'Air kerma: {mean_kerma} uGy')
print(f'Mean conversion coefficient for H*(10): {mean_hk} Sv/Gy')
```

The script output is:

```
First HVL for Al: 5.904510251136515 mm
Second HVL for Al: 6.239790098050192 mm
First HVL for Cu: 0.23502729534875702 mm
Second HVL for Cu: 0.2624330033450075 mm
Mean energy: 47.797974735384756 keV
Air kerma: 1.5902735973543143 uGy
Mean conversion coefficient for H*(10): 1.5909359863722154 Sv/Gy
```

### Compute mean radiation protection quantities with uncertainties

This second example shows how to compute the mean values and uncertainties of some radiation protection quantities 
of an x-ray spectrum simulated using SpekPy.
The considered x-ray spectrum is the one corresponding to the radiation quality N-60, 
which is obtained using 60 KeV of peak kilovoltage in the x-ray tube and filters of aluminum (4 mm) and copper (0.6 mm).
The considered operational quantity is ambient dose equivalent, H*(10), 
with a radiation incidence angle of 0º at a distance of 1 m from the x-ray tube.
The tool that **USpekPy** provides to do this is the **USpek** class.

The next python script shows how to compute the first and second half-value layers for aluminium and copper, 
the mean energy, the air kerma and the mean air kerma-to-dose-equivalent conversion coefficient.

```python
from uspekpy import USpek

# Define values and relative uncertainty (k=1) of x-ray beam parameters for radiation quality N-60
# (filter thickness, peak kilovoltage and anode angle)
my_beam = {
    'kVp': (60, 0.01),  # mm, fraction of one
    'th': (20, 0.01),  # mm, fraction of one
    'Al': (4, 0.01),  # mm, fraction of one
    'Cu': (0.6, 0.01),  # mm, fraction of one
    'Sn': (0, 0),  # mm, fraction of one
    'Pb': (0, 0),  # mm, fraction of one
    'Be': (0, 0),  # mm, fraction of one
    'Air': (1000, 0.01)  # mm, fraction of one
}

# Define path to CSV file containing mass energy transfer coefficients of air in terms of the energy
my_mu_csv = 'data/mu_tr_rho.csv'

# Define path to CSV file containing the monoenergetic air kerma-to-dose-equivalent conversion coefficients for H*(10)
my_hk_csv = 'data/h_k_h_amb_10.csv'

# Define relative uncertainty (k=1) of mass energy transfer coefficients of air
my_mu_std = 0.01  # fraction of one

# Initialize a USpekPy object with the defined beam parameters, mass energy transfer coefficients of air
# and monoenergetic air kerma-to-dose-equivalent conversion coefficients for H*(10)
s = USpek(beam_parameters=my_beam, mass_transfer_coefficients=my_mu_csv,
          mass_transfer_coefficients_uncertainty=my_mu_std, conversion_coefficients=my_hk_csv)

# Run simulation with a given number of iterations
df = s.simulate(simulations_number=3)

# Define the path of the output file where the simulation results will be saved
my_output_csv = 'output/output.csv'

# Save results to a CSV file
df.to_csv(my_output_csv, index=True)

# Print results
print(df.to_string())
```

The script **output** is a table containing the randomly sampled values of the beam parameters and 
the computed mean radiation protection quantities of the simulated x-ray spectrum 
for each iteration of the Monte Carlo simulation.
It also contains their mean values and standard uncertainties (k=1).
The **units** are
kV for the peak kilovoltage,
deg for the anode angle,
mm for the filter thickness, air gap and half-value layers, 
keV for the mean energy,
Gy for the air kerma and 
Sv/Gy for the mean air kerma-to-dose-equivalent conversion coefficient.

```
                      #   kVp (kV)   th (deg)    Air (mm)   Al (mm)   Cu (mm)  Sn (mm)  Pb (mm)  Be (mm)  HVL1 Al (mm)  HVL2 Al (mm)  HVL1 Cu (mm)  HVL2 Cu (mm)  Mean energy (keV)  Air kerma (uGy)  Mean conv. coeff. (Sv/Gy)
0           Iteration 1  59.929717  20.070882  996.150291  4.031398  0.591599      0.0      0.0      0.0      5.831812      6.172730      0.230861      0.258297          47.538305         1.599452                   1.585449
1           Iteration 2  59.534814  20.485473  996.406825  4.003680  0.589934      0.0      0.0      0.0      5.781268      6.117909      0.227873      0.254629          47.303424         1.533225                   1.581466
2           Iteration 3  59.596255  19.678848  996.920532  3.935728  0.606411      0.0      0.0      0.0      5.826152      6.157480      0.230388      0.256981          47.453653         1.488258                   1.585720
3                  Mean  59.686929  20.078401  996.492549  3.990269  0.595981      0.0      0.0      0.0      5.813078      6.149373      0.229707      0.256636          47.431794         1.540312                   1.584211
4    Standard deviation   0.173500   0.329346    0.320239  0.040192  0.007406      0.0      0.0      0.0      0.022611      0.023103      0.001311      0.001517           0.097127         0.045670                   0.001945
5  Relative uncertainty   0.002907   0.016403    0.000321  0.010073  0.012427      NaN      NaN      NaN      0.003890      0.003757      0.005708      0.005913           0.002048         0.029650                   0.001228

```

### Compute batch simulation for several x-ray spectra

This third example shows how to perform batch simulation to compute the mean values and uncertainties of 
radiation protection quantities for several x-ray spectra simulated with SpekPy.
The considered x-ray spectrum is the one corresponding to the radiation quality N-60, 
which is obtained using 60 KeV of peak kilovoltage in the x-ray tube and filters of aluminum (4 mm) and copper (0.6 mm).
The considered operational quantity is ambient dose equivalent, H*(10), 
with a radiation incidence angle of 0º at a distance of 1 m from the x-ray tube.
The tool that **USpekPy** provides to do this is the **batch_simulation()** function.

To perform the batch simulation you need and **input file** where the parameters of each simulation are specified.
This can be a CSV file or an Excel file.
- **First column: simulation parameters' names**:
The first column contain the names of the quantities used as simulation parameters.
They are grouped in general parameters (radiation quality, operational quantity, irradiation angle and number of simulations),
value parameters (filters thickness, air gap, peak kilovoltage, anode angle, mass energy transfer coefficients of air and monoenergetic air kerma-to-dose-equivalent conversion coefficients)
and relative uncertainty parameters (filters thickness, air gap, peak kilovoltage, anode angle, mass energy transfer coefficients).
Units of value parameters are specified in the column.
Relative uncertainties are fractional uncertainties, i.e., they are expressed as fractions of one.
The name of the parameters must not be changed, since they are used for data parsing.
- **Next columns: simulation parameters' values**:
The next columns contain the values of the simulation parameters, one column for each simulation case.

The next table shows the content of the input file for this example.

```
                                                                                    Case1                  Case2
General                                                                               NaN                    NaN
Quality                                                                              N-60                   N-60
Operational quantity                                                               H*(10)                 H*(10)
Irradiation angle (deg)                                                                 0                      0
Number of simulations                                                                   3                      3
Values                                                                                NaN                    NaN
Al filter width (mm)                                                                    4                      4
Cu filter width (mm)                                                                  0.6                    0.6
Sn filter width (mm)                                                                    0                      0
Pb filter width (mm)                                                                    0                      0
Be filter width (mm)                                                                    0                      0
Air gap width (mm)                                                                   1000                   1000
Peak kilovoltage (kV)                                                                  60                     60
Anode angle (deg)                                                                      20                     20
Mass energy transfer coefficients of air file (keV and cm²/g)          data/mu_tr_rho.csv     data/mu_tr_rho.csv
Mono-energetic K to H conversion coefficients file (keV and Sv/Gy)  data/h_k_h_amb_10.csv  data/h_k_h_amb_10.csv
Relative uncertainties (k=1)                                                          NaN                    NaN
Al filter width (fraction of one)                                                    0.01                   0.01
Cu filter width (fraction of one)                                                    0.01                   0.01
Sn filter width (fraction of one)                                                       0                      0
Pb filter width (fraction of one)                                                       0                      0
Be filter width (fraction of one)                                                       0                      0
Air gap width (fraction of one)                                                      0.01                   0.01
Peak kilovoltage (fraction of one)                                                   0.01                   0.01
Anode angle (fraction of one)                                                        0.01                   0.01
Mass energy transfer coefficients of air (fraction of one)                           0.01                   0.01               
```

The next python script shows how to compute the first and second half-value layers for aluminium and copper, 
the mean energy, the air kerma and the mean air kerma-to-dose-equivalent conversion coefficient 
for the previous **input file in CSV format**.

```python
from uspekpy import batch_simulation

# Define the path to the input CSV file
my_csv = 'data/input.csv'

# Call the batch_simulation function with the defined input CSV file
df = batch_simulation(input_file_path=my_csv)

# Define the path of the output file where the simulation results will be saved
my_output_csv = 'output/output.csv'

# Save results to a CSV file
df.to_csv(my_output_csv, index=True)

# Print results
print(df.to_string())
```

The next python script shows how to compute the first and second half-value layers for aluminium and copper, 
the mean energy, the air kerma and the mean air kerma-to-dose-equivalent conversion coefficient 
for the previous **input file in Excel format**.

```python
from uspekpy import batch_simulation

# Define the path to the input Excel file
my_excel = 'data/input.xlsx'

# Define the name of the sheet in the input Excel file
my_sheet = 'input'

# Call the batch_simulation function with the defined input Excel file and sheet
df = batch_simulation(input_file_path=my_excel, sheet_name=my_sheet)

# Define the path of the output file where the simulation results will be saved
my_output_csv = 'output/output.csv'

# Save results to a CSV file
df.to_csv(my_output_csv, index=True)

# Print results
print(df.to_string())
```

In both cases, the script **output** is a table in which the simulation results for each case 
are concatenated to the input table.
Simulation results includes the computed mean values and standard uncertainties (k=1) 
for the radiation protection quantities of each simulated x-ray spectrum.
The **units** are
mm for the half-value layers, 
keV for the mean energy,
Gy for the air kerma and 
Sv/Gy for the mean air kerma-to-dose-equivalent conversion coefficient.

```
                                                                                    Case1                  Case2
General                                                                               NaN                    NaN
Quality                                                                              N-60                   N-60
Operational quantity                                                               H*(10)                 H*(10)
Irradiation angle (deg)                                                                 0                      0
Number of simulations                                                                   3                      3
Values                                                                                NaN                    NaN
Al filter width (mm)                                                                    4                      4
Cu filter width (mm)                                                                  0.6                    0.6
Sn filter width (mm)                                                                    0                      0
Pb filter width (mm)                                                                    0                      0
Be filter width (mm)                                                                    0                      0
Air gap width (mm)                                                                   1000                   1000
Peak kilovoltage (kV)                                                                  60                     60
Anode angle (deg)                                                                      20                     20
Mass energy transfer coefficients of air file (keV and cm²/g)          data/mu_tr_rho.csv     data/mu_tr_rho.csv
Mono-energetic K to H conversion coefficients file (keV and Sv/Gy)  data/h_k_h_amb_10.csv  data/h_k_h_amb_10.csv
Relative uncertainties (k=1)                                                          NaN                    NaN
Al filter width (fraction of one)                                                    0.01                   0.01
Cu filter width (fraction of one)                                                    0.01                   0.01
Sn filter width (fraction of one)                                                       0                      0
Pb filter width (fraction of one)                                                       0                      0
Be filter width (fraction of one)                                                       0                      0
Air gap width (fraction of one)                                                      0.01                   0.01
Peak kilovoltage (fraction of one)                                                   0.01                   0.01
Anode angle (fraction of one)                                                        0.01                   0.01
Mass energy transfer coefficients of air (fraction of one)                           0.01                   0.01
Results                                                                              None                   None
HVL1 Al  Mean (mm)                                                               5.895819               5.931133
HVL1 Al  Standard deviation (mm)                                                 0.020477               0.022359
HVL1 Al  Relative uncertainty (fraction of one)                                  0.003473                0.00377
HVL2 Al  Mean (mm)                                                               6.238907               6.275384
HVL2 Al  Standard deviation (mm)                                                 0.017694               0.024303
HVL2 Al  Relative uncertainty (fraction of one)                                  0.002836               0.003873
HVL1 Cu  Mean (mm)                                                               0.234631               0.236732
HVL1 Cu  Standard deviation (mm)                                                  0.00116               0.001351
HVL1 Cu  Relative uncertainty (fraction of one)                                  0.004946               0.005706
HVL2 Cu  Mean (mm)                                                               0.262671               0.265111
HVL2 Cu  Standard deviation (mm)                                                 0.001065               0.001673
HVL2 Cu  Relative uncertainty (fraction of one)                                  0.004053                0.00631
Mean energy  Mean (keV)                                                         47.815274              47.968429
Mean energy  Standard deviation (keV)                                            0.067034               0.104718
Mean energy  Relative uncertainty (fraction of one)                              0.001402               0.002183
Air kerma  Mean (uGy)                                                            1.609083               1.622638
Air kerma  Standard deviation (uGy)                                              0.039089               0.029723
Air kerma  Relative uncertainty (fraction of one)                                0.024293               0.018318
Mean conv. coeff.  Mean (Sv/Gy)                                                  1.589867               1.592054
Mean conv. coeff.  Standard deviation (Sv/Gy)                                    0.001307               0.001274
Mean conv. coeff.  Relative uncertainty (fraction of one)                        0.000822                 0.0008
```

### Data files

For these scripts to work you need to have several data files. 
The content of these files for the previous examples are show below.

CSV file with the **mass energy transfer coefficients** of air in terms of the energy (mu_tr_rho.csv):

```
E (keV),mu_tr/rho (cm^2/g)
1.000000,3487.700000000000000
1.172600,2271.660000000000000
1.250000,1907.850000000000000
1.400000,1396.250000000000000
1.500000,1152.410000000000000
1.750000,746.850000000000000
2.000000,510.495000000000000
2.500000,267.712000000000000
3.000000,156.677000000000000
3.206300,128.597000000000000
3.206301,139.322000000000000
3.223910,139.220000000000000
3.250510,136.749000000000000
3.500000,110.244000000000000
3.618810,99.946700000000000
4.000000,74.386300000000000
5.000000,38.316500000000000
6.000000,22.138700000000000
7.000000,13.863800000000000
8.000000,9.209547628642890
9.000000,6.407464852253970
10.000000,4.626920149961950
12.500000,2.307431530377440
14.000000,1.615050752537630
15.000000,1.301309790375540
17.500000,0.801145676760343
20.000000,0.525990443101652
25.000000,0.262079759969996
28.663300,0.172139443801020
30.000000,0.150643910752649
35.000000,0.096166283094939
40.000000,0.067006659158694
50.000000,0.040350724533314
60.000000,0.030060380204255
70.000000,0.025736225862943
80.000000,0.023919178948042
90.000000,0.023273564441493
100.000000,0.023169137685326
125.000000,0.023905175732908
140.000000,0.024501233602389
150.000000,0.024926643691358
175.000000,0.025877217107796
187.083000,0.026274062287156
200.000000,0.026655131026205
250.000000,0.027882238669658
300.000000,0.028683812435718
324.037000,0.028972447929017
350.000000,0.029148771809045
386.867000,0.029415131704691
400.000000,0.029490249846129
474.342000,0.029698178702551
500.000000,0.029685041261757
574.456000,0.029603764611649
600.000000,0.029549718949812
673.537000,0.029405101930449
700.000000,0.029197657857256
800.000000,0.028890614121642
900.000000,0.028390536220701
1000.000000,0.027936798166738
1250.000000,0.026719405747041
1500.000000,0.025621217869820
1558.930000,0.025359438553807
1750.000000,0.024631087150390
1870.830000,0.024240842040503
2000.000000,0.023753744772526
2345.210000,0.022671649894621
2500.000000,0.022309768351513
3000.000000,0.021132688079239
3240.370000,0.020639133403572
3500.000000,0.020121558259145
4000.000000,0.019347638398287
4500.000000,0.018700741656237
5000.000000,0.018185053120065
6000.000000,0.017326066208925
6480.740000,0.016966042150857
7000.000000,0.016690444038446
8000.000000,0.016199645451199
9000.000000,0.015809252632524
```

CSV file with the **monoenergetic air kerma-to-dose-equivalent conversion coefficients** for H*(10) (h_k_h_amb_10.csv):

```
E (keV),h_k(0 deg) (Sv/Gy)
7,0.000012
8,0.000095
9,0.00145
10,0.008
11,0.0331
12,0.0737
13,0.127
14,0.19
15,0.26
16,0.326
17,0.395
18,0.466
19,0.538
20,0.61
30,1.1
40,1.47
50,1.67
60,1.74
80,1.72
100,1.65
150,1.49
200,1.4
300,1.31
400,1.26
500,1.23
600,1.21
800,1.19
1000,1.17
1500,1.15
2000,1.13
3000,1.12
4000,1.11
5000,1.19
6000,1.09
8000,1.08
10000,1.06
```

Please note that there **must be no zeros or empy-valued energy gaps** in these files, since it will lead to errors in the 
interpolation to the energy values of the x-ray spectrum.

## Future developments

In future versions of USpekPy we would like to make the following enhancements:

- Include the **uncertainty contribution** of the monoenergetic air kerma-to-dose-equivalent conversion coefficients.
- Manage **zeros or empy-valued energy gaps** in data files for mass energy transfer coefficients and monoenergetic 
air kerma-to-dose-equivalent conversion coefficients.
- Expand the **documentation** of the package.

If you have any other suggestions please let us know (please check the 
[Contributing to USpekPy](#contributing-to-uspekpy) section).

## How to get support?

If you need support, please check the **USpekPy** documentation at GitHub
([README](https://github.com/lmri-met/uspekpy/blob/main/README.md)).

If you need further support, please send an e-mail to 
[Paz Avilés](mailto:Paz.Aviles@ciemat.es) or to 
[Xandra Campo](mailto:xandra.campo@ciemat.es).

## Documentation

The official documentation of **USpekPy** is hosted on GitHub.
Check its [README](https://github.com/lmri-met/uspekpy#README) file for a quick start guide.

## Contributors

**USpekPy** is developed and maintained by [Paz Avilés](https://github.com/pazaviles/) and [Xandra Campo](https://github.com/xandratxan/).
It is one of the projects of the [Ionizing Radiation Metrology Laboratory (LMRI)](https://github.com/lmri-met/), 
which is the Spanish National Metrology Institute for ionizing radiation.

## License

**USpekPy** is distributed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/) License.

## Contributing to USpekPy

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
Please check the **USpekPy** [issues page](https://github.com/lmri-met/uspekpy/issues) if you want to contribute.
