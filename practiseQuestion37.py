def rec_func(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    rec_func(list, idx+1)

fb=["messi","cr","lewa","ney","zid"]

rec_func(fb)