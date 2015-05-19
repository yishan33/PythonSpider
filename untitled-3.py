filename = 'test.txt'
f_date = '2013' + '\n' + '2014'
f = file(filename, 'w+')
f.write(f_date)
f.close()
f = file(filename, 'r+')
f.seek(-4, 2)
f.truncate()
f.close()
f = file(filename, 'r')
line0 = f.readline()
line00 = f.readline()
f.close()
f = file(filename, 'a+')
f.write('2014')
f.close()
f = file(filename, 'r+')
line1 = f.readline()
line2 = f.readline()
f.close()
print line0, line00, line1, line2

