# A Pipeline to how do a double interted pendulum be stable


## First
- You need understand a double inverted pendulum problem system.


´´´

import mujoco
import mujoco.viewer
import csv
import os
import time

MODEL_PATH = "double_inverted_pendulum.xml"
OUTPUT = "data/pendulum_dataset.csv"

model = mujoco.MjModel.from_xml_path(MODEL_PATH)
data = mujoco.MjData(model)

#Inclinação inicial para o pêndulo cair
data.qpos[0] = 0.2
data.qpos[1] = -0.1

theta1_addr = model.jnt_qposadr[0]
theta2_addr = model.jnt_qposadr[1]

os.makedirs("data", exist_ok=True)

with open(OUTPUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "theta1", "theta2"])

    #Abrir visualizador
    with mujoco.viewer.launch_passive(model, data) as viewer:

        print("Simulação iniciada...")

        while viewer.is_running():

            step_start = time.time()

            mujoco.mj_step(model, data)

            theta1 = data.qpos[theta1_addr]
            theta2 = data.qpos[theta2_addr]

            writer.writerow([
                data.time,
                theta1,
                theta2
            ])

            viewer.sync()

            #manter tempo real
            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)

print("Simulação finalizada!")

´´´