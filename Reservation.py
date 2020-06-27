import sys,copy

TrainLines = open("D:/github/Train-Reservation/E-on_Train/Trainlist.txt", 'r')
List = []
indlist = []
while True:
    line = TrainLines.readline().split()
    List.append(line)
    if not line:
        break
TrainLines.close()
del List[0]
del List[len(List) - 1]

modyList = copy.deepcopy(List)
reservation_list = []
ind = None


for i in range(20):
    del modyList[i][2]
    modyList[i][0] = modyList[i][0].replace(":", "")
    modyList[i][0] = int(modyList[i][0])


class Train:
    def train_menu(self):
        while True:
            print("1. 빠른 시간 기차 검색 및 예매")
            print("2. 전체 기차 운행시간 보기 ")
            print("3. 예매 현황 및 예약 취소")
            print("4. 프로그램 종료 ")
            try:
                menu = int(input("메뉴를 입력하세요 : "))
            except:
                print("제대로된 숫자를 입력해주세요.(1~4)")
                self.train_menu()

            if menu == 1:
                self.search_train()
            elif menu == 2:
                self.show_list()
            elif menu == 3:
                self.reserved_train()
            elif menu == 4:
                self.program_off()
                break
            elif ValueError:
                print("제대로 된 입력이 아닙니다.")
                self.train_menu()

    def search_train(self):
        print("입력을 해주세요.")
        print("1. 시간 입력하기")
        print("2. 뒤로가기")
        search_train_menu = input("입력 : ")
        if search_train_menu == "1":
            des_train = list(input(
                "조회할 시간(hh:mm), 출발역, 도착역, 열차종류 입력 Ex) 07:00 서울 부산 KTX" 
                "\n시간 입력 : ").split())
            tmp_TL = copy.deepcopy(modyList)

            for i in range(20):
                tmp_TL[i].pop()

            tmp_input_time = int(des_train[0].replace(":", ""))
            a, b = divmod(tmp_input_time, 100) 
            input_time = a * 60 + b 
            time_list = [365, 395, 435, 522]
            des_train[0] = closed_time(input_time, time_list)
            

            closed_T = []

            for i in range(20):
                if tmp_TL[i] == des_train:
                    closed_T = tmp_TL[i].copy()
                    closed_T.append(List[i][5])
                    ind = i
                    print("\n가장 가까운 시간의 기차 정보\n")
            a, b = divmod(closed_T[0], 100)
            a = str(a)
            b = str(b)
            if int(b) // 10 == 0:
                closed_T[0] = ''.join(['0', a, ':', '0', b])
            else:
                closed_T[0] = ''.join(['0', a, ':', b])
            print('', end=' ')
            for a in closed_T:
                print(a, end='  ')

            while True:
                reservation = input("\n해당 기차표를 예매하시겠습니까? [Y/N]"
                                    "\n입력 : ")
                if (reservation == 'Y') or (reservation == 'y'):
                    if List[ind][5] != 0:
                        reservation_list.append(List[ind])
                        List[ind][5] = int(List[ind][5]) - 1
                        print("\n예매가 완료되었습니다.")
                        print("\n메뉴로 돌아갑니다.\n")
                        indlist.append(ind)
                        break
                    elif List[ind][5] == 0:
                        List[ind][5] = "매진"
                        print("매진된 좌석입니다.")
                        print("\n메뉴로 돌아갑니다.\n")
                        break
                   
                elif (reservation == "N") or (reservation =='n'):
                    break
                else:
                    print("Y(y) 또는 N(n)을 입력하세요")
            return ind, reservation_list
        elif search_train_menu == "2":
            self.train_menu()
        elif ValueError:
            print("다시 입력해주세요.")
            self.search_train()
        

    def show_list(self):
        print("1. 모든 기차의 시간대를 확인")
        print("2. 뒤로가기")
        show_list_menu = input("입력 : ")
        if show_list_menu == "1":
            print("====== 전체 기차 시간표 ======"
                  "\n시간  출발역->도착역 열차종류 잔여좌석수\n")
            i = 0
            while i < len(List):
                a, b, c, d, e, f = List[i]
                print(a, b, c, d, e, f)
                i += 1
            print("\n")
        elif show_list_menu == "2":
            self.train_menu()
        elif ValueError:
            print("다시 입력해주세요.")
            self.show_list


    def reserved_train(self):
        print("1. 예매 확인 및 취소")
        print("2. 뒤로가기")
        reserved_train_menu = input("입력 : ")
        if reserved_train_menu == "1":
            print("\n==== 예매 내역 ====\n")

            i = 0
            while i < len(reservation_list):
                a, b, c, d, e, f = reservation_list[i]
                print(a, b, c, d, e, f)
                i += 1
                print(reservation_list)

                if ind is not None or reservation_list is not 0:
                    cancel = input("\n예매를 취소하시겠습니까? [Y/N]"
                                   "\n입력 : ")

                    if cancel == 'Y':
                        if List[indlist[len(indlist) - 1]][5] == '매진':
                            List[indlist[len(indlist) - 1]][5] = 1
                            reservation_list.pop()
                        else:
                            List[indlist[len(indlist) - 1]][5] = List[indlist[len(indlist) - 1]][5] + 1
                            reservation_list.pop()
                        indlist.pop()
                        print('\n취소가 완료되었습니다.')
                else:
                    self.train_menu()



    def program_off(self):
        print("1. 종료")
        print("2. 뒤로가기")
        program_off_menu = input("입력 : ")
        if program_off_menu == "1":
            print("종료합니다.")
            sys.exit()
        elif program_off_menu == "2":
            self.train_menu()


def closed_time(input_time, time_list):
    a = input_time
    b = time_list.copy()
    real_time_list = [605, 635, 715, 842]
    abs_list = []
    for i in range(len(b)):
        abs_list.append(abs(a - b[i]))
    ind = abs_list.index(min(abs_list))
    return real_time_list[ind]


if __name__ == "__main__":
    operate = Train()
    print(operate.train_menu())