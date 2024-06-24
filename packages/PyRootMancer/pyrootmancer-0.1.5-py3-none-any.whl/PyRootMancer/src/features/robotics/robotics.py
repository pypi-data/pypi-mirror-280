from sim_class import Simulation
from simple_pid import PID
from cv_pipeline import cv_pipeline

cv_pip = cv_pipeline()
sim = Simulation(num_agents=1)


image_path = sim.get_plate_image()

x_pid_controller = PID(Kp=7, Ki=0, Kd=0)
y_pid_controller = PID(Kp=7, Ki=0, Kd=0)
z_pid_controller = PID(Kp=7, Ki=0, Kd=0)

num_steps = 1000
df = cv_pip.main(image_path)


for i in range(len(df)):
    # Get the goal position for the current iteration
    goal_position = cv_pip.get_image_coordinates(df, i)

    # Set the PID setpoints
    x_pid_controller.setpoint = goal_position[0]
    y_pid_controller.setpoint = goal_position[1]
    z_pid_controller.setpoint = goal_position[2]

    for step in range(num_steps):
        pipette_position = sim.get_pipette_position(robotId=sim.robotIds[0])

        # PID actions based on the current pipette position
        x_action = x_pid_controller(pipette_position[0])
        y_action = y_pid_controller(pipette_position[1])
        z_action = z_pid_controller(pipette_position[2])

        # Check if it's the last step
        if step == num_steps - 1:
            drop = 1
        else:
            drop = 0

        # PID actions to the robot in the simulation
        # actions = [[x_action, y_action, z_action, drop]]
        actions = [[x_action, y_action, z_action, drop]]
        sim.apply_actions(actions)

        # simulation for one step
        sim.run(actions, num_steps=1)

        # current states of the robot
        robot_states = sim.get_states()['robotId_' + str(sim.robotIds[0])]

        # Print or log relevant information only when drop is 1
        if drop == 1:
            print(
                f"Iteration: {i + 1}, Step: {step + 1}, Pipette Position: {pipette_position}, Robot States: {robot_states}"
            )


if __name__ == "__main__":
    print(f"selected image is {image_path}")
