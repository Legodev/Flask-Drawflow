from components.base.drawflownodebase import DrawflowNodeBase


class SlackNode(DrawflowNodeBase):
    name = "Slack recive message"
    inputs = 1
    outputs = 0
    icon = 'fab fa-slack'
    node = 'slack'
    nodehtml = '<div><div class="title-box"><i class="fab fa-slack"></i> Slack chat message</div></div>'

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
