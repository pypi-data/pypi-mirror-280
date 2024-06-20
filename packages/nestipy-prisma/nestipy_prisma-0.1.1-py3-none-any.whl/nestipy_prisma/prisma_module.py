from typing import Optional

from nestipy.common import Module
from nestipy.dynamic_module import DynamicModule

from .prisma_builder import ConfigurableModuleClass, PrismaOption
from .prisma_service import PrismaService


@Module(
    providers=[PrismaService],
    exports=[PrismaService],
    is_global=True
)
class PrismaModule(ConfigurableModuleClass):

    @classmethod
    def for_root(cls, option: Optional[PrismaOption] = None) -> DynamicModule:
        return cls.register(option or PrismaOption())
