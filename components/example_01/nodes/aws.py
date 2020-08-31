from components.base.drawflownodebase import DrawflowNodeBase


class AWSNode(DrawflowNodeBase):
    def __init__(self):
        self.name('aws')
        self.title("AWS")
        self.input("input1", str)
        self.output("output1", str)
        self.icon('fab fa-aws')
        self.nodehtml("""
          <div>
            <div class="title-box"><i class="fab fa-aws"></i> Aws Save </div>
            <div class="box">
              <p>Save in aws</p>
              <input type="text" df-db-dbname placeholder="DB name"><br><br>
              <input type="text" df-db-key placeholder="DB key">
              <p>Output Log</p>
            </div>
          </div>
          """)
