def perm(selected, remain):  
    '''
    Args:
        selected: 선택된 값 목록
        reamin: 선택되지 않고 남은 값 목록 
    '''
    if not remain:
        print(selected)
        return
    else:
        for idx in range(len(remain)):
            selected_elem = remain[idx]
            remain_list = remain[:idx] + remain[idx + 1:]
            perm(selected + [selected_elem], remain_list)
            # selected.append(remain.pop(idx))


# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3])
