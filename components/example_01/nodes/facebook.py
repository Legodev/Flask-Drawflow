from components.base.drawflownodebase import DrawflowNodeBase


class FacebookNode(DrawflowNodeBase):
    name = "Facebook"
    inputs = 0
    outputs = 1
    icon = 'fab fa-facebook'
    node = 'facebook'
    nodehtml = '<div><div class="title-box"><i class="fab fa-facebook"></i> Facebook Message</div></div>'

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
