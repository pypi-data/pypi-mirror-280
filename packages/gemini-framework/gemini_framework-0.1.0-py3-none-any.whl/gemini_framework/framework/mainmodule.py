from gemini_framework.framework.loop import Loop


class MainModule:
    plant = None
    modules = dict()
    loop = None

    def __init__(self, plant):
        self.plant = plant

        self.modules['preprocessor'] = plant.find_modules('preprocessor')
        self.modules['model'] = plant.find_modules('model')
        self.modules['postprocessor'] = plant.find_modules('postprocessor')

        self.loop = Loop()

        end_time = self.plant.databases[0].get_current_time_str()
        timestep = 900  # hardcoded to 15 minutes
        self.loop.initialize(end_time, timestep)

    def step(self):
        for database in self.plant.databases:
            # database.delete(self.plant.name)
            database.import_raw_data()

        for module in self.modules['preprocessor']:
            module.step(self.loop)

        for module in self.modules['model']:
            module.step(self.loop)

        for module in self.modules['postprocessor']:
            module.step(self.loop)
