def solution(players, callings):
    answer = [0] * len(players)
    player_to_index = {}  # player: index
    index_to_player = {}  # index: player
    for i in range(len(players)):
        player_to_index[players[i]] = i
        index_to_player[i] = players[i]

    for call in callings:
        call_idx = player_to_index[call]  # 불려진 현재 플레이어 인덱스
        front_idx = call_idx - 1  # 앞선 플레이어 인덱스
        front_player = index_to_player[front_idx]  # 앞선 플레이어의 이름

        # player: index / index: player에 대해 각각 순서를 바꿔준다
        player_to_index[call], player_to_index[front_player] = front_idx, call_idx
        index_to_player[call_idx], index_to_player[front_idx] = front_player, call
    # index: player형태의 딕셔너리에서 value값들을 리스트형태로 반환하면 경주가 끝났을 때의 순서대로 나타내준다.
    return list(index_to_player.values())
