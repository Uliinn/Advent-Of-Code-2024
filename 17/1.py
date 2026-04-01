


with open("input.txt","r") as f:
  inp = f.readlines()

  regA = int(inp[0].strip().split()[-1])
  regB = int(inp[1].strip().split()[-1])
  regC = int(inp[2].strip().split()[-1])

  program = [int(v) for v in inp[-1].strip().split()[-1].split(",")]

def get_combo_operand(code):
  match code:
    case 0:
      return 0
    case 1:
      return 1
    case 2:
      return 2
    case 3:
      return 3
    case 4:
      return regA
    case 5:
      return regB
    case 6:
      return regC
    case 7:
      raise ValueError("Not valid literal")

pointer = 0
output = []
while pointer < len(program):
  opcode = program[pointer]

  match opcode:
    case 0:
      regA = regA >> get_combo_operand(program[pointer + 1])
    case 1:
      regB = regB ^ program[pointer + 1]
    case 2:
      regB = get_combo_operand(program[pointer + 1]) & 0b111
    case 3:
      if regA == 0:
        pointer += 2
      else:
        pointer = program[pointer + 1]
    case 4:
      regB = regB ^ regC
    case 5:
      output.append(get_combo_operand(program[pointer + 1]) & 0b111) 
    case 6:
      regB = regA >> get_combo_operand(program[pointer + 1])
    case 7:
      regC = regA >> get_combo_operand(program[pointer + 1])
  
  if opcode != 3:
    pointer += 2

print(",".join(map(str,output)))
