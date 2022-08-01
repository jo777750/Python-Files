def __getattr__(name):
    op,num=name.split("_")
    num=int(num)
    return{
        "times":lambda val:val*num,
        "plus":lambda val:val+num,
    }[op]
