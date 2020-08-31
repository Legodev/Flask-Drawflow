from components.base.drawflownodebase import DrawflowNodeBase


class DBClickNode(DrawflowNodeBase):
    def __init__(self):
        super().__init__()

        self.name('dbclick')
        self.title("DBClick!")
        self.input("Input1", str)
        self.output("Output1", str)
        self.icon('fas fa-mouse')
        self.html("""
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
                """)
