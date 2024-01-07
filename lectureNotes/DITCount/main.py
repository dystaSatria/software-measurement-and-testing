def dit(yolcu):
    return sum(i for i in range(1, yolcu+1) if yolcu % i == 0)
