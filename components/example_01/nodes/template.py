from components.base.drawflownodebase import DrawflowNodeBase


class TemplateNode(DrawflowNodeBase):
    def __init__(self):
        self.name('template')
        self.title('Template')
        self.input('Input1', int)
        self.output('Output1', str)
        self.icon('fas fa-code')
        self.nodehtml("""
                <div>
                  <div class="title-box"><i class="fas fa-code"></i> Template</div>
                  <div class="box">
                    Ger Vars
                    <textarea df-template></textarea>
                    Output template with vars
                  </div>
                </div>
                """)
