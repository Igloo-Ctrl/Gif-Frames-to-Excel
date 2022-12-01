with open("frames/frame_TEST1.txt", "r") as f:
    data = f.readlines()
    stop = 0
    for i in data:
        if stop == 2:
            break
        else:
            print(i)
            stop += 1
