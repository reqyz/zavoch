from zavoch.protocols import PipelineManager, QueueManager, ConfigManager, ConfigConsumer


class NatsConfigManager(ConfigConsumer, ConfigManager):

    async def get_config(self):
        return await super().get_config()

    async def create_config(self):
        return await super().create_config()

    async def update_config(self):
        return await super().update_config()


class NatsPipelineManager(PipelineManager):

    async def create_pipeline(self):
        return await super().create_pipeline()

    async def update_pipeline(self):
        return await super().update_pipeline()

    async def delete_pipeline(self):
        return await super().delete_pipeline()


class NatsQueueManger(QueueManager):
    async def create_queue(self):
        return await super().create_queue()

    async def update_queue(self):
        return await super().update_queue()

    async def delete_queue(self):
        return await super().delete_queue()
