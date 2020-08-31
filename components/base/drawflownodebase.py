class DrawflowNodeBase:
    name = "Basenode"
    inputs = 0
    outputs = 0
    icon = ""
    node = "basenode"
    nodehtml = "<b>DO NOT USE THE BASE NODE!!!</b>"

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
