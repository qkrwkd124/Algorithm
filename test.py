def min_swaps_to_rearrange(before, after):
    # 매핑 생성: 각 문자의 'before' 위치에서 'after' 위치로의 매핑
    position_map = {before[i]: after[i] for i in range(len(before))}
    
    # 방문 여부를 추적하기 위한 집합
    visited = set()
    swaps = 0
    
    for char in before:
        # 이미 방문한 문자는 건너뛴다
        if char in visited:
            continue
        
        # 현재 순환을 탐색하기 시작
        current = char
        cycle_length = 0
        
        # 순환을 따라가며 길이를 계산
        while current not in visited:
            visited.add(current)
            current = position_map[current]
            cycle_length += 1
        
        # 순환의 길이가 1보다 클 경우, 해당 순환을 재배치하는 데 필요한 최소 스왑 횟수를 추가
        if cycle_length > 1:
            swaps += cycle_length - 1
    
    return swaps

# 함수 호출은 주석 처리하였습니다.
result = min_swaps_to_rearrange(["A", "B", "C"], ["B", "C", "A"])
print(result)
