import string
from string import ascii_uppercase as up_case
from string import ascii_lowercase as lo_case


# caesar 함수 시작(s = msg, k = encrypt_key, decode(True or False))
def caesar(s, k, decode = False):
    # decode 가 True일 경우, encrypt_key를 시프트(26이라는 인덱스를 가지고 있는 리스트안에서 로테이션(복호화))
    # decode 가 False일 경우, 이부분을 진행하지 않고 encrypt_key 그대로 진행(암호화)
    if decode: 
        k = 26 - k

# string의 translate를 실행함. maketrans 함수를 활용하여 원래 리스트를 encrypt_key를 기준으로 재조립하여 이를 암호화에 사용
    return s.translate(
        str.maketrans(
            up_case + lo_case,
            up_case[k:] + up_case[:k] +
            lo_case[k:] + lo_case[:k]
            )
        )

# 실제 실행 부분(무한반복)
# encrypt_key와 msg를 사용자에게서 입력받아 이를 이용하여 caesar 함수 실행(암호화, 복호화 결과 모두 출력)
# q를 누르면 while 문을 break하고 프로그램을 종료
while True:
    encrypt_key = int(input("decide the magic number: "))
    msg = input("enter the message: ")
    print("encrypted message: ", caesar(msg, encrypt_key))
    print("decrypted message: ", caesar(caesar(msg, encrypt_key), encrypt_key, True))
    exit = input("press 'q' to quit: ")
    if exit == 'q' or exit == 'Q':
        break









