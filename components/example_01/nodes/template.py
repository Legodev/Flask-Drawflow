from components.base.drawflownodebase import DrawflowNodeBase


class TemplateNode(DrawflowNodeBase):
    name = "Template"
    inputs = 1
    outputs = 1
    icon = 'fas fa-code'
    node = 'template'
    nodehtml = """
            <div>
              <div class="title-box"><i class="fas fa-code"></i> Template</div>
              <div class="box">
                Ger Vars
                <textarea df-template></textarea>
                Output template with vars
              </div>
            </div>
            """

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
