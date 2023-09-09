class StudentsDataException(Exception):
  pass

class BadLine(StudentsDataException):
  def __init__(self, line_number, line_string):
      super().__init__(self)
      self.line_number = line_number
      self.line_string = line_string


class FileEmpty(StudentsDataException):
  def __init__(self):
    super().__init__(self)


from os import strerror

data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
  f = open(file_name, "rt")
  lines = f.readlines()
  f.close()

  if len(lines) == 0:
    raise FileEmpty()

  for i in range(len(lines)):
    line = lines[i]
    columns = line.split()

    if len(columns) != 3:
      raise BadLine(i + 1, line)
    student = columns[0] + ' ' + columns[1]

    try:
      points = float(columns[2])
    except ValueError:
      raise BadLine(i + 1, line)
    try:
      data[student] += points
    except KeyError:
      data[student] = points
  for student in sorted(data.keys()):
    print(student,'\t', data[student])

except IOError as e:
  print("I/O error occurred: ", strerror(e.errno))
except BadLine as e:
  print("Bad line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
  print("Source file empty")
