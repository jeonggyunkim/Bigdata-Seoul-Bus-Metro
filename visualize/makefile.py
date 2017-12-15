f = open('visualize.html', 'w', encoding='utf-8')

with open('main.html', 'r', encoding='utf-8') as ff:
  a = ff.read()

ind = a.find('parse') + 7
f.write(a[:ind])
with open('bus_dummy.json', 'r') as w:
	f.write(w.read())
f.write(a[ind:])
f.close()