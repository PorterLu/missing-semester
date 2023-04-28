import gdb
from pathlib import Path

class RegDump(gdb.Command):
  def __init__(self):
    super(RegDump, self).__init__(
        "rdump", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL
    )

  def invoke(self, arg, _):
      array = gdb.parse_and_eval(f'array')
      num_elements = int(array.type.sizeof / array.type.target().sizeof)
      for i in range(num_elements):
        gdb.write('Element{} : {}\n'.format(i, array[i]))
      print('-' * 40)

RegDump()
