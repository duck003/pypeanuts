name = ["jump","lick","lickb","look","paw","run","scared","sit","sleep","sprint"]
image = [
        ["animation_data/cat/jump"+str(i)+".png" for i in range(1,8)],
        ["animation_data/cat/lick"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/lickb"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/look"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/paw"+str(i)+".png" for i in range(1,7)],
        ["animation_data/cat/run"+str(i)+".png" for i in range(1,9)],
        ["animation_data/cat/scared"+str(i)+".png" for i in range(1,9)],
        ["animation_data/cat/sit"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/sleep"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/sprint"+str(i)+".png" for i in range(1,9)]
        ]

eachmove = {name[i]:image[i] for i in range(10)}