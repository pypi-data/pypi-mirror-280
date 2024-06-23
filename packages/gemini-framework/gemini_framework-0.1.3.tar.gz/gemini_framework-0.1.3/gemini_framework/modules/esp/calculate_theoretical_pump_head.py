from gemini_framework.abstract.unit_module_abstract import UnitModuleAbstract
from gemini_model.pump.esp import ESP


class CalculateTheoreticalPumpHead(UnitModuleAbstract):

    def __init__(self, unit):
        super().__init__(unit)

        self.model = ESP()

        self.link_input('measured', 'esp_flow')
        self.link_input('measured', 'esp_frequency')
        self.link_output('calculate', 'esp_pump_head')

    def step(self, loop):
        self.loop = loop
        self.loop.start_time = self.get_output_last_data_time('esp_pump_head')
        self.loop.compute_n_simulation()

        esp_param = dict()
        esp_param['no_stages'] = self.unit.parameters['esp_no_stage']
        esp_param['pump_name'] = self.unit.parameters['esp_type']

        self.model.update_parameters(esp_param)

        time, esp_flow = self.get_input_data('esp_flow')
        time, esp_frequency = self.get_input_data('esp_frequency')

        u = dict()
        esp_pump_head = []
        for ii in range(1, self.loop.n_step):
            u['pump_flow'] = esp_flow[ii] / 3600
            u['pump_freq'] = esp_frequency[ii]

            x = []
            self.model.calculate_output(u, x)

            y = self.model.get_output()

            esp_pump_head.append(y['pump_head'] / 1e5)

        if esp_pump_head:
            self.write_output_data('esp_pump_head', time, esp_pump_head)
