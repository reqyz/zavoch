from pathlib import Path

from zavoch.protocols import ConfigConsumer, ConfigManager


class YamlConfigManager(ConfigConsumer, ConfigManager):

    def __init__(self, file_path: Path):
        self._file_path = file_path

    async def get_config(self):
        return await super().get_config()

    async def create_config(self):
        return await super().create_config()

    async def update_config(self):
        return await super().update_config()