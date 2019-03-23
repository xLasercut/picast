from flask import request
from picast import app
from picast.exceptions import InvalidRequest
from picast.services import StreamService, VolumeService, SeekService, ControlService, StatusService

streamService = StreamService()
volumeService = VolumeService()
seekService = SeekService()
controlService = ControlService()
statusService = StatusService()

@app.route('/status', methods=['POST'])
def statusHandler():
    try:
        statusService.runWorkflow(request)
        return statusService.successResponse
    except InvalidRequest as e:
        return e.errorResponse


@app.route('/stream', methods=['POST'])
def streamHandler():
    try:
        streamService.runWorkflow(request)
        return streamService.successResponse
    except InvalidRequest as e:
        return e.errorResponse


@app.route('/volume', methods=['POST'])
def volumeHandler():
    try:
        volumeService.runWorkflow(request)
        return volumeService.successResponse
    except InvalidRequest as e:
        return e.errorResponse


@app.route('/seek', methods=['POST'])
def seekHandler():
    try:
        seekService.runWorkflow(request)
        return seekService.successResponse
    except InvalidRequest as e:
        return e.errorResponse

@app.route('/control', methods=['POST'])
def controlHandler():
    try:
        controlService.runWorkflow(request)
        return controlService.successResponse
    except InvalidRequest as e:
        return e.errorResponse
