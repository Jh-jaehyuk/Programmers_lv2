def solution(m, musicinfos):
    # #이 들어간 음을 한글자로 변환
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    # m이 들어가는 음악을 저장할 리스트
    result = []

    for i in musicinfos:
        # 뮤직인포에 있는 정보를 ',' 를 기준으로 나눔
        arr = i.split(',')
        # 음악길이를 기록하기 위해 시간을 ':' 기준으로 나눔
        l = arr[0].split(':') + (arr[1].split(':'))
        # 음악길이를 분 단위로 계산하기 위해 시간에 *60하고 분을 더해줌
        music_length = (int(l[2]) * 60 + int(l[3])) - (int(l[0]) * 60 + int(l[1]))
        # #이 들어간 음을 한글자로 변환
        arr[3] = arr[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        # 뮤직인포에 있는 음악정보를 한글자마다 잘라서 리스트로 변환
        music = [i for i in arr[3]]
        count = 0
        idx = 0
        y = ''
        # 음악길이만큼 반복하기 위함
        while count < music_length:
            # 음악길이가 음악정보보다 길다면 다시 처음부터 시작
            if idx >= len(music):
                idx = 0
            y += music[idx] # 실제 음악길이만큼 반복된 음악
            idx += 1
            count += 1
        # 만약 무지가 들은 음악 m이 실제 음악안에 있다면
        if m in y:
            # 리스트에 음악길이와 음악이름을 저장
            result.append((music_length, arr[2]))
    # 리스트에 음악이 여러개일 경우, 음악길이가 긴 것을 기준으로 하므로
    # 음악길이가 긴 것이 리스트의 처음으로 오게 정렬
    result.sort(key=lambda x: (-x[0]))
    # 리스트에 음악이 저장되어있다면, 첫번째 음악을 반환하고
    # 리시트에 음악이 없다면 '(None)' 을 반환
    return result[0][1] if result else '(None)'


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
