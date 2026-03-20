def add_stop(stops_as_string: str, some_index: int, some_sub_string: str) -> str:
    if some_index in range(len(stops_as_string)):
        left_part = stops_as_string[:some_index]
        right_part = stops_as_string[some_index:]
        stops_as_string = left_part + some_sub_string + right_part
    return stops_as_string
 
 
def remove_stop(stops_as_string: str, some_start_index: int, some_end_index: int) -> str:
    if some_start_index in range(len(stops_as_string)) and \
            some_end_index in range(len(stops_as_string)):
        left_part = stops_as_string[:some_start_index]
        right_part = stops_as_string[some_end_index + 1:]
        stops_as_string = left_part + right_part
    return stops_as_string
 
 
def switch(stops_as_string: str, some_old_string:str, some_new_string:str) -> str:
    if some_old_string in stops_as_string:
        stops_as_string = stops_as_string.replace(some_old_string, some_new_string)
    return stops_as_string
 
 
stops = input()
command = input().split(":")
while command[0] != "Travel":
    action = command[0]
    if action == "Add Stop":
        index, sub_string = int(command[1]), command[2]
        stops = add_stop(stops, index, sub_string)
    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif action == "Switch":  # else
        old_string, new_string = command[1], command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)
    command = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")
 
