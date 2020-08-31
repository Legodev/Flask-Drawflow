class DrawflowNodeBase:
    name = "basenode"
    title = "Basenode"
    inputs = list()
    outputs = list()
    icon = ""
    nodehtml = "<b>DO NOT USE THE BASE NODE!!!</b>"

    def name(self, name):
        self.name = name

    def title(self, title):
        self.title = title

    def input(self, varname, type):
        self.inputs.append((varname, type))

    def output(self, varname, type):
        self.outputs.append((varname, type))

    def icon(self, html):
        self.icon = html

    def nodehtml(self, html):
        self.nodehtml = html

    def getAsTuple(self):
        return (self.title, len(self.inputs), len(self.outputs), self.icon, self.name, self.nodehtml)
