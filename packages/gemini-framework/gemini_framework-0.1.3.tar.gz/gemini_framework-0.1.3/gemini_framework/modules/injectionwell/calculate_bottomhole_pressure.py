from gemini_framework.abstract.unit_module_abstract import UnitModuleAbstract
from gemini_model.well.vertical_lift_curve import VLP


class CalculateBottomholePressure(UnitModuleAbstract):

    def __init__(self, unit):
        super().__init__(unit)

        self.model = VLP()
        self.model.update_parameters(unit.parameters)

    def step(self, timestamp):
        pass
