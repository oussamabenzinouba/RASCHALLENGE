import random
import matplotlib.pyplot as plt

class DrivingSimulation:
    def __init__(self):
        self.points = 0
        self.traffic_signs = ['Stop', 'Speed Limit 50', 'Yield']
        self.points_history = []

    def simulate_drive(self, days):
        for _ in range(days):
            distance_driven = random.randint(20, 50)
            traffic_signs_disregarded = random.randint(1, 3)
            speed_limit_respected = random.uniform(0, 1) > 0.3  # 70% chance of respecting speed limit
            seat_belt_used = random.uniform(0, 1) > 0.4  # 60% chance of using seat belt

            # Simulate disregarding traffic signs
            for _ in range(traffic_signs_disregarded):
                self.points -= 3

            # Simulate driving and checking speed limit
            for _ in range(distance_driven):
                if not speed_limit_respected:
                    self.points -= 5
                else:
                    self.points += 3

            # Simulate seat belt usage
            for _ in range(2):  # twice a day
                if seat_belt_used:
                    self.points += 4
                else:
                    self.points -= 5

            self.points_history.append(self.points)

    def plot_points(self):
        plt.plot(self.points_history)
        plt.title('Annual Collection of Points')
        plt.xlabel('Days')
        plt.ylabel('Points')
        plt.show()

# Run the simulation for 365 days (one year)
simulation = DrivingSimulation()
simulation.simulate_drive(365)

# Plot the points over the year
simulation.plot_points()
