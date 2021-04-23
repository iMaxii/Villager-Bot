import sys

# fully reimplemented
import speedups.gateway
import speedups.mixins

# partial implementations
import speedups.activity
import speedups.message
import speedups.utils


def install():
    discord_module = sys.modules.get("discord")

    for module in (speedups.activity, speedups.message, speedups.utils):
        for thing in module.__all__:
            if hasattr(discord_module, thing):
                setattr(discord_module, thing, getattr(module, thing))

    # these two were fully reimplemented so just patch em on ez
    discord_module.gateway = speedups.gateway
    discord_module.mixins = speedups.mixins
