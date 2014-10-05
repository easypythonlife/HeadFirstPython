man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file = man_file)
    print(other, file = other_file)
except IOError as err:                  # 예외 내용 상세히 알기, 예외의 상세 내용이 err에 저장되어 있음
    print("File error: " + str(err))    # err을 str로 형변환
finally:
    if 'man_file' in locals():          # 파일이 열린 경우에만 close를 호출 함
        man_file.close()
    if 'other_file' in locals():        # 결국, 예외처리를 위해 "프로그램 논리 추가" 방법을 사용하고 있음
        other_file.close()
