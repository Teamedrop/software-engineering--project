todo_list = []

for i in range(50):
    title = f"Task {i}"

    obj = {"id": i, "title": title}

    todo_list.append(obj)

    todo_obj[i] = {"title": title}


# print("Todo Object", todo_obj)
# print("\n\nTodo List", todo_list)

search_id = 49

list_start = time.perf_counter()
for todo in todo_list:
    if todo["id"] == search_id:
        print("Found")

list_stop = time.perf_counter()
list_time = list_stop - list_start

print("Time elapsed for list search is ", list_stop - list_start)

dict_start = time.perf_counter()
if todo_obj[search_id]:
    print("Found in Dict")
dict_stop = time.perf_counter()
dict_time = dict_stop - dict_start

print("Time difference is ", list_time - dict_time)