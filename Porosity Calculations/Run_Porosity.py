import calculate_porosity as poros
#Written by Julian A. Davis and Josh Avery
#import ()
import re
import datetime

from pathlib import Path

import csv

currentDT = datetime.datetime.now()
print ("Porosity Calculated at time:" + str(currentDT))



#change path to wherever binary folder is located...
pathlist = Path('/home/JADavi/Documents/').glob('**/*.tiff')



row = ['Porosity']
counter=0

f=open("myfile.csv", "w")
f.close()
f =open("myfile.csv", "a")
pattern = re.compile(r"([0-9]+)\.[^\.]+$")
for path in pathlist:
    id=pattern.search(str(path)).group(1)
    counter = id
    # because path is object not string
    porosity_calc = poros.calculate_porosity(str(path))
    # print(path_in_str)
    print(str(path) + " : " + "Tiff File Time #" + str(counter))
    print(porosity_calc)
    print(f'\t{row[0]} .')

#csv output partially below:


    data = [porosity_calc, id, str(path)]
    out = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    out.writerow(data)


