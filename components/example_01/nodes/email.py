from components.base.drawflownodebase import DrawflowNodeBase


class EmailSendNode(DrawflowNodeBase):
    name = "Email send"
    inputs = 1
    outputs = 0
    icon = 'fas fa-at'
    node = 'email'
    nodehtml = """<div><div class="title-box"><i class="fas fa-at"></i> Send Email </div></div>"""

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
