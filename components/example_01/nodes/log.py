from components.base.drawflownodebase import DrawflowNodeBase


class FileLogNode(DrawflowNodeBase):
    name = "File Log"
    inputs = 1
    outputs = 0
    icon = 'fas fa-file-signature'
    node = 'log'
    nodehtml = """<div><div class="title-box"><i class="fas fa-file-signature"></i> Save log file </div></div>"""

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
