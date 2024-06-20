"""
Copyright (C) 2022-2024 Stella Technologies (UK) Limited.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""
import itertools
import json
from dataclasses import dataclass
from typing import Generator

import httpx
from keycloak import KeycloakError, KeycloakOpenID
from loguru import logger

from stellanow_cli.core.datatypes import StellaEntity, StellaEvent, StellaEventDetailed, StellaField
from stellanow_cli.core.decorators import make_stella_context_pass_decorator
from stellanow_cli.exceptions.api_exceptions import (
    StellaAPIForbiddenError,
    StellaAPINotFoundError,
    StellaAPIUnauthorisedError,
    StellaAPIWrongCredentialsError,
    StellaNowKeycloakCommunicationException,
)
from stellanow_cli.services.service import StellaNowService, StellaNowServiceConfig

CODE_GENERATOR_SERVICE_NAME = "code-generator-service"
OIDC_CLIENT_ID = "tools-cli"


@dataclass
class CodeGeneratorServiceConfig(StellaNowServiceConfig):
    base_url: str
    username: str
    password: str
    organization_id: str
    project_id: str


class CodeGeneratorService(StellaNowService):
    def __init__(self, config: CodeGeneratorServiceConfig) -> None:  # noqa
        self._config = config
        self.auth_token = None
        self.refresh_token = None
        self.keycloak = KeycloakOpenID(
            server_url=self._auth_url, client_id=OIDC_CLIENT_ID, realm_name=self._config.organization_id, verify=True
        )

        self.authenticate()

    @classmethod
    def service_name(cls) -> str:
        return CODE_GENERATOR_SERVICE_NAME

    @property
    def _auth_url(self):
        return f"{self._config.base_url}/auth/"

    @property
    def _events_url(self):
        return f"{self._config.base_url}/workflow-management/projects/{{projectId}}/events"

    @property
    def _event_url(self):
        return f"{self._config.base_url}/workflow-management/projects/{{projectId}}/events/{{eventId}}"

    def _handle_response(self, response):
        try:
            details = response.json().get("details", dict())
            if not isinstance(details, dict):
                details = dict()
        except json.JSONDecodeError:
            details = dict()

        match response.status_code:
            case 401:
                errors = details.get("errors", list())
                if not isinstance(errors, list):
                    errors = list()

                for error in errors:
                    match error.get("errorCode"):
                        case "inactiveAuthToken":
                            self.auth_refresh()
                            return
                        case "wrongUsernameOrPassword":
                            raise StellaAPIWrongCredentialsError()
                        case _:
                            raise StellaAPIUnauthorisedError(details)
                else:
                    response.raise_for_status()
            case 403:
                raise StellaAPIForbiddenError()
            case 404:
                raise StellaAPINotFoundError(details)
            case _:
                response.raise_for_status()

    def _get_token_response(self):
        try:
            return self.keycloak.token(username=self._config.username, password=self._config.password)
        except KeycloakError as exc:
            logger.info(exc)
            logger.error("operation failed")
            raise StellaNowKeycloakCommunicationException(details=exc)

    def authenticate(self):
        logger.info("Authenticating to the API ... ")

        if self.refresh_token is not None:
            self.auth_refresh()
        else:
            self.auth_token = None
            self.refresh_token = None

            response = self._get_token_response()

            self.auth_token = response.get("access_token")
            self.refresh_token = response.get("refresh_token")

        logger.info("Authentication Successful")

    def auth_refresh(self):
        if self.refresh_token is None:
            self.authenticate()
        else:
            logger.info("API Token Refreshing ...")

            refresh_token = self.refresh_token

            self.auth_token = None
            self.refresh_token = None

            response = self.keycloak.refresh_token(refresh_token)

            self.auth_token = response.get("password")
            self.refresh_token = response.get("refresh_token")

            logger.info("API Token Refresh Successful")

    def get_events(self) -> Generator[StellaEvent, None, None]:
        page_size = 100
        for page_number in itertools.count(1, 1):
            url = (
                self._events_url.format(projectId=self._config.project_id)
                + f"?page={page_number}&pageSize={page_size}&filter=IncludeInactive"
            )
            headers = {"Authorization": f"Bearer {self.auth_token}"}

            response = httpx.get(url, headers=headers)
            self._handle_response(response)

            events = response.json().get("details", dict()).get("results", [])
            if not events:
                break

            yield from (
                StellaEvent(
                    id=event.get("id"),
                    name=event.get("name"),
                    isActive=event.get("isActive"),
                    createdAt=event.get("createdAt"),
                    updatedAt=event.get("updatedAt"),
                )
                for event in events
            )

    def get_event_details(self, event_id: str) -> StellaEventDetailed:
        url = self._event_url.format(projectId=self._config.project_id, eventId=event_id)
        headers = {"Authorization": f"Bearer {self.auth_token}"}

        response = httpx.get(url, headers=headers)
        self._handle_response(response)

        details = response.json().get("details", dict())
        logger.info(details)

        # create StellaEntity objects from the 'entities' list
        entities = [StellaEntity(**entity) for entity in details.get("entities", list())]

        # create StellaField objects from the 'fields' list
        fields = [StellaField(**field) for field in details.get("fields", list())]

        # create and return StellaEventDetailed object
        return StellaEventDetailed(
            id=details.get("id"),
            name=details.get("name"),
            description=details.get("description"),
            isActive=details.get("isActive"),
            createdAt=details.get("createdAt"),
            updatedAt=details.get("updatedAt"),
            fields=fields,
            entities=entities,
        )


pass_code_generator_service = make_stella_context_pass_decorator(CodeGeneratorService)
