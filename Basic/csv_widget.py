import csv




def reader():
  f = open('input.csv', 'r')
  rd = csv.reader(f)
  for e, line in enumerate(rd):
    print(line)
  f.close()


def dict_reader():
  f = open('input.csv', 'r')
  rd = csv.DictReader(f)
  for e, line in enumerate(rd):
    print(line)
  f.close()

dict_reader()