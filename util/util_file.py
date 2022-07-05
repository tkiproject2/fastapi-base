# ===== Module & Library
import os

# ===== Header

# ===== Function
def ListFiles(startpath):
    for root, dirs, files in os.walk(startpath):
        dirPrefix = []
        dirContent = []
        for dir in dirs:
            goInside = os.path.join(startpath, dir)
            dirPrefix.append("")
            dirContent.append(ListFiles(goInside))
        filesList = []
        filesPrefix = []
        for file in files:
            filesList.append(file)
            filesPrefix.append("")
        return {
            "name": root,
            "files": filesList,
            "fileExt": filesPrefix,
            "dirs": dirContent,
            "dirExt": dirPrefix,
        }


def Prepend(list, str):
    list = ["{}{}".format(i, str) for i in list]
    return list


def AddString(result, str_test):
    if result["fileExt"] != []:
        result["fileExt"] = Prepend(result["fileExt"], str_test)
    if result["dirs"] != []:
        result["dirExt"] = Prepend(result["dirExt"], str_test)
        for i in range(len(result["dirs"])):
            AddString(result["dirs"][i], str_test)


def PrintDirectory(startPath, result):
    # prefix
    space = "     "
    branch = "|    "

    # pointer
    tee = "+--- "

    # Resulting Root Folder
    if result["name"] == startPath:
        print("[" + startPath + "]\n|")
    else:
        print(result["name"])

    # Resulting List of Folder first
    if result["dirs"] != []:
        for i in range(len(result["dirs"])):
            if (result["files"] == []) and (
                result["dirs"][i] == result["dirs"][len(result["dirs"]) - 1]
            ):
                AddString(result["dirs"][i], space)
                below_dir = space + branch
            else:
                AddString(result["dirs"][i], branch)
                below_dir = branch + branch
            result["dirs"][i]["name"] = (
                result["dirExt"][i]
                + tee
                + "["
                + os.path.basename(result["dirs"][i]["name"])
                + "]\n"
                + result["dirExt"][i]
                + below_dir
            )
            PrintDirectory(startPath, result["dirs"][i])

    # Resulting List of Files
    if result["files"] != []:
        for i in range(len(result["files"])):
            result["files"][i] = result["fileExt"][i] + tee + result["files"][i]
            print(result["files"][i])


# ===== Class

# ===== Main
