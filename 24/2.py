
# ripple carry adder
# z45 carry bit and others the same

variables = {}

highest_zs = 0
swaps = []
with open("input.txt","r") as f:
  inp = f.readlines()
  i = 0
  while inp[i] != "\n":
    var, val = inp[i].split()
    variables[var[:-1]] = int(val) # remove :
    i += 1
  
  statements = [[v for v in row.strip().split()] for row in inp[i+1:]]

  for x1,op,x2,_,ans in statements:
    if "z" in ans and highest_zs < int(ans[1:]):
      highest_zs = int(ans[1:])
    variables[ans] = (x1,op,x2)


# Find a gate with a specific operator and variables
def find_gate(op, a, b):
    for wire, val in variables.items():
        if not isinstance(val, tuple):
            continue
        x1, gop, x2 = val
        if gop == op and {x1, x2} == {a, b}:
            return wire
    return None

def swap_wires(a, b):
    variables[a], variables[b] = variables[b], variables[a]
    swaps.extend([a, b])

# z00 is a special case: x00 XOR y00 (no carry in)
# Find carry out from bit 0: x00 AND y00
carry = find_gate("AND", "x00", "y00")

for i in range(1, highest_zs):
    xi = f"x{i:02d}"
    yi = f"y{i:02d}"
    
    # Half ader: xi XOR yi
    half_sum = find_gate("XOR", xi, yi)
    
    # Förväntad z: half_sum XOR carry
    z = f"z{i:02d}"
    expected_z = find_gate("XOR", half_sum, carry)
    
    if expected_z is None:
        # Something is wrongly swapped, find which wire is wrong
        # Look if z-wire exists but with wrong input
        zval = variables[z]
        if isinstance(zval, tuple):
            zx1, zop, zx2 = zval
            if zop == "XOR":
                # One of the inputs are wrong, swap the one that is not carry or half_sum
                wrong = zx1 if zx2 in (half_sum, carry) else zx2
                correct = carry if zx2 == half_sum else half_sum
                # Hitta vad wrong egentligen borde vara
                swap_wires(wrong, correct)
                expected_z = z
    elif expected_z != z:
        # Right structure but wrong output wire
        swap_wires(expected_z, z)
        expected_z = z
    
    # Carry propagation:
    # new_carry = (half_sum AND carry) OR (xi AND yi)
    carry_and = find_gate("AND", half_sum, carry)
    direct_and = find_gate("AND", xi, yi)
    new_carry = find_gate("OR", carry_and, direct_and)
    
    if new_carry is None:
      
      if len(swaps) == 8: # Fine, then no more swaps to make
        break
      else:
         raise Exception("new_carry is None")
    
    carry = new_carry

print(",".join(sorted(swaps)))