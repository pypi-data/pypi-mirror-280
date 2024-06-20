from typing import Annotated
from dataclasses import asdict
from nestipy.common import Injectable
from nestipy.core import OnInit, OnDestroy
from nestipy.ioc import Inject
from prisma import Prisma
from .prisma_builder import PrismaOption, PRISMA_OPTION


@Injectable()
class PrismaService(Prisma, OnInit, OnDestroy):
    def __init__(self, option: Annotated[PrismaOption, Inject(PRISMA_OPTION)]):
        super().__init__(**asdict(option))

    async def on_startup(self):
        await self.connect()

    async def on_shutdown(self):
        await self.disconnect()
