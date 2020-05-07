from .base import BaseResponse

class CreateHookResponse(BaseResponse):
    def get_hook_id(self):
        try:
            if self.get_message_key() == "createHookError":
                return None
        except KeyError:
            pass

        return self.get_field('hookID')

class DestroyHookResponse(BaseResponse):
    pass

class ListHooksResponse(BaseResponse):
    def get_hooks(self):
        hooks = []
        for hookXml in self.get_field("hooks")["hook"]:
            hooks.append(hookXml)

        return hooks
        
