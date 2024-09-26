class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.last_action = None

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        elif current_temperature >= self.desired_temperature and self.last_action == "Turn on heater":
            action = "Turn off heater"
        else:
            action = "No action needed" 

        self.last_action = action  
        return action

rooms = {"Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24}

desired_temperature = 22
model_based_agent = ModelBasedReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = model_based_agent.act(temperature)
    print("\n{}: Current temperature = {}°C. {}.".room, temperature, action)