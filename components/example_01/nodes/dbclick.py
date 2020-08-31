from components.base.drawflownodebase import DrawflowNodeBase


class DBClickNode(DrawflowNodeBase):
    name = "DBClick!"
    inputs = 1
    outputs = 1
    icon = 'fas fa-mouse'
    node = 'dbclick'
    nodehtml = """
            <div>
            <div class="title-box"><i class="fas fa-mouse"></i> Db Click</div>
              <div class="box dbclickbox" ondblclick="showpopup(event)">
                Db Click here
                <div class="modal" style="display:none">
                  <div class="modal-content">
                    <span class="close" onclick="closemodal(event)">&times;</span>
                    Change your variable {name} !
                    <input type="text" df-name>
                  </div>

                </div>
              </div>
            </div>
            """

    def getAsTuple(self):
        return (self.name, self.inputs, self.outputs, self.icon, self.node, self.nodehtml)
