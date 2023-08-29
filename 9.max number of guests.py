def max_guests_present(E, L, T):
    timeline = []
    for i in range(len(E)):
        timeline.append((E[i], 1))
        timeline.append((L[i], -1))
    timeline.sort()
    max_guests = 0
    current_guests = 0
    for event in timeline:
        guests, action = event
        current_guests += guests * action
        max_guests = max(max_guests, current_guests)
    return max_guests

num_hours = int(input("Enter the number of hours: "))
E = []
L = []
for i in range(num_hours):
    e = int(input(f"Enter the number of guests entering at hour {i + 1}: "))
    l = int(input(f"Enter the number of guests leaving at hour {i + 1}: "))
    E.append(e)
    L.append(l)
T = int(input("Enter the time limit (T): "))
result = max_guests_present(E, L, T)
print(f"The maximum number of guests present within {T} hours: {result}")
