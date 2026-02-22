import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
import os
import sys

# 0.2 Parameter Kurve abschalten
plot1_Mauna_Loa_ = 1 # 2 print in line 2, 0 keine Kurve 1 Mauna Loa 4 save png
c1 = "blue" # plot1 color
Kurve2_population_on = 0 # 5 3, 4, 5 0 row 5 # 0=no print , 1 = Bevölkerung in grün
plot3_delta_CO2_red_bars = 0 # 3 4 0 7 8 keine delta_CO2 , 1 = delta_CO2 in rot , 7,8 mit Beschriftung   
plot4_CO2_orange2025 = 0 # 3, 4, 0 orange Glen , 1 = 0.013t² - 51t + 49,536 in rot 3 works plot4_CO2_orange2025
Kurve5_Glen_delta_on = 0 # 3, 4, 0 print row 4 # green Glen diff print in line 4
plot6_Glen_CO2_on = 3 # 3 print in line 3, 0 keine Kurve Glen , 1 = 0.013t² - 51t + 49,536 in rot  
c6 = "purple" # plot6 color
plot7_temperature = 4 # 4, 0
c7 = "red" # plot7 color
parameter8_save_png = 8 # save png

# 0.3.1 scale the left Y axis
y_min = 300 # min value 280
y_max = 700 # min value 440 70

# 0.3.2 scale the right Y axis
y_Tmin = 0 # min value °C
y_Tmax = 8 # 40 # max value C

x_anf = 1980 # 1960 geht, 2000 geht
x_end = 2100 # 2026 geht

ydiff = (y_max - y_min) / 10 # for y axis scale print
xdiff = (x_end - x_anf) / 10 # for legend print

scale_mode = 10 # 0 7 8 10 hansen 10
# -----------------------------
# 0.4 Plot (x-width, y-width) Size of the figure in inches 
# -----------------------------
y_grid_CO2 = 10
if scale_mode == 7:
   fig, ax1 = plt.subplots(figsize=(13, 7))
elif scale_mode == 8:
   fig, ax1 = plt.subplots(figsize=(13, 8))
elif scale_mode == 10:
   fig, ax1 = plt.subplots(figsize=(13, 10))
   y_grid_CO2 = 50
else:
   fig, ax1 = plt.subplots(figsize=(13, 7))


# 0.4 scale the text rows below the plot field
tr1x = -0.09 # text row 1 x value -.3...1 -0.12
tr1y = -.16 # text row 1 y end value -.3...1 -.15
tr2x = 0.01 # text row 2 x value -.3...1 -0.08
tr2y = -.24 # text row 2 y end value -.3...1 -.24

# 0.5 scale the text rows below the plot field
tr3y = -.32 # text row 1 y end value -.3...1 -.32
tr4y = -.40 # text row 1 y end value -.3...1 -.40
tr5y = -.48 # text row 1 y end value -.3...1 -.48
tr6y = -.56 # text row 1 y end value -.3...1 -.56
trs = 20 # trs = 16 # fontsize=14

# 0.6 scale the legend lines below the plot field
lr2x1 = 0.065 # line row 2 x value begin 0.065
lr2x2 = 0.085 # line row 2 x value end 0.085
lr2y = 0.215 # line row 2 y value begin 0.215
lr3y = 0.17 # line row 3 y value begin 0.17
lr4y = 0.124 # line row 4 y value begin 0.124
lr5y = 0.078 # line row 5 y value begin 0.08

# 0.7 scale the right y axis
yr0=ydiff/8
yr0 = int(yr0+0.49) # cast to integer result = 2 (int)
yr1=ydiff-yr0
yr1 = int(yr1+0.49) # cast to integer result = 2 (int)




# 0.8 Parameter strig
header_parameter = f"{plot1_Mauna_Loa_}" # 1960 number inside string
header_parameter = header_parameter + f"{Kurve2_population_on}" # Kurve2_population_on number inside string
header_parameter = header_parameter + f"{plot3_delta_CO2_red_bars} " # plot3_delta_CO2_red_bars number inside string
header_parameter = header_parameter + f"{plot4_CO2_orange2025}" # plot4_CO2_orange2025 number inside string
header_parameter = header_parameter + f"{Kurve5_Glen_delta_on}" # Kurve5_Glen_delta_on number inside string
header_parameter = header_parameter + f"{plot6_Glen_CO2_on} " # Kurve2_population_on number inside string
header_parameter = header_parameter + f"{plot7_temperature}" 
header_parameter = header_parameter + f"{parameter8_save_png} " 
# header_parameter = f" parameter= {plot1_Mauna_Loa_}" # 1960 number inside string
# -----------------------------
# 1.1 Kurve1 Jahre 1960–2025
# -----------------------------

jahre1 = list(range(1960, x_end))

# Select only 2018–2025
start = jahre1.index(x_anf)
end = jahre1.index(2025) + 1
jahre1_subset = jahre1[start:end]

# -----------------------------
# 1.2 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# https://gml.noaa.gov/ccgg/trends/mlo.html
# https://gml.noaa.gov/ccgg/trends/global.html
# -----------------------------
co2_values1 = [
316.91, 317.64, 318.45, 318.99, 319.62, 320.04, 321.38, 322.16, 323.04, 324.62, # 1960–1969
325.68, 326.32, 327.46, 329.68, 330.19, 331.13, 332.03, 333.84, 335.41, 336.84, # 1970–1979
338.76, 340.12, 341.48, 343.15, 344.87, 346.35, 347.61, 349.31, 351.69, 353.20, # 1980–1989
354.45, 355.70, 356.54, 357.21, 358.96, 360.97, 362.74, 363.88, 366.84, 368.54, # 1990–1999
369.71, 371.32, 373.45, 375.98, 377.70, 379.98, 382.09, 384.02, 385.83, 387.64, # 2000–2009
390.10, 391.85, 394.06, 396.74, 398.81, 401.01, 404.41, 406.76, 408.72, 411.66, # 2010–2019
414.24, # 2020
416.41, # 2021
418.53, # 2022
421.08, # 2023 421.08
424.61, # 2024
428.26 # 2025 = 424.61 + 3.69 ppm
]

# 1.2 Kurve1 CO₂ Daten https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_clobal.txt
# 1.2.2 world data not found
# https://gml.noaa.gov/ccgg/trends/global.html

# 1.3 subset skip the old years
co2_values1_subset = co2_values1[start:end]
df = pd.DataFrame({
"Jahr": jahre1_subset,
"CO2": co2_values1_subset
})


# 1.5 add more space below plot
fig.subplots_adjust(bottom=0.30) # 0.25 = 25% margin at bottom

# fig.text(0.5, 0.05, "This is extra text below the figure",
# ha="center", va="center", fontsize=12, color="gray")
# 1.6 Legende oben links
#ax1.plot(df["Jahr"], df["CO2"], marker="o", markersize=5, color="blue", linewidth=2, label="Mauna Loa CO₂ in ppm 2025 = 424.61 + 3.69 ppm K1")
# 1.7 print blue Mauna Loa

ax1.plot(df["Jahr"], df["CO2"], marker="o", markersize=5, color="blue", linewidth=2, label=" ")
ax1.set_xlabel("year", fontsize=16 )
plt.xticks(fontsize=16)

# 1.7.2 write "CO₂ in ppm" left Axis upwards
ax1.set_ylabel("CO₂ in ppm", color=c1, fontsize=20) # y achse links

# 1.7.4 write the numbers left of plot field
ax1.tick_params(axis="y", labelcolor=c1, labelsize=20) # Achsenbeschriftung
ax1.grid(True)

# 1.8 scale the Y value 280 ppm to 440 ppm y_grid_CO2 = 20
if scale_mode == 10:
   ax1.set_ylim(y_min, y_max)
   ax1.yaxis.set_major_locator(MultipleLocator(y_grid_CO2))   # Hauptstriche
   ax1.yaxis.set_minor_locator(MultipleLocator(10))   # Nebenstriche
   ax1.tick_params(axis='y', which='major', length=12, width=1.5)
   ax1.tick_params(axis='y', which='minor', length=6,  width=1, color='blue')
   # 1.8 scale the X value time = 20
   ax1.xaxis.set_major_locator(MultipleLocator(20))   # Hauptstriche
   ax1.tick_params(axis='x', which='major', length=12, width=2)
   ax1.xaxis.set_minor_locator(MultipleLocator(2))   # Nebenstriche
   ax1.tick_params(axis='x', which='minor', length=4,  width=1)
   ax1.grid(True, which="major") # grosses Netz 20 ppm
   ax1.grid(True, which="minor", alpha=0.20) # Netz 
   y_block = (y_max - y_min) / y_grid_CO2  # 120 / 20 = 6 y_block
else:
  ax1.set_ylim(y_min, y_max)

# ------Kurve 2-----------------------
# 2.1 Weltbevölkerung laden (UN WPP 2024 via OWID)
# url = "https://ourworldindata.org/grapher/population.csv"
# -----------------------------

if Kurve2_population_on > 0:
   pop_df = pd.read_csv("population4.csv")
   pop_world = (
         pop_df[pop_df["Entity"] == "World"][["Year", "Population"]]
         .query("1960 <= Year <= 2026")
         .sort_values("Year")
         .reset_index(drop=True)
      )
   pop_world_subset = pop_world[start:end]
   # 2.3 in Milliarden
   pop_world["Population_Mrd"] = pop_world["Population"] / 1e9
   #end Kurve2_population_on=1 - print population

# 2.3 Kurve2_population_on=1
if Kurve2_population_on > 0:
   ax2 = ax1.twinx()
   ax2.spines.right.set_position(("outward", 50))
   ax2.set_ylabel("Earth Population in Billion", color="green")
   # 2.5 Legende oben links
   ax2.plot(pop_world["Year"], pop_world["Population_Mrd"], marker="s", color="green", label="Earth Population in Billion K2")
   ax2.set_ylabel("Earth Population in Billion", color="green")
   ax2.tick_params(axis="y", labelcolor="green")
   ax2.set_ylim(1, 9) #8
   #end print_y2=1 - print population

if Kurve2_population_on == 2: ax2.set_ylim(6.5, 8.5) # andere Skala
#end Kurve2_population_on=1 - print population

# 2.4 Kurve2_population_on=1

# -----Kurve 3------------------------
# 3.1 ΔCO₂ berechnen (per pandas) Balken
# df["CO2"].diff() Calculates the difference between consecutive CO₂ values
# -----------------------------

if plot3_delta_CO2_red_bars > 0:
   df["Delta_CO2"] = df["CO2"].diff().fillna(0)  # This line creates a new column in your DataFrame called Delta_CO2.
   ax3 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax3.spines.right.set_position(("outward", 20))

if plot3_delta_CO2_red_bars > 0:
   bars = ax3.bar(df["Jahr"], df["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax3.bar(df["Jahr"], df["Delta_CO2"], width=0.7, alpha=0.5, color="red")
   ax3.set_ylabel("red bars Mauna Loa CO2 increase in ppm", color="red", fontname="Arial",fontsize=16) # fontweight="bold"
   ax3.tick_params(axis="y", labelcolor="red", labelsize=16)
   ax3.set_ylim(-yr0, yr1) # scale y axis3 right red
   #ax3.set_ylim(-2, 14)

# 3.5 Add numbers on top of delta CO2 bars
if plot3_delta_CO2_red_bars > 6:
   ax3.bar_label(bars, fontsize=8, fontname="Arial",padding=1, color="black")

# 4 part 4
# 4.1 Kurve4 -- 2. Quadratic model function
def co2_model4(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7

# 4.2 Kurve4 . Real Mauna Loa CO₂ annual data 1960–2023
# 2025 = 424.61 + 3.69 ppm = 428.26
data4 = {
1960: 316.91, 1961: 317.64, 1962: 318.45, 1963: 318.99, 1964: 319.62,
1965: 320.04, 1966: 321.37, 1967: 322.18, 1968: 323.05, 1969: 324.62,
1970: 325.68, 1971: 326.32, 1972: 327.46, 1973: 329.68, 1974: 330.19,
1975: 331.12, 1976: 332.03, 1977: 333.84, 1978: 335.41, 1979: 336.84,
1980: 338.76, 1981: 340.12, 1982: 341.48, 1983: 343.15, 1984: 344.85,
1985: 346.35, 1986: 347.61, 1987: 349.31, 1988: 351.69, 1989: 353.20,
1990: 354.45, 1991: 355.70, 1992: 356.54, 1993: 357.21, 1994: 358.96,
1995: 360.97, 1996: 362.74, 1997: 363.88, 1998: 366.84, 1999: 368.54,
2000: 369.71, 2001: 371.32, 2002: 373.45, 2003: 375.98, 2004: 377.70,
2005: 379.98, 2006: 382.09, 2007: 384.02, 2008: 385.83, 2009: 387.64,
2010: 390.10, 2011: 391.85, 2012: 394.06, 2013: 396.74, 2014: 398.87,
2015: 401.01, 2016: 404.41, 2017: 406.76, 2018: 408.72, 2019: 411.66, # 2025 = 424.61 + 3.69 ppm
2020: 414.24, 2021: 417.41, 2022: 418.52, 2023: 421.24, 2024: 424.61 , 2025: 428.26
}
years4 = np.array(list(data4.keys()))

# 4.3
co2_actual4 = np.array(list(data4.values()))
co2_modeled4 = co2_model4(years4)

# 4.3. Calculate difference (actual minus model)
difference4 = co2_actual4 - co2_modeled4

# -- 4.4. Create DataFrame for convenience
df4 = pd.DataFrame({
"Year": years4,
"Actual": co2_actual4,
"Modeled": co2_modeled4,
"Difference": difference4
})

# 4.6
if plot4_CO2_orange2025 > 0:
   ax4 = ax1.twinx()
   ax4.tick_params(labelright=False) # removes the right-side numbers
   ax4.set_ylabel("") # removes the axis label

# 4.5 Legende oben links
if plot4_CO2_orange2025 > 0:
   ax4.plot(df4["Year"], df4["Modeled"], '--', label="Glen *parabola* ( 0.0132t² - 51t + 49,536) K4", color="orange", linewidth=3)
   ax4.set_ylim(y_min, y_max) # scale glen curve same as Mauna loa
   ax4.spines.right.set_position(("outward", 90))

# 5 part 5 difference Mauna Loa minus Glen_CO2
# 5.4 print y axis 5 on right side Twin axis for difference
if Kurve5_Glen_delta_on > 0:
   ax5 = ax1.twinx()
   ax5.bar(df4["Year"], df4["Difference"], color="green", alpha=0.4, label="Diff (Actual − Model)")
   ax5.set_ylabel("5 Difference Mauna Loa - Glen-parabol (ppm)", color="green", fontsize=14)
   ax5.tick_params(axis="y", labelcolor="green")
   #ax5.set_ylim(-1, 13) # scale
   # ydiff=16
   ax5.set_ylim(-yr0, yr1) # scale

# -----------------------------
# 6.1 Kurve6 Jahre 1960–3025
# -----------------------------
# CO₂ Funktion
def co6_ppm(t):
   return 0.0132251 * t**2 - 51.0337 * t + 49536.7

# 6.2 Jahre von 1960 bis 3000
years6 = np.arange(x_anf, x_end +1 )
co6_values = co6_ppm(years6)

# -- 6.4. Create DataFrame for convenience
df6 = pd.DataFrame({
"Year6": years6,
"Modeled6": co6_values
})

if plot6_Glen_CO2_on > 0:
   ax6 = ax1.twinx()
   ax6.spines.right.set_position(("outward", 90))
   ax6.spines["right"].set_visible(False) # remove right y-Achse
   ax6.tick_params(right=False, labelright=False) # remove Zahlen

if plot6_Glen_CO2_on > 0:
   ax6.plot(df6["Year6"], df6["Modeled6"], '--', label="Glen formula CO2= 0.0132t² - 51t + 49,536 K6", color=c6, linewidth=3)
   ax6.tick_params(axis="y", labelcolor="green")
   ax6.set_ylim(y_min, y_max) # scale
   ax6.spines.right.set_position(("outward", 60))

# 7 part 1
# 7.1 plot7_temperature @reescatophuls.bsky.social
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
# (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
def T_model7(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123

# 7.1.2 years scale x axis
years7 = np.arange(x_anf, x_end + 1 )
T_values = T_model7(years7)

# -- 7.1.4. Create DataFrame for convenience
df7 = pd.DataFrame({
"Year7": years7,
"Modeled7": T_values
})

# 7.1.6 plot7_temperature
if plot7_temperature > 0:
   ax7 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax7.plot(df7["Year7"], df7["Modeled7"], '--', label="T formula CO2=  K6", color=c7, linewidth=3)
   ax7.tick_params(axis="y", labelcolor=c7)
   ax7.set_ylim(y_Tmin, y_Tmax) # scale
   Tax1 = 1 # 0.1))   # Hauptstriche
   Tax2 = 0.2 # 0.1))   # Nebenstriche
   ax7.yaxis.set_major_locator(MultipleLocator(Tax1))   # Hauptstriche
   ax7.yaxis.set_minor_locator(MultipleLocator(Tax2))   # Nebenstriche
   ax7.set_ylim(y_Tmin, 3 ) # scale
  
# 7.1.7 plot7 Achse und Beschriftung
if plot7_temperature > 0:
   #ax7 = ax1.twinx()  # twinx(): Shares the same x-axis Adds a new y-axis on the right
   ax7.spines.right.set_position(("outward", 5))
   # ax7.spines["right"].set_visible(False) # remove right y-Achse
   ax7.set_ylabel("Δ Temperature in °C", color=c7, fontname="Arial",fontsize=20) # fontweight="bold"
   ax7.tick_params(axis="y", labelcolor=c7, labelsize=20)



# 7.1.8 plot7_temperature
if plot7_temperature > 0:
   ax7.set_ylim(y_Tmin, y_Tmax) # scale
   # ax7.axhline(1.5, color="red", linestyle="--", linewidth=1.5, alpha=0.7)
   # ax7.axhline(2, color="grey", linestyle="--", linewidth=1.5, alpha=0.7)
   ax7.axhspan(1.5, 2.0, color="#B3D9FF", alpha=0.25, zorder=0) # color="lightblue" 2°C streifen
   ax7.axvspan(2024, 2026, color="#B3D9FF", alpha=0.25, zorder=0) # vertical bar'

"""
# Load the annual GISTEMP data
url = "https://datahub.io/core/global-temp/r/annual.csv"
df = pd.read_csv(url)

# Inspect the first rows
print(df.head())

# Plot
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Mean"], marker="o")
plt.title("Global Annual Temperature Anomalies (GISTEMP)")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid(True)
plt.show()
"""
# 4.x KurveX – Global annual temperature anomaly (°C, relative to baseline)
dataT = {
1880: -0.16, 1881: -0.08, 1882: -0.10, 1883: -0.17, 1884: -0.28,
1885: -0.33, 1886: -0.31, 1887: -0.36, 1888: -0.18, 1889: -0.11,
1890: -0.35, 1891: -0.22, 1892: -0.27, 1893: -0.31, 1894: -0.30,
1895: -0.23, 1896: -0.11, 1897: -0.11, 1898: -0.27, 1899: -0.17,
1900: -0.09,
# …
2000:  0.42, 2001:  0.54, 2002:  0.63, 2003:  0.62, 2004:  0.54,
2005:  0.67, 2006:  0.63, 2007:  0.66, 2008:  0.54, 2009:  0.64,
2010:  0.71, 2011:  0.59, 2012:  0.63, 2013:  0.66, 2014:  0.74,
2015:  0.87, 2016:  1.00, 2017:  0.92, 2018:  0.85, 2019:  0.98,
2020:  1.02, 2021:  0.85, 2022:  0.89, 2023:  1.18
}
yearsT = np.array(list(dataT.keys()))
tempsT = np.array(list(dataT.values()))



# Telil 8.1 plot
plt.xlim(x_anf, x_end)

# 8.2 headline part print ablove the plot aerea
# 8.2.1 blue headline part
trs = 20
# header_black = f"CO2 concentration in the atmosphere {x_anf}" # 1960 number inside string
if plot7_temperature > 0: # one temperature active
   # 8.2.3 plot the headline
   # plt.text(-0.1, 1.05, header, color="blue", fontname="Arial", fontsize=18, transform=plt.gca().transAxes)
   plt.text(-0.1, 1.05,
     f"{x_anf}   CO2 Mauna Loa",    # f"More CO2 in atmosphere", 
     color="blue", fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.24, 1.05,
     f"- - CO2 quadratic",
     color=c6, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
   plt.text(0.48, 1.05,
     f"--> Δ Temperature calculated °C year 2100",
     color=c7, fontname="Arial", fontsize=trs, transform=plt.gca().transAxes )
else:   
   header = f"CO2 measured at Mauna Loa up to 2024. Print {x_anf}" # 1960 number inside string
   header = header + f" to {x_end} " # 2026 number inside string
   # 8.3.3 plot the headline
   plt.text(-0.1, 1.05, header, color="black", fontname="Arial", fontsize=18,
            transform=plt.gca().transAxes)
            
#  Interpret the x and y coordinates in axis-relative units, not data values.
# transform=plt.gca().transAxes) # x = 0 → left edge of the plot  x = 1 → right edge of the plot


# 8.4 legende Mauna Loa blau plot1_Mauna_Loa_
if plot1_Mauna_Loa_ > 6: # 8.5.1 legende world data plot1_Mauna_Loa_
   K1_text=" Blue: CO2 measured at Mauna Loa ( 2025 = 424.61ppm + 3.69 ppm )"
   plt.text(0.02, 0.95, K1_text, color="blue", fontname="Arial", fontsize=16,
   transform=plt.gca().transAxes)
   ax1.plot([x_anf+1, x_anf +2], [y_max -5, y_max -5], marker="o", markersize=5, color="blue", linewidth=2, label="short line")
# 8.5 Kurve2_population_on = 1 # 0 keine Bevölkerung , 1 = Bevölkerung in grün
if plot1_Mauna_Loa_ > 8:
   if Kurve2_population_on > 0:
      plt.text(0.02, 0.90,"green: Human Population in billion K2", color="green", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
# 8.6 legende
if plot1_Mauna_Loa_ > 8:
   if plot3_delta_CO2_red_bars > 0:
      plt.text(0.02, 0.86," red bars: Mauna Loa yearly increase. //see right larger ppm scaling", color="red", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -21, y_max -21], marker="_", markersize=5, color="red", linewidth=8)
# 8.7 legende '--', label="Glen *parabola* ( 0.0132t² - 51t + 49,536) K4", color="orange", linewidth=3)
if plot1_Mauna_Loa_ > 8:
   if plot4_CO2_orange2025 > 0:
      plt.text(0.02, 0.80," orange: Glen formula ppm = 0.0132 t² - 51 t + 49,536 ", color="orange", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -30.5, y_max -30.5], marker="_", markersize=5, color="orange", linewidth=3)
# 8.8 legend in the plot
if plot1_Mauna_Loa_ > 8:
   if Kurve5_Glen_delta_on > 0:
      plt.text(0.02, 0.29," green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling", color="green", fontname="Arial", fontsize=14,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -52, y_max -52], marker="_", markersize=5, color="green", linewidth=8)
# 8.9 legend in the plot
if plot1_Mauna_Loa_ > 8:
   if plot6_Glen_CO2_on > 0:
      plt.text(0.02, 0.85," Red: Glen formula ppm = 0.0132251t² - 51.0337t + 49,536", color="red", fontname="Arial", fontsize=16,
      transform=plt.gca().transAxes)
      ax1.plot([x_anf+1, x_anf +2], [y_max -12, y_max -12], marker="_", markersize=5, color="red", linewidth=3)


# 9 part 9 print information below the plot field
# 9 part 9 print information below the plot field
trs = 20
# 9 part 9 print information below the plot field
# 9.1 print line 1 the text below the figure tr1x = -0.09 # tr1y = -.16 
filename = os.path.basename(sys.argv[0])
text_below1 = ""
# text_below1 = text_below1 + header_parameter
text_below1 = text_below1 + "Figure from "
text_below1 = text_below1 + filename
plt.text(-0.1, tr1y, text_below1, color="black", fontname="Arial", fontsize=trs,
         transform=plt.gca().transAxes)

# 9.2 print line 1 blue Mauna Loa data below the figure
# 9.2 print line 2 below the plot explainations
if plot1_Mauna_Loa_ == 3: # 8.5.1 legende world data plot1_Mauna_Loa_
   K1_text=" 2 new text )"
   plt.text(tr2x, tr2y, K1_text, color="blue", fontname="Arial", fontsize=18,
   transform=plt.gca().transAxes)
   # elif plot1_Mauna_Loa_ == 1:
else: # 9.2.2 draw bue line as legend
   line1 = Line2D([lr2x1, lr2x2], [lr2y, lr2y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="o", markersize=5, color="blue", linewidth=2)
# 9.2.3 draw bue line as legend
fig.add_artist(line1)
# 9.2.4 write blue text
blue_text="Blue line: CO2 measured at Mauna Loa ( 2025 = 424.61ppm + 3.69 ppm )"
# 9.2.5 plot the blue text
plt.text(tr2x, tr2y, blue_text, color="blue", fontname="Arial", fontsize=trs,
transform=plt.gca().transAxes)

# 9.3 print line 3 below the plot explainations
# 9.3.2 print line 3 Kurve2_population_on marker="s"
if Kurve2_population_on == 3: # 8.5.1 legende world data plot1_Mauna_Loa_
   line1 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line1)
   # 9.5.4 write blue text
   blue_text="Green line: Earth Population in billion"
   # 9.5.5 plot the blue text
   plt.text(tr2x, tr3y, blue_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.3 print line 3 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif plot3_delta_CO2_red_bars == 3 or plot3_delta_CO2_red_bars == 7:
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write red text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling"
   # 9.2.5 plot the red text
   plt.text(tr2x, tr3y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.3.4 work_ print line 3 orange Glen data below the figure
elif plot4_CO2_orange2025 == 3: # print in line 3 up to 2025
   line3 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line3)
   # 9.2.4 write blue text
   red_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr3y, red_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
# 9.3.5  print line 3 green Glen 
elif Kurve5_Glen_delta_on == 3: # print in line4
   line4 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.3.5 draw bue line as legend
   fig.add_artist(line4)
   # 9.3.5 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.3.5 plot the green text
   plt.text(tr2x, tr3y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3.6_ print line 3 red Glen data below the figure
# 9.3.6  print line 6 red Glen 
if plot6_Glen_CO2_on == 3: # print in line 3
   line6 = Line2D([lr2x1, lr2x2], [lr3y, lr3y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c6, linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line6)
   # 9.2.4 write blue text
   red_text="purple dashed @gergyl.bsky atmosphere ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr3y, red_text, color=c6, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.3 end print line 3 below the plot explainations


# 9.4 print line 4 below the plot explainations
# 9.4 print line 4 below the plot explainations
# 9.4.2 print line 4 Kurve2_population_on marker="s"
if Kurve2_population_on == 4:
   line1 = Line2D([lr2x1, lr2x2], [lr4y, lr4y],
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   fig.add_artist(line1)
   blue_text="Green line: Earth Population in billion"
   plt.text(tr2x, tr4y, blue_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # 9.4.3 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
if plot3_delta_CO2_red_bars == 4 or plot3_delta_CO2_red_bars == 8:
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="_", markersize=5, color="red", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   text4="red bars: Mauna Loa yearly CO2 increase //see right larger ppm scaling"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, text4, color="red", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.4 work_ print line 4 orange Glen data below the figure
if plot4_CO2_orange2025 == 4: # print in line 3 up to 2025
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color="orange", linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   red_text="Orange dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red_text, color="orange", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.5 print line 4 green Glen data below the figure marker="_", markersize=5, color="green", linewidth=8)
elif Kurve5_Glen_delta_on == 4: # print in line4
   line5 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1 lr3y
   transform=fig.transFigure,
   marker="_", markersize=5, color="green", linewidth=8)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line5)
   # 9.2.4 write blue text
   green_text="Green bars: Difference Mauna Loa - Glen quadratic t² //see right larger ppm scaling"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, green_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.4.6_ print line 3 red Glen data below the figure
elif plot6_Glen_CO2_on == 4: # print in line 3
   line4 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c6, linewidth=2)
   # 9.2.3 draw bue line as legend
   fig.add_artist(line4)
   # 9.2.4 write blue text
   red_text=" dashed line: Glen parabol formula ppm = 0.0132251t² - 51.0337t + 49,536"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red_text, color=c6, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
elif plot7_temperature == 4:
   line7 = Line2D([lr2x1, lr2x2], [lr4y, lr4y], # y from 0 to 1
   transform=fig.transFigure,
   marker="o", markersize=3, color=c7, linewidth=2)
   # 9.4.7 draw bue line as legend
   fig.add_artist(line7)
   # 9.4.7 write  text  0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
   red_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
   # 9.2.5 plot the blue text
   plt.text(tr2x, tr4y, red_text, color=c7, fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)


# 9.5.2 print line 5 Kurve2_population_on marker="s"
if Kurve2_population_on == 5: # 8.5.1 legende world data plot1_Mauna_Loa_
   line1 = Line2D([lr2x1, lr2x2], [lr5y, lr5y], # x coords in figure space (0–1)
   transform=fig.transFigure,
   marker="s", markersize=5, color="green", linewidth=2)
   # 9.5.2 draw bue line as legend
   fig.add_artist(line1)
   # 9.5.4 write blue text
   blue_text="Green line: Earth Population in billion"
   # 9.5.5 plot the blue text
   plt.text(tr2x, tr5y, blue_text, color="green", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
   # elif plot1_Mauna_Loa_ == 1:
else: # 9.2.2 draw bue line as legend
   plt.text(tr2x, tr5y, "Line 5 -0.48", color="white", fontname="Arial", fontsize=trs,
   transform=plt.gca().transAxes)
# 9.5 print line 5 Kurve2_population_on
# 9.6 print line 6

header_black = " CO2 in ppm  Parameter="
header_black = header_black + header_parameter

# plt.text(0.6, 1.08, header_black, color="black", fontname="Arial", fontsize=14,
text6 = f" y_max= {y_max}ppm" # y_max number inside string
text6 = text6 + f" y_min= {y_min} " # y_max number inside string
text6 = text6 + f" T_max= {y_Tmax}°C " # y_max number inside string
text6 = text6 + header_black

# 9.6 plot line 6
plt.text(-0.12, -.56, text6 , color="black", fontname="Arial", fontsize=trs,
    transform=plt.gca().transAxes)
fig.tight_layout()
plt.tight_layout()
plt.show()

# 9.7 save the plot line 6
if parameter8_save_png > 0:
   filename = ""
   filename2 = os.path.basename(__file__) # "1234test.py"
   # take only the first 5 characters
   first5 = filename2[:parameter8_save_png]
   filename = filename + first5
   filename = filename + "_"
   filename = filename + header_parameter
   filename = filename + str(x_end)
   path = f"/Users/thomasboettcher/Desktop/python test/40/{filename}"
   fig.savefig(path, dpi=300, bbox_inches="tight")
   path = f"/Users/thomasboettcher/documents/Python/4_Python_CO2/41_CO2_T.png"
   fig.savefig(path, dpi=300, bbox_inches="tight")
# 9.9 close the plotted figure
plt.close(fig)

# Datenquellen:
# CO₂: Mauna-Loa/NOAA Jahresmittel (bis 2023), 2024/2025 vorläufig/Schätzung wie zuvor verwendet.
# https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt
# ppm CO2 = 0.0132251t² - 51.0337t + 49,536.7

