
def calc (in_list):
    cur_val=0
    in_op=in_list[2]
    if in_op=="x":
        cur_val=(int(in_list[3])*int(in_list[4]))
    elif in_op=="-":
        cur_val=(int(in_list[3])-int(in_list[4]))
    elif in_op=="/":
        cur_val=(int(in_list[3])/int(in_list[4]))
    elif in_op=="+":
        cur_val=(int(in_list[3])+int(in_list[4]))
    return(cur_val)

f_lines=[]
f_in = open ("C:\Ian\DevOps\Module-1\calc3.txt")
for line in f_in:
    f_lines.append(line)
f_in.close()

not_found=True
cur_line=0
cur_count=1
while cur_count<<10:
    lis_cmd=f_lines[cur_line].split()
    print (lis_cmd)
# If the line has a calc, work it out
#    str_cmd=lis_cmd[cur_line]
    if len(lis_cmd[cur_line]) >> 3:
        cur_line=calc(lis_cmd[cur_line])
    else:
        str_cmd=lis_cmd[cur_line]
        cur_line=int(str_cmd(1))
        print(str_cmd)
    not_found=False
    cur_count+=1

print (cur_line)


#    if len(str_in)==0:
#        break
#    Check if string is allready in 'All_Lines'
    
#    str_list=str_in.split()
#    print(str_list)
#    Total+=calc (str_list)
#f_in.close
#print (Total)
