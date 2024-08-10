import pyrogram
import sys
from atexit import register
from os import execl


def patch(obj):
    def is_patchable(item):
        return getattr(item[1], "patchable", False)

    def wrapper(container):
        for name, func in filter(is_patchable, container.__dict__.items()):
            old = getattr(obj, name, None)
            setattr(obj, "old_" + name, old)
            setattr(obj, name, func)
        return container

    return wrapper


def patchable(func):
    func.patchable = True
    return func


@patch(pyrogram.client.Client)
class Client:
    @patchable
    async def invoke(self, *args, **kwargs):
        try:
            return await self.old_invoke(*args, **kwargs)
        except OSError:
            def restart():
                execl(sys.executable, sys.executable, "-m", "cilik")

            register(restart)
            sys.exit(0)
