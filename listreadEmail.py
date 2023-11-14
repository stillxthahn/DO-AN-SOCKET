import socket

def listreadEmail(data):
  list = data.split('\r\n')
  list = list[1:]
  list = list[:-2]
  #tmp = []
  for i in range(0, len(list)):
    list[i] = list[i][2:]
  return list
