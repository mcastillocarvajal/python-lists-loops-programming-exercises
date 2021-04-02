parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(matrix):
    state = {
        'total_slots': 0,
        'available_slots': 0,
        'occupied_slots': 0
    }
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] != 0:
                state['total_slots'] += 1
                if matrix[row][col] == 1:
                    state['occupied_slots'] += 1
                else:
                    state['available_slots'] += 1
    return state

print(get_parking_lot(parking_state))
