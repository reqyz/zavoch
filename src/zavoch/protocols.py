from typing import Protocol


class ConfigConsumer(Protocol):

    async def get_config(self):
        ...


class ConfigManager(Protocol):

    async def create_config(self):
        ...

    async def update_config(self):
        ...


class PipelineManager(Protocol):

    async def create_pipeline(self):
        ...

    async def update_pipeline(self):
        ...

    async def delete_pipeline(self):
        ...


class QueueManager(Protocol):

    async def create_queue(self):
        ...

    async def update_queue(self):
        ...

    async def delete_queue(self):
        ...
