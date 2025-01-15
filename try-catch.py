try:
    a=(1,2,5,9,"hello")

    # check =a.isDigit()
    for i in a:
        print(isinstance(i,int))
        if not isinstance(i,int):
            raise Exception()
    # pass

except:
    print("There are Exception in code")
finally:
    pass
    print("This run always")