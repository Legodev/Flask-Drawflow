from components.base.drawflownodebase import DrawflowNodeBase


class AWSNode(DrawflowNodeBase):
    name = "AWS"
    inputs = 1
    outputs = 1
    icon = 'fab fa-aws'
    node = 'aws'
    nodehtml = """
          <div>
            <div class="title-box"><i class="fab fa-aws"></i> Aws Save </div>
            <div class="box">
              <p>Save in aws</p>
              <input type="text" df-db-dbname placeholder="DB name"><br><br>
              <input type="text" df-db-key placeholder="DB key">
              <p>Output Log</p>
            </div>
          </div>
          """

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
