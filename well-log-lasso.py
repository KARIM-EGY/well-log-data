import lasio
import pandas as pd
import matplotlib.pyplot as plt

las = lasio.read(r'D:\Karim\Geostatics\A12a_A2-logdata\A12a-CPP-A02_1225in.LAS')
las.sections.keys()
for item in las.sections['Well']:
    print (f'{item.descr}  ({item.mnemonic}) : \t\t {item.value}')
for count, par in enumerate(las.curves):
    print (f"curve :{par.mnemonic} \t Unit :{par.unit} \t The describtion :   {par.descr} ")
print (f'There is {count+1} curves in this log file')
df = las.df()
df.head()

df['GR_ARC'].plot(kind='hist', bins = 30, alpha = 0.5, density = True, edgecolor= 'black', color = 'red')
df['GR_ARC'].plot(kind = 'kde', color = 'black')
plt.xlabel('Gamma Ray - API')
plt.ylabel('Frequency')
plt.xlim(0,150)


average = df['GR_ARC'].mean()
p5 = df['GR_ARC'].quantile(0.05)
p95 = df['GR_ARC'].quantile(0.95)
print (f'Mean of API : \t {average} \n p5% : \t {p5} \n p95% : \t {p95}')

plt.scatter(x = 'TNPH' , y = 'ROBB', data = df , c = 'GR_ARC' , vmin = 0, vmax=150, cmap = 'rainbow')
plt.colorbar(label='Gamma Ray color scale')
plt.title("Cross plot")
plt.xlabel("Thermal Neutron Porosity")
plt.ylabel("Bulk Density")
plt.show()
df.reset_index(inplace = True)
df.rename(columns={'DEPT':'Depth','GR_ARC':'GR', 'ROBB':'Density', 'TNPH':'Neutron'}, inplace = True)
df.head()

fig = plt.subplots(figsize = (10,10))


log1 = plt.subplot2grid((1,3), (0,0) , rowspan = 1, colspan=1) # subplot 1
log2 = plt.subplot2grid((1,3), (0,1) , rowspan = 1, colspan=1) # subplot 2
log3 = plt.subplot2grid((1,3), (0,2) , rowspan = 1, colspan=1) # subplot 3
log4 = log3.twiny() # subplot 4
log5 = log2.twiny() # subplot 4
for log in [log2, log3]:
    plt.setp(log.get_yticklabels(),visible = False)

#Gamma Ray log
log1.plot('GR', 'Depth',data = df, color ='green')
log1.set_xlim(0,150)
log1.set_ylim(400,700)
log1.set_title('Gamma Ray - API')
log1.grid()

# Resistivty semi log
log2.plot('P16H_UNC', 'Depth', data = df , color = 'red')
log2.set_ylim(400,700)
log2.set_xlim(0.2 , 2000)
log2.semilogx()
log2.grid()
log2.set_title('Resistivity_Deep- OHM')
# Resistivty semi log
log5.plot('P40H_UNC', 'Depth', data = df , color = 'blue')
log5.set_ylim(400,700)
log5.set_xlim(0.2 , 2000)
log5.semilogx()
log5.grid()
log5.set_title('Resistivity_Deep- OHM')

# Neutron porosity log
log3.plot('Neutron', 'Depth',data = df, color ='yellow')
log3.set_title('Neutron - Density')
log3.grid()
plt.xticks(rotation = 45)
log3.set_ylim(400,700)

# Density porosity log
log4.plot('Density', 'Depth',data = df, color ='blue')
log3.set_ylim(400,700)


