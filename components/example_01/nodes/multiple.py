from components.base.drawflownodebase import DrawflowNodeBase


class MultipleIONode(DrawflowNodeBase):
    name = "Multiple inputs / outputs"
    inputs = 3
    outputs = 4
    icon = 'fas fa-code-branch'
    node = 'multiple'
    nodehtml = """<div><div class="box">Multiple!</div></div>"""

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
