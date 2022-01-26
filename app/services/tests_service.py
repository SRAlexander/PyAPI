import datetime
import json
import sqlalchemy
import urllib

from dependency_injector.wiring import inject, Provide
from marshmallow import Schema, fields, ValidationError, pre_load

import sys
import os
sys.path.append(os.getcwd() + '/..')

from repositorys.tests_repository import TestsRepository
from alchemy.tables.test_definition import TestDefinition
from alchemy.schemas.test_definition_schema import TestDefinitionSchema

class TestsService:

    @inject
    def __init__(self, testsRepository : TestsRepository):
        self._testsRepository = testsRepository

    def getTest(self, id):
        result = self._rulesRepository.getRule(id)
        if (result is None):
            return None

        responseModel: TestDefinitionSchema = TestDefinitionSchema()
        response = responseModel.dump(result)
        return response

    def getTests(self):
        results = self._testsRepository.getTests()
        responses = []
        for result in results:
            responseModel: TestDefinitionSchema = TestDefinitionSchema()
            response = responseModel.dump(result)
            responses.append(response)
             
        return responses
    
    def addTest(self, query):
        
        if not query["name"]:
            raise ValidationError("Name has not been provided")
        
        if not query["description"]:
            raise ValidationError("Description has not been provided")

        testDefinition : TestDefinition = TestDefinition()

        testDefinition.name = query["name"]
        testDefinition.description = query["description"]
        self._testsRepository.addTest(testDefinition)
        return
        
        

        