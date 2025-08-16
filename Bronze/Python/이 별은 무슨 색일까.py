lam = int(input())

if lam >= 620 and lam <= 780:
    print("Red")
elif lam >= 590 and lam < 620:
    print("Orange")
elif lam >= 570 and lam < 590:
    print("Yellow")
elif lam >= 495 and lam < 570:
    print("Green")
elif lam >= 450 and lam < 495:
    print("Blue")
elif lam >= 425 and lam < 450:
    print("Indigo")
else:
    print("Violet")
