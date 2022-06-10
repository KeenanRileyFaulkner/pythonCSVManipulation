# Open cupcakeinvoices.csv
open_file = open("cupcakeinvoices.csv")

# print each row of the csv file
for line in open_file:
    print(line)

# print the type of cupcake purchased for each invoice
open_file.seek(0)
print("\n")
flavors = []
for line in open_file:
    line = line.strip()
    values = line.split(',')
    flavors.append(values[2])
print(flavors)

# print the total for each invoice
open_file.seek(0)
totals = []
for line in open_file:
    line = line.strip()
    values = line.split(',')
    totals.append("{:.2f}".format(round(float(values[3]) * float(values[4]), 2)))
print("\n", totals)

# print the total for all invoices combined
gross = 0
for total in totals:
    gross += float(total)

gross = round(gross, 2)
print("\n", gross)

chocolate_cupcake_gross = 0
vanilla_cupcake_gross = 0
strawberry_cupcake_gross = 0

for i in range(len(totals) - 1):
    if flavors[i] == 'Chocolate':
        chocolate_cupcake_gross += float(totals[i])
    elif flavors[i] == 'Vanilla':
        vanilla_cupcake_gross += float(totals[i])
    else:
        strawberry_cupcake_gross += float(totals[i])

chocolate_cupcake_gross = float("{:.2f}".format(chocolate_cupcake_gross))
vanilla_cupcake_gross = float("{:.2f}".format(vanilla_cupcake_gross))
strawberry_cupcake_gross = float("{:.2f}".format(strawberry_cupcake_gross))

gross_by_flavor = []
gross_by_flavor.append(chocolate_cupcake_gross)
gross_by_flavor.append(vanilla_cupcake_gross)
gross_by_flavor.append(strawberry_cupcake_gross)

flavor = []
flavor.append('Chocolate')
flavor.append('Vanilla')
flavor.append('Strawberry')

import matplotlib.pyplot as plt

plt.bar(flavor, gross_by_flavor)
plt.title('Gross Profit by Flavor of Cupcake')
plt.xlabel('Flavor', fontsize=16, fontweight='bold')
plt.ylabel('Amount($)', fontsize=16, fontweight='bold')
plt.show()

open_file.close()