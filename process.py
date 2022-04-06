import json

d = {}

def loop_dir(directory, base):
    arr = []
    if "contents" in directory:
        for file in directory["contents"]:
            if file["type"] == "file":
                if file["name"].split(".")[-1].lower() in ["jpg", "png", "jpeg", "gif", "webp"]:
                    arr.append(base + "/" + directory["name"] + "/" + file["name"])
            if file["type"] == "directory":
                arr = arr + loop_dir(file, base + "/" + directory["name"])
    return arr

with open("tmp/tmp.json") as rf:
    j = json.load(rf)

for folder in j:
    if folder["type"] == "directory":
        arr = loop_dir(folder, "")
        if len(arr) != 0:
            d[folder["name"]] = loop_dir(folder, "")

with open("data/dress.json", "w") as wf:
    json.dump(d, wf)

