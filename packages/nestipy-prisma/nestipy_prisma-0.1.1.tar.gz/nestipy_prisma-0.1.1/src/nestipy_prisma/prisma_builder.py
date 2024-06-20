import dataclasses
from datetime import timedelta

from nestipy.dynamic_module import ConfigurableModuleBuilder
from prisma._constants import DEFAULT_CONNECT_TIMEOUT
from prisma.types import DatasourceOverride, HttpConfig


@dataclasses.dataclass
class PrismaOption:
    use_dotenv: bool = True
    log_queries: bool = False
    auto_register: bool = False
    datasource: DatasourceOverride | None = None
    connect_timeout: int | timedelta = DEFAULT_CONNECT_TIMEOUT
    http: HttpConfig | None = None


ConfigurableModuleClass, PRISMA_OPTION = ConfigurableModuleBuilder[PrismaOption]().build()
