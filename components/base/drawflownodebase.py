class DrawflowNodeBase:
    def __init__(self):
        self.nodename = "basenode"
        self.nodetitle = "Basenode"
        self.nodeinputs = list()
        self.nodeoutputs = list()
        self.nodeicon = ""
        self.nodehtml = "<b>DO NOT USE THE BASE NODE!!!</b>"

    def name(self, name):
        self.nodename = name

    def title(self, title):
        self.nodetitle = title

    def input(self, varname, type):
        self.nodeinputs.append((varname, type))

    def output(self, varname, type):
        self.nodeoutputs.append((varname, type))

    def icon(self, html):
        self.nodeicon = html

    def html(self, html):
        self.nodehtml = html

    def getAsTuple(self):
        return (self.nodetitle, len(self.nodeinputs), len(self.nodeoutputs), self.nodeicon, self.nodename, self.nodehtml)
