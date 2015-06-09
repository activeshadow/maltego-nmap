import fnmatch, os

from MaltegoTransform import *
from lxml             import etree

m = MaltegoTransform()
m.parseArguments(sys.argv)

filename = m.getValue()

results = []

if os.path.isdir(filename):
  for root, dirnames, filenames in os.walk(filename):
    for result in fnmatch.filter(filenames, 'results.xml'):
      results.append(os.path.join(root, result))
else:
  results.append(filename)

for result in results:
  document = etree.parse(result)

  for host in document.xpath("//host[ports/port[state[@state='open']]]"):
    iface = None

    for addr in host.xpath("address[@addrtype='ipv4']"):
      iface = m.addEntity("maltego.IPv4Address", addr.attrib['addr'])

    if iface != None:
      ports = []

      for port in host.xpath("ports/port[state[@state='open']]"):
        pnum = port.attrib['portid']
        name = []

        try:
          svc = port.xpath("service")[0]

          try:
            name.append(svc.attrib['product'])
            name.append(svc.attrib['version'])
            name.append(svc.attrib['extrainfo'])
          except KeyError:
            if len(' '.join(name)) == 0:
              name.append(svc.attrib['name'])
        except:
          pass

        ports.append("%s::%s" % (pnum, ' '.join(name)))

      iface.addAdditionalFields("service.ports", "Listening Ports", "strict", '|'.join(ports))

m.returnOutput()
