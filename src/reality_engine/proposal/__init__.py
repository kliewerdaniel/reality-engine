class Proposal:
    def __init__(self, **kw):
        self.__dict__.update(kw)

class ModelProvider:
    def generate(self, prompt):
        return ""

class OllamaProvider(ModelProvider):
    def __init__(self, enabled=False):
        self.enabled = enabled
    def generate(self, prompt):
        if not self.enabled:
            return ""
        return ""

class ClaimProposer:
    def propose(self, entity, observations):
        return []

class RuleBasedProposer(ClaimProposer):
    def propose(self, entity, observations):
        return []
