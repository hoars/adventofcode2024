import pandas as pd

with open("input.txt") as file:
    lines = [line.replace("\n","") for line in file]

xys_dict = {}
logic_wires = []
for line in lines:
    if ":" in line:
        key = line.split(":")[0]
        value = int(line.split(":")[1])
        xys_dict[key] = value
    elif line=="":
        # trash line to remove this empty string because im a simpleton and dont want to figure out better way to do
        print(line)
    else:
        logic_wires.append(line)

logic_wires = [wire.split(" ") for wire in logic_wires]

logics={"OR":"|", "AND":"&", "XOR":"^"}
def logic(a,b,x):
    answer=eval(f"{a} {logics[x]} {b}")
    return answer
    
keep_going=True
while keep_going:
    needs_another_round=[]
    for logic_list in logic_wires:
        try:
            xys_dict[logic_list[4]]=logic(xys_dict[logic_list[0]], xys_dict[logic_list[2]], logic_list[1])
        except:
            needs_another_round.append(logic_list)
    if len(needs_another_round)==0:
        keep_going= False
        
decimal = 0
for key in xys_dict.keys():
    if key.startswith("z"):
        decimal = decimal + xys_dict[key] * (2**int(key.replace("z","")))

print(decimal)