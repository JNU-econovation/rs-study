dict = {'A':'best!!!','B':'good!!','C':'run!','D':'slowly~'}

a = input()

if(a in dict):
    for i in dict.keys():
        if(a == i):
            print(dict[i])
else:
    print("what?")

# 딕셔너리 자료형 이용
# dict.keys()는 dict의 Key만 모아서 dick_keys객체를 반환해준다. 이 객체는 리스트를 사용하는 것과 비슷하지만,
# 리스트 고유의 append,insert,pop,remove,sort 함수는 수행 할 수 없다.
