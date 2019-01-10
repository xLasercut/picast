from flask import request, jsonify
from picast import app
from picast.exceptions import InvalidRequest
from picast.services import StreamService, VolumeService, SeekService, ControlService
import re

@app.route("/status", methods=["GET"])
def statusHandler():
    return jsonify("OK"), 200


@app.route("/stream", methods=["POST"])
def streamHandler():
    try:
        streamService = StreamService(request)
        streamService.validateRequest()
        streamService.runCommand()
        return "ok", 200
    except InvalidRequest as e:
        return e.sendErrorResponse()


@app.route("/volume", methods=["POST"])
def volumeHandler():
    try:
        volumeService = VolumeService(request)
        volumeService.validateRequest()
        volumeService.runCommand()
        return "OK", 200
    except InvalidRequest as e:
        return e.sendErrorResponse()


@app.route("/seek", methods=["POST"])
def seekHandler():
    try:
        seekService = SeekService(request)
        seekService.validateRequest()
        seekService.runCommand()
        return "OK", 200
    except InvalidRequest as e:
        return e.sendErrorResponse()

@app.route("/control", methods=["POST"])
def controlHandler():
    try:
        controlService = ControlService(request)
        controlService.validateRequest()
        controlService.runCommand()
        return "OK", 200
    except InvalidRequest as e:
        return e.sendErrorResponse()
