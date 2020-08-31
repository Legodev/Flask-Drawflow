from components.base.drawflownodebase import DrawflowNodeBase


class PersonalizedNode(DrawflowNodeBase):
    name = "Personalized"
    inputs = 1
    outputs = 1
    icon = 'fas fa-fill'
    node = 'personalized'
    nodehtml = """<div>Personalized</div>"""

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
