All_Lines=['']
Cur_Line=0

def calc (in_list):
    cur_val=0
    in_op=in_list[1]
    if in_op=="x":
        cur_val=(int(in_list[2])*int(in_list[3]))
    elif in_op=="-":
        cur_val=(int(in_list[2])-int(in_list[3]))
    elif in_op=="/":
        cur_val=(int(in_list[2])/int(in_list[3]))
    elif in_op=="+":
        cur_val=(int(in_list[2])+int(in_list[3]))
    return(cur_val)


f_in = open ("C:\Ian\DevOps\Module-1\calc.txt")

while True:
    str_in = f_in.readline()
    if len(str_in)==0:
        break
#    Check if string is allready in 'All_Lines'
    
    str_list=str_in.split()
#    print(str_list)
    Total+=calc (str_list)
f_in.close

print (Total)
