import os
import xml.etree.ElementTree as ET

total = millenium_falcon = tie_fighter = 0
for f in os.listdir('labeled'):
    if f[-4:] != '.xml': continue

    total += 1
    root = ET.parse('labeled/' + f).getroot()
    for tag in root.findall('object/name'):
        if tag.text == 'millenium falcon': millenium_falcon += 1
        else: tie_fighter += 1

print('total: {}'.format(total))
print('millenium_falcon: {}'.format(millenium_falcon))
print('tie_fighter: {}'.format(tie_fighter))
