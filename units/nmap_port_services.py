from MaltegoTransform import *

m = MaltegoTransform()
m.parseArguments(sys.argv)

ports = m.getVar('service.ports') # string
ports = ports.split('|')  # array

for port in ports:
  port, name = port.split('::')

  svc = m.addEntity('maltego.Service', port)
  svc.addAdditionalFields("port.number", "Port", "strict", port)
  svc.addAdditionalFields("banner.text", "Service Banner", "strict", name)

m.returnOutput()
