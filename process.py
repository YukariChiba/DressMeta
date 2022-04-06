import json

d = {}
dl = {}

def loop_dir(directory, base):
    arr = []
    if "contents" in directory:
        for file in directory["contents"]:
            if file["type"] == "file":
                if file["name"].split(".")[-1].lower() in ["jpg", "png", "jpeg", "gif", "webp"]:
                    print("Adding photo: " + file["name"])
                    arr.append(base + "/" + directory["name"] + "/" + file["name"])
            if file["type"] == "directory":
                arr = arr + loop_dir(file, base + "/" + directory["name"])
    return arr

with open("tmp/tmp.json") as rf:
    j = json.load(rf)
with open("tmp/tmp-lite.json") as rf:
    jl = json.load(rf)

for folder in j:
    if folder["type"] == "directory":
        arr = loop_dir(folder, "")
        if len(arr) != 0:
            d[folder["name"]] = arr

for folder in jl:
    if folder["type"] == "directory":
        arrl = loop_dir(folder, "")
        if len(arrl) != 0:
            dl[folder["name"]] = arrl

with open("data/dress.json", "w") as wf:
    json.dump(d, wf)

with open("data/dress.lite.json", "w") as wfl:
    json.dump(dl, wfl)
