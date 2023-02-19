dict = {'A':'best!!!','B':'good!!','C':'run!','D':'slowly~'}

a = input()

if(a in dict):
    for i in dict.keys():
        if(a == i):
            print(dict[i])
else:
    print("what?")
