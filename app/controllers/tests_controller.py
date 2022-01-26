import json
from flask import Blueprint, jsonify, make_response, request
from flasgger import Swagger
from flasgger.utils import swag_from

from dependency_injector.wiring import inject, Provide

import sys
import os

from marshmallow.fields import Number
sys.path.append(os.getcwd() + '../')

from services.tests_service import TestsService
from alchemy.common.jsonEncoder import AlchemyEncoder
from container import Container

testsControllerBlueprint = Blueprint('TestsController', __name__)

@testsControllerBlueprint.route('/<id>', methods=['GET'])
@inject
def getTest(_testsService: TestsService = Provide[Container._testsService]):
    """
    Get all test records
    An endpoint which returns one test record by ID
    ---  
    tags:
        - Tests Controller
    responses:
        200:
            description: Success
            schema:
                type: array
                items: 
                    type: object
                    properties:
                        id:
                            type: int
                            description: The identifier of the test record
                        name:
                            type: string
                        description:
                            type: string 
                example: {"id": 1, "name": "name 1", "description": "description 1"}
        404:
            description: Not Found
        500:
            description: Internal Server Error
    """
    queryResult = _testsService.getTest(id)
    statusCode = 200
    if queryResult == None:
        statusCode = 404
    response = make_response(json.dumps(queryResult, cls=AlchemyEncoder), 404)
    response.headers["Content-Type"] = "application/json"
    return response

@testsControllerBlueprint.route('', methods=['POST'])
@inject
def getTests(_testsService: TestsService = Provide[Container._testsService]):
    """
    An endpoint which returns all test records
    ---  
    tags:
        - Tests Controller
    responses:
        200:
            description: Success
            schema:
                type: array
                items: 
                    type: object
                    properties:
                        id:
                            type: int
                            description: The identifier of the test record
                        name:
                            type: string
                        description:
                            type: string 
                example: [{"id": 1, "name": "name 1", "description": "description 1"}, {"id": 2, "name": "name 2", "description": "description 2"}]
        204:
            description: No Content
        500:
            description: Internal Server Error
    """

    queryResult = _testsService.getTests()
    httpStatusCode = 200
    if len(queryResult) == 0:        
        httpStatusCode = 204
        
    response = make_response(json.dumps(queryResult, cls=AlchemyEncoder),httpStatusCode)
    response.headers["Content-Type"] = "application/json"
    return response

@testsControllerBlueprint.route('', methods=['PUT'])
@inject
def addTest(_testsService: TestsService = Provide[Container._testsService]):
    """
    Adds a new test record to the DB
    ---  
    tags:
        - Tests Controller
    parameters:
      - in: body
        name: body
        required: true
        schema:
            type: object
            properties:
                name:
                    type: string
                description: 
                    type: string
    responses:                    
        200:
            description: Success
        500:
            description: Internal Server Error    
    """

    query = request.json
    responseId = _testsService.addTest(query)
    response = make_response(json.dumps(responseId, cls=AlchemyEncoder),200)
    response.headers["Content-Type"] = "application/json"
    return response

