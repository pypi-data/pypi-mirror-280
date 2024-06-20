from gemini_model.model_abstract import Model
import os
import json

path = os.path.dirname(__file__)


class ESP(Model):
    """ Class of ESP

        Class to calculate ESP power, efficiency and head
    """

    def __init__(self):
        """ Model initialization
        """
        self.parameters = {}
        self.output = {}

    def update_parameters(self, parameters):
        """ To update model parameters

        Parameters
        ----------
        parameters: dict
            parameters dict as defined by the model
        """
        for key, value in parameters.items():
            self.parameters[key] = value

        self.get_coefficient(self.parameters['pump_name'])

    def initialize_state(self, x):
        """ generate an initial state based on user parameters """
        pass

    def update_state(self, u, x):
        """update the state based on input u and state x"""
        pass

    def calculate_output(self, u, x):
        """calculate output based on input u and state x"""
        # get input
        pump_freq = u['pump_freq']
        pump_flow = u['pump_flow']

        # calculate model
        pump_head = self.head_function(pump_flow, pump_freq)
        pump_power = self.power_function(pump_flow, pump_freq)
        pump_eff = self.efficiency_function(pump_flow, pump_head, pump_power)

        # write output
        self.output['pump_head'] = pump_head
        self.output['pump_power'] = pump_power
        self.output['pump_eff'] = pump_eff

    def get_output(self):
        """get output of the model"""
        return self.output

    def head_function(self, pump_flow, freq):
        """ Function to calculate ESP power based on pump correlation in US unit"""
        pump_flow = pump_flow * 543439.650564  # m3/s to bbl/d

        head = self.parameters['no_stages'] * ((freq / 60) ** 2) * (
                self.parameters['hC0'] +
                self.parameters['hC1'] * pump_flow +
                self.parameters['hC2'] * (pump_flow ** 2) +
                self.parameters['hC3'] * (pump_flow ** 3) + self.parameters['hC4'] * (
                        pump_flow ** 4) +
                self.parameters['hC5'] * (pump_flow ** 5))
        return head * 2988.30167  # feet of head to Pa

    def power_function(self, pump_flow, freq):
        """ Function to calculate ESP power based on pump correlation in US unit"""
        pump_flow = pump_flow * 543439.650564  # m3/s to bbl/d

        pump_power = self.parameters['no_stages'] * ((freq / 60) ** 3) * (
                self.parameters['bC0'] +
                self.parameters['bC1'] * pump_flow +
                self.parameters['bC2'] * (pump_flow ** 2) +
                self.parameters['bC3'] * (pump_flow ** 3) +
                self.parameters['bC4'] * (pump_flow ** 4) +
                self.parameters['bC5'] * (pump_flow ** 5))

        return pump_power * 745.7  # brake horsepower to Watts

    def efficiency_function(self, pump_flow, pump_head, pump_power):
        """ Function to calculate ESP power based on pump correlation in US unit"""
        pump_flow = pump_flow * 543439.650564  # m3/s to bbl/d

        if pump_power < 0.1:
            pump_eff = 0
        else:
            pump_eff = 100 * pump_flow / 135773 * (pump_head / pump_power) * (
                    745.7 / 2988.30167)

        return pump_eff

    def get_coefficient(self, pump_type):
        with open(os.path.join(path, 'bin', 'pumpdatabase.json')) as jsonfile:
            pumpdatabase = json.load(jsonfile)

        for pump_data in pumpdatabase['data']:
            if pump_data['stagetype'] == pump_type:
                self.parameters['bC0'] = float(pump_data['bC0'])
                self.parameters['bC1'] = float(pump_data['bC1'])
                self.parameters['bC2'] = float(pump_data['bC2'])
                self.parameters['bC3'] = float(pump_data['bC3'])
                self.parameters['bC4'] = float(pump_data['bC4'])
                self.parameters['bC5'] = float(pump_data['bC5'])

                self.parameters['hC0'] = float(pump_data['hC0'])
                self.parameters['hC1'] = float(pump_data['hC1'])
                self.parameters['hC2'] = float(pump_data['hC2'])
                self.parameters['hC3'] = float(pump_data['hC3'])
                self.parameters['hC4'] = float(pump_data['hC4'])
                self.parameters['hC5'] = float(pump_data['hC5'])

                break
