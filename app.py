from flask import Flask, redirect, url_for, render_template, request, session
from flask import jsonify

import json
import sys
import os
from os import listdir

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/examples/01', methods=['GET', 'POST'])
def example_01():
    avail_nodes = list()
    avail_nodes.append(('Facebook', 'fab fa-facebook', 'facebook', '<div><div class="title-box"><i class="fab fa-facebook"></i> Facebook Message</div></div>'))
    avail_nodes.append(('Slack recive message', 'fab fa-slack', 'slack', '<div><div class="title-box"><i class="fab fa-slack"></i> Slack chat message</div></div>'))
    avail_nodes.append(('Github Star', 'fab fa-github', 'github',"""
          <div>
            <div class="title-box"><i class="fab fa-github "></i> Github Stars</div>
            <div class="box">
              <p>Enter repository url</p>
            <input type="text" df-name>
            </div>
          </div>
          """))
    avail_nodes.append(('Telegram send message', 'fab fa-telegram', 'telegram', """
          <div>
            <div class="title-box"><i class="fab fa-telegram-plane"></i> Telegram bot</div>
            <div class="box">
              <p>Send to telegram</p>
              <p>select channel</p>
              <select df-channel>
                <option value="channel_1">Channel 1</option>
                <option value="channel_2">Channel 2</option>
                <option value="channel_3">Channel 3</option>
                <option value="channel_4">Channel 4</option>
              </select>
            </div>
          </div>
          """))
    avail_nodes.append(('AWS', 'fab fa-aws', 'aws', """
          <div>
            <div class="title-box"><i class="fab fa-aws"></i> Aws Save </div>
            <div class="box">
              <p>Save in aws</p>
              <input type="text" df-db-dbname placeholder="DB name"><br><br>
              <input type="text" df-db-key placeholder="DB key">
              <p>Output Log</p>
            </div>
          </div>
          """))
    avail_nodes.append(('File Log', 'fas fa-file-signature', 'log', '<div><div class="title-box"><i class="fas fa-file-signature"></i> Save log file </div></div>'))
    avail_nodes.append(('Google Drive save', 'fab fa-google-drive', 'google', '<div><div class="title-box"><i class="fab fa-google-drive"></i> Google Drive save </div></div>'))
    avail_nodes.append(('Email send', 'fas fa-at', 'email', '<div><div class="title-box"><i class="fas fa-at"></i> Send Email </div></div>'))
    avail_nodes.append(('Template', 'fas fa-code', 'template', """
            <div>
              <div class="title-box"><i class="fas fa-code"></i> Template</div>
              <div class="box">
                Ger Vars
                <textarea df-template></textarea>
                Output template with vars
              </div>
            </div>
            """))
    avail_nodes.append(('Multiple inputs / outputs', 'fas fa-code-branch', 'multiple', '<div><div class="box">Multiple!</div></div>'))
    avail_nodes.append(('Personalized', 'fas fa-fill', 'personalized', '<div>Personalized</div>'))
    avail_nodes.append(('DBClick!', 'fas fa-mouse', 'dbclick', """
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
            """))

    return render_template('example_01.html', files=listdir('templates'), avail_nodes=avail_nodes)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)  # Random key for dev purposes
    app.run()
