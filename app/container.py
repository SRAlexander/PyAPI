from dependency_injector import containers, providers

from services.tests_service import TestsService
from repositorys.tests_repository import TestsRepository
from alchemy.common.session import AlchemySession


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    _alchemySession = providers.Factory(
        AlchemySession
    )

    # Repositorys
    _testsRepository = providers.Factory(
        TestsRepository,
        _alchemySession
    )

    # Services

    _testsService = providers.Factory(
        TestsService,
        _testsRepository
    )

#Add services, controllers and repositories


    


