from typing import Optional

from nestipy.common import Module
from nestipy.dynamic_module import DynamicModule

from .jwt_builder import ConfigurableModuleClass, JwtOption
from .jwt_service import JwtService


@Module(
    providers=[
        JwtService
    ],
    exports=[
        JwtService
    ]
)
class JwtModule(ConfigurableModuleClass):
    @classmethod
    def for_root(cls, option: Optional[JwtOption] = None) -> DynamicModule:
        dynamic_module: DynamicModule = super().for_root(option or JwtOption(secret="nestipy_secret_key"))
        if option and option.is_global:
            dynamic_module.is_global = option.is_global
        return dynamic_module
