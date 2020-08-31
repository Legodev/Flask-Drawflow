from flask import Flask, redirect, url_for, render_template, request, session
from flask import jsonify

import json
import sys
import os
from os import listdir
from components.example_01.nodes import aws, dbclick, email, facebook, github, google, log, multiple, personalized, slack, telegram, template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/examples/01', methods=['GET', 'POST'])
def example_01():
    avail_nodes = list()

    avail_nodes.append(facebook.FacebookNode().getAsTuple())
    avail_nodes.append(slack.SlackNode().getAsTuple())
    avail_nodes.append(github.GithubNode().getAsTuple())
    avail_nodes.append(telegram.TelegramNode().getAsTuple())
    avail_nodes.append(aws.AWSNode().getAsTuple())
    avail_nodes.append(log.FileLogNode().getAsTuple())
    avail_nodes.append(google.GoogleDriveSaveNode().getAsTuple())
    avail_nodes.append(email.EmailSendNode().getAsTuple())
    avail_nodes.append(template.TemplateNode().getAsTuple())
    avail_nodes.append(multiple.MultipleIONode().getAsTuple())
    avail_nodes.append(personalized.PersonalizedNode().getAsTuple())
    avail_nodes.append(dbclick.DBClickNode().getAsTuple())

    return render_template('example_01.html', files=listdir('templates'), avail_nodes=avail_nodes)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)  # Random key for dev purposes
    app.run()

"""
import fab
import math

title('Cylinder (X)')

input('xmin', float)
input('xmax', float)
input('y', float)
input('z', float)
input('r', float)

output('shape', fab.shapes.cylinder_x(xmin, xmax, y, z, r))

# UI
sb.ui.wireframe([(xmin, y, z), (xmax, y, z)])
sb.ui.wireframe([(xmin, y, z), (xmin, y, z + r)])

sb.ui.wireframe([
    (xmin, math.cos(i/36. * 2*math.pi) * r + y,
     math.sin(i/36. * 2*math.pi) * r + z)
    for i in range(36)], close=True)

sb.ui.wireframe([
    (xmax, math.cos(i/36. * 2*math.pi) * r + y,
     math.sin(i/36. * 2*math.pi) * r + z)
    for i in range(36)], close=True)

sb.ui.point(xmin, y, z)
sb.ui.point(xmax, y, z)
sb.ui.point(xmin, y, z + r, drag=(None, None, r))

"""