from components.base.drawflownodebase import DrawflowNodeBase
from uuid import UUID

class MultipleIONode(DrawflowNodeBase):
    def __init__(self):
        super().__init__()

        self.name('multiple')
        self.title("Multiple inputs / outputs")

        self.input("Name", str)
        self.input("Age", int)
        self.input("ID", UUID)

        self.output("Friends", list())
        self.output("Groups", list())
        self.output("Projects", list())
        self.output("isHappy", bool)

        self.icon('fas fa-code-branch')
        self.html("""<div><div class="box">Multiple!</div></div>""")
