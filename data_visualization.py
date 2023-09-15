from matplotlib import pyplot as plt

cities = ['Ahmedabad', 'Surat', 'Baroda','Somnath']
cases = [200,180,194,67]

mydata = {"cities": cities, 'cases': cases}
cites_new = mydata['cities']
case_new = mydata['cases']

mydata = {'alldata':[{'cites': "Ahmedabad", 'cases': 200,},
                     {'cites': "surat", 'cases':180},
                     {'cites': "Baroda", 'cases':194},
                     {'cites': "Somnath", 'cases':67}]}
cites_api =[]
cases_api =[]

for i in range(0, len(mydata['alldata'])):
    cites_api.append(mydata['alldata'][i]['cites'])
    cases_api.append(mydata['alldata'][i]['cases'])

plt.bar(cites_api, cases_api, color = "green")
plt.xlabel("cites")
plt.ylabel("cases")
plt.title("Gujarat covid case")
plt.show()
