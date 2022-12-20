import os

thisNode = hou.pwd();
path = thisNode.evalParm("fbxDirectoryPath");
if os.path.exists(path):
    pathList = os.listdir(path)
    for fileName in pathList:
        if fileName.endswith(".fbx"):
            fileNode = thisNode.createOutputNode("file");
            filePath = path + fileName;
            fileNode.setParms({"file": filePath});
            fileNode.setDisplayFlag("on");
            fileNode.cook();   # 虽然不知道原因， 但确实起到了生成 fbm.texture 的效果
            fileNode.destroy();
            