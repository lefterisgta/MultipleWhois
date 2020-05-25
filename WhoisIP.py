from ipwhois import IPWhois
import csv
import domain

__outFile__ = raw_input("Provide your output File Path with .csv file name: ")

try:
    c = csv.writer(open(__outFile__, "wb"))
except Exception as error:
    print "Error in output file", error
else:
    c.writerow(['IP Address', 'Country', 'State', 'City', 'Description', 'Name', 'Emails', 'Range'])

__inputFile__ = raw_input("Enter the list of IP Address file path: ")
try:

    fileOpne = open(__inputFile__, 'r')
    lines = fileOpne.read().strip().split()

    for ip in lines:
        obj = IPWhois(ip)
        out = obj.lookup()

        f = out["nets"][0]['city']
        a = out["nets"][0]['country']
        g = out["nets"][0]['description']
        h = out["nets"][0]['name']
        rangs = out["nets"][0]['range']
        e = out["nets"][0]['state']

        c.writerow([ip, a, e, f, g, h, rangs])
    fileOpne.close()
except Exception as an:
    print "Error in input file :", an