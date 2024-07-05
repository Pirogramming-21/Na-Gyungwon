# 단계 별 commit
# 1단계: num 선언
num = 0

# 2단계: input()으로 1~3 정수 입력
# num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")


# 3단계:
# 2단계에서 정수가 아닐 경우 "정수를 입력하세요" 출력
# 1,2,3을 입력하지 않는 경우, "1, 2, 3 중 하나를 입력하세요" 출력
# 올바른 값이 입력될 때가지 입력 요구
def input_num():
    while True:
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

        if not num.isdigit():
            print("정수를 입력하세요.")
            continue

        num = int(num)

        if num not in [1, 2, 3]:
            print("1, 2, 3 중 하나를 입력하세요")
            continue

        break
    return num


# num = input_num()

# 4단계: num을 이용하여 2단계에서 입력한 수만큼 숫자를 출력하는 코드 작성

# cur_num = 1
# for i in range(num):
#     print(f"playerA: {cur_num}")
#     cur_num += 1

# 5단계:
# 1~3 사이의 정수를 입력받는 코드 작성 "부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): "
# 정수를 입력하지 않는 경우, "정수를 입력하세요" 출력
# 1,2,3을 입력하지 않는 경우 , "1, 2, 3 중 하나를 입력하세요" 출력
# 올바른 값이 입력될 때가지 입력 요구
# num을 이용하여 입력한 수만큼 숫자를 출력하는 코드 작성

# num = input_num()

# for i in range(num):
#     print(f"playerB: {cur_num}")
#     cur_num += 1

# 6단계: 게임이 끝날 때까지 playerA와 playerB에게 번갈아가며 부를 숫자의 개수를 입력받는 코드 작성

# players = ["playerA", "playerB"]
# cur_idx = 0

# while cur_num < 32:
#     num = input_num()
#     for i in range(num):
#         print(f"{players[cur_idx%2]}: {cur_num}")
#         cur_num += 1
#         if cur_num >= 32:
#             break
#     cur_idx += 1

# 7단계: 게임이 끝났을 때, 누가 이겼는지 출력
# "playerA win!" / "playerB win!"

# print(f"{players[cur_idx%2]} win!")


# 8단계: 6단계까지 중복되는 코드를 찾아 함수로 만들기, 함수 이름 "brGame"
def brGame(num, players, cur_idx=0, cur_num=1):
    for i in range(num):
        if cur_num >= 32:
            break
        print(f"{players[cur_idx%2]}: {cur_num}")
        cur_num += 1

    cur_idx += 1
    return [cur_idx, cur_num]


players = ["playerA", "playerB"]
cur_idx = 0
cur_num = 1
while cur_num < 32:
    num = input_num()
    cur_idx, cur_num = brGame(num, players, cur_idx, cur_num)

print(f"{players[cur_idx%2]} win!")

# 9단계: computer과 대결하는 배스킨라빈스31게임 제작
# playerA -> computer, playerB -> player
# computer는 임의로 1~3의 수
# random, randint(a, b) a <= n <= b인 n
