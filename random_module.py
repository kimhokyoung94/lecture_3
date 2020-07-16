import random as rd

def random_monster():
    #print(type(rd.randint(1,3)))
    monster = rd.randint(1,10)
    human = rd.randint(1,6)
    command = input('공격은 hit 입력,도망가기는 run\n')
    if(command == 'hit'):
        if(monster >= human):
            print('U lose')
        else:
            print('U win')
    elif(command == 'run'):
        if(monster >= human):
            print('실패했다!')
            return random_monster()
        else:
            print('도망쳤다!')
    else:
        print('다시선택하세요')
        return random_monster()
    
#random_monster() # 몬스터 휴먼 게임

def lotto_number_list():
    number = list(range(1,46))
    selec_num = rd.randint(1,8)
    for _ in range(1,9):
        list.append(selec_num)
    print(list)


def lotto_number():
    number = list(range(1,46))
    selec_num = rd.randint(1,8)
    first_num = number[rd.randint(1,8)-1]
    second_num = number[rd.randint(9,16)-1]
    third_num = number[rd.randint(17,24)-1]
    fouth_num = number[rd.randint(25,32)-1]
    fifth_num = number[rd.randint(33,40)-1]
    sixth_num = number[rd.randint(41,45)-1]
    print('오늘 대박예감 번호입니다 {},{},{},{},{},{}'.format(first_num,second_num,third_num,fouth_num,fifth_num,sixth_num ))
    # print(selec_num)