from flask import request
from picast import app
from picast.exceptions import InvalidRequest
from picast.services import StreamService, VolumeService, SeekService, ControlService, StatusService

@app.route('/status', methods=['POST'])
def statusHandler():
    try:
        statusService = StatusService(request)
        statusService.runWorkflow()
        return statusService.successResponse
    except InvalidRequest as e:
        return e.errorResponse


@app.route('/stream', methods=['POST'])
def streamHandler():
    try:
        streamService = StreamService(request)
        streamService.runWorkflow()
        return streamService.successResponse
    except InvalidRequest as e:
        return e.errorResponse


@app.route('/volume', methods=['POST'])
def volumeHandler():
    try:
        volumeService = VolumeService(request)
        volumeService.runWorkflow()
        return volumeService.successResponse
    except InvalidRequest as e:
        return e.errorResponse


@app.route('/seek', methods=['POST'])
def seekHandler():
    try:
        seekService = SeekService(request)
        seekService.runWorkflow()
        return seekService.successResponse
    except InvalidRequest as e:
        return e.errorResponse

@app.route('/control', methods=['POST'])
def controlHandler():
    try:
        controlService = ControlService(request)
        controlService.runWorkflow()
        return controlService.successResponse
    except InvalidRequest as e:
        return e.errorResponse
