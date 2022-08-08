# ARRAY GENERATOR

# WRITE THIS SCRIPT TO FILE WITH:
# python Array_Generator.py > ral_vars.py

set_name = "RAL"

pre_array = [
["1000","Green beige","CDBA88"],
["1001","Beige","D0B084"],
["1002","Sand yellow","D2AA6D"],
]

print("")
print("set_name    = \""+set_name+"\"")
print("panel_label = set_name")
print("panel_name  = set_name.upper()")
print("array_name  = \"array_\"+set_name.lower()")
print("\narray = [")

for i in pre_array:
  print("[\""+set_name+i[0]+"\",\""+set_name+i[0]+" - "+i[1]+"\",\""+set_name,i[0]+"\",\""+set_name.lower()+"_"+i[0]+"\",\""+i[2]+"\"],")

print("]")
