from components.base.drawflownodebase import DrawflowNodeBase


class GithubNode(DrawflowNodeBase):
    name = "Github Star"
    inputs = 0
    outputs = 1
    icon = 'fab fa-github'
    node = 'github'
    nodehtml = """
          <div>
            <div class="title-box"><i class="fab fa-github "></i> Github Stars</div>
            <div class="box">
              <p>Enter repository url</p>
            <input type="text" df-name>
            </div>
          </div>
          """

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
