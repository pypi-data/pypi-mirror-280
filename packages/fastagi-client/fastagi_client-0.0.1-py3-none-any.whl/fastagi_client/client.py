from typing import Any

from pydantic import validate_arguments

from fastagi_client.lib.auth import validate_api_key
from fastagi_client.lib.fastagi import Fastagi
from fastagi_client.types import *


class Client:
    def __init__(
        self,
        api_key: str,
        url: Optional[str] = "https://app.fastagi.khulnasoft.com",
        fastagi=None,
        **kwargs: Any,
    ):
        """
        Initialize the Client.

        Args:
            api_key: The API key for authentication.
            url: The URL of the Fastagi service.
            fastagi: An instance of the Fastagi class.
            **kwargs: Additional keyword arguments.
        """
        self.api_key = api_key
        self.url = url
        self.fastagi = None

        validate_api_key(base_url=f"{self.url}", api_key=self.api_key)

        if fastagi is None:
            fastagi = Fastagi(base_url=self.url, api_key=self.api_key)
        self.fastagi = fastagi

    @validate_arguments
    def create_agent(self, agent_config: AgentConfig):
        """
        Create a new agent.

        Args:
            agent_config: The configuration for the new agent.

        Returns:
            A dictionary containing the ID of the newly created agent.
        """
        response = self.fastagi.create_agent(agent_config=agent_config)
        return response

    @validate_arguments
    def update_agent(self, agent_id: int, agent_update_config: AgentUpdateConfig):
        """
        Update an existing agent.

        Args:
            agent_id: The ID of the agent to update.
            agent_update_config: The new configuration for the agent.

        Returns:
            A dictionary containing the ID of the updated agent.
        """
        response = self.fastagi.update_agent(
            agent_id=agent_id, agent_update_config=agent_update_config
        )
        return response

    @validate_arguments
    def pause_agent(self, agent_id: int, agent_run_ids: Optional[List[int]] = None):
        """
        Pause an agent.

        Args:
            agent_id: The ID of the agent to pause.
            agent_run_ids: The IDs of the agent runs to pause.

        Returns:
            A dictionary indicating whether the operation was successful.
        """
        response = self.fastagi.pause_agent(
            agent_id=agent_id, agent_run_ids=agent_run_ids
        )
        return response

    @validate_arguments
    def resume_agent(self, agent_id: int, agent_run_ids: Optional[List[int]] = None):
        """
        Resume an agent.

        Args:
            agent_id: The ID of the agent to resume.
            agent_run_ids: The IDs of the agent runs to resume.

        Returns:
            A dictionary indicating whether the operation was successful.
        """
        response = self.fastagi.resume_agent(
            agent_id=agent_id, agent_run_ids=agent_run_ids
        )
        return response

    @validate_arguments
    def create_agent_run(self, agent_id: int, agent_run: Optional[AgentRun] = None):
        """
        Create a new agent run.

        Args:
            agent_id: The ID of the agent to run.
            agent_run: The configuration for the new agent run.

        Returns:
            A dictionary containing the ID of the newly created agent run.
        """
        response = self.fastagi.create_agent_run(
            agent_id=agent_id, agent_run=agent_run
        )
        return response

    @validate_arguments
    def get_agent_run_status(
        self, agent_id: int, agent_run_filter: Optional[AgentRunFilter] = None
    ):
        """
        Get the status of an agent run.

        Args:
            agent_id: The ID of the agent.
            agent_run_filter: The filter to apply to the agent runs.

        Returns:
            A list of dictionaries containing the run IDs and their statuses.
        """
        response = self.fastagi.get_agent_run_status(
            agent_id=agent_id, agent_run_filter=agent_run_filter
        )
        return response

    @validate_arguments
    def get_agent_run_resources(self, agent_run_ids: List[int]):
        """
        Get the resources of an agent run.

        Args:
            agent_run_ids: The IDs of the agent runs.

        Returns:
            A dictionary containing the run IDs and their associated resources.
        """
        response = self.fastagi.get_agent_run_resources(agent_run_ids=agent_run_ids)
        return response
