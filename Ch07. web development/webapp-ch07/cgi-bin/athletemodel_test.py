from athletemodel import put_to_store, get_from_store

# 선수들의 데이터가 담긴 파일 목
the_files = ["../data/james.txt", "../data/julie.txt", "../data/mikey.txt", "../data/sarah.txt"]

# 선수들의 파일 목록을 읽어서 각 파일의 내용을 AthleteList 객체로 변환 후, 이름을 key로 하여 전체를 하나의 dictionary 객체로 만들고,
# 이를 pickle로 저장하는 함수
put_to_store(the_files)

# 저장된 pickle에서 dictionary 객체를 불러와 athletes 변수에 저장
athletes = get_from_store()

# 확인 용 출력
print(athletes)
print(athletes['Julie Jones'].clean_data)
print(athletes['Julie Jones'].top3)

# 생일 출력하기
for each in athletes:
    print(athletes[each].name + ' ' + athletes[each].dob)