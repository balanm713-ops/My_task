# # qns 3 :
class Printer(): #3
    def print_info(self,*args):
        if len(args)==1:
            print(f"single info : {args[0]}")
        elif len(args)==2:
            print(f"two info : {args[0]}, {args[1]}")
        elif len(args)>2:
            print(f'multiple inputs : {",".join(map(str,args))}')
        else:
            print("no inforamtion")
a=Printer()
a.print_info('balan',43,'college')

# ----------------------------------------------------------------------------------
# qns 3 :
a = 5
b = 4
def swap(a,b):
    d = a
    a=b
    b =d
    print((a,b))

swap(a,b)
