name = ["UP","Down","Left","Right"]
image = [
        ["animation_data/cat/jump"+str(i)+".png" for i in range(1,8)],
        ["animation_data/cat/lick"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/lickb"+str(i)+".png" for i in range(1,5)],
        ["animation_data/cat/look"+str(i)+".png" for i in range(1,5)],
]
eachmove = {name[i]:image[i] for i in range(4)}