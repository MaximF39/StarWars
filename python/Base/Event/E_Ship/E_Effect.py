

class E_Effect:
    effects: list

    def get_effect(self, effect_type, active_time):
        if effect_type in self.effects:
            for k, v in self.effects:
                if effect_type == k:
                    self.effects[k] += active_time
                    self.start_timer_update(self.remove_effect, active_time)

    def remove_effect(self, effect_type):
        for effect in self.effects:
            if effect.effectType == effect_type:
                self.effects.remove(effect)
        self.PacMan.effectRemoved(effect_type)

    def add_effect(self, EffectClass):
        self.effects.append(EffectClass)
        self.PacMan.effectCreated(EffectClass.effect['effectType'])
        self.start_timer_update(self.remove_effect, EffectClass.effect["effectTime"] / 1000,
                                args=(EffectClass.effect["effectType"],))
