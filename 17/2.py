

with open("input.txt","r") as f:
  inp = f.readlines()

  program = [int(v) for v in inp[-1].strip().split()[-1].split(",")]

def run(regA):
        regB = regC = 0
        pointer = 0
        outputs = []
        while pointer < len(program):
            op = program[pointer]
            lit = program[pointer + 1]
            combo = [0,1,2,3,regA,regB,regC][lit] if lit < 7 else None
            match op:
                case 0: regA = regA >> combo
                case 1: regB = regB ^ lit
                case 2: regB = combo & 7
                case 3:
                    if regA != 0:
                        pointer = lit
                        continue
                case 4: regB = regB ^ regC
                case 5: outputs.append(combo & 7)
                case 6: regB = regA >> combo
                case 7: regC = regA >> combo
            pointer += 2
        return outputs


# Build regA backwards, 3 bits at a time
candidates = [0]
for target in reversed(program):
    next_candidates = []
    for base in candidates:
        for bits in range(8):
            regA = (base << 3) | bits
            if run(regA)[0] == target:
                next_candidates.append(regA)
    candidates = next_candidates

print(min(candidates))
