# Pipeline for Stabilizing a Double Inverted Pendulum

## Step 1 — System Understanding and Data Acquisition

The first step is to understand the dynamics of a double inverted pendulum system and to acquire the angular states of the system, specifically the base and the segment link angle, like show bellow.

- Base → First link angle (θ₁)  
- First link → Second link angle (θ₂)

However, these angles should **not** be used directly in their raw form when building a dataset for machine learning or artificial intelligence (A.I.) models, because de dois motivos: a redundância dos valores de seno ou cosseno a repseito de um mesmo valor angular geram confusão a respeito da parte trigonométrica equivalente em que o pêndulo efetivamente se encontra, por exemplo:

- 30°  -> 1/2 or 0.5
- 150° -> 1/2 or 0.5

Thus, in order to address this problem, the sine and cosine values are used for any acquired angle to avoid angular ambiguities. In addition, there is also a crucial need to avoid an angle wrapping discontinuity, since in a numerical dataset the transition between angles may introduce an artificial discontinuity, as shown in the example below.

- θ = 0° ≠ 360° ≠ 720

Even that trignomnumerically this is the same point in unity circle of trignometric, numerically, this appears as a large jump, even though the physical motion is smooth. This phenomenon is known as angle wrapping, and it can negatively affect the training of AI models because it introduces non-continuous state representations like the figure bwllow represents.

<img width="1000" height="600" alt="Figure_1_Graph_Angle_Inverted_Pendulum_Representation" src="https://github.com/user-attachments/assets/2f8b2dd5-5249-4b2e-9cf5-d0dd7aa72863" />


### Solution: Trigonometric State Representation

To avoid this issue, each angular variable must be represented using:

- sin(θ)
- cos(θ)

This representation removes discontinuities caused by angle wrapping and preserves the natural periodicity of angular variables. By encoding angles using sine and cosine, the system orientation is represented continuously on the unit circle, which improves numerical stability and facilitates learning for neural networks and reinforcement learning models.

Thus, instead of storing:

θ₁, θ₂

we store:

sin(θ₁), cos(θ₁), sin(θ₂), cos(θ₂)

---

## Data Collection Using MuJoCo

The following script simulates the double inverted pendulum in MuJoCo and generates a dataset containing angular positions, angular velocities, and system energy according to the previously known and stipulated requirements.

```python
import mujoco
import mujoco.viewer
import numpy as np
import csv
import os
import time

MODEL_PATH = "double_inverted_pendulum.xml"
OUTPUT = "data/pendulum_dataset.csv"

EPISODES = 5
SIM_TIME = 10  # seconds per episode

# =========================
# Load model
# =========================
model = mujoco.MjModel.from_xml_path(MODEL_PATH)
data = mujoco.MjData(model)

os.makedirs("data", exist_ok=True)

# =========================
# State randomization
# =========================
def randomize_state():
    # Initial angles
    data.qpos[0] = np.random.uniform(-0.2, 0.2)
    data.qpos[1] = np.random.uniform(-0.2, 0.2)

    # Initial angular velocities
    data.qvel[0] = np.random.uniform(-1.0, 1.0)
    data.qvel[1] = np.random.uniform(-1.0, 1.0)

    mujoco.mj_forward(model, data)


# =========================
# System energy computation
# =========================
def compute_energy():
    kinetic = np.sum(data.qvel ** 2) * 0.5
    potential = data.energy[0] if hasattr(data, "energy") else 0
    return kinetic, potential


# =========================
# Dataset generation
# =========================
with open(OUTPUT, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "episode",
        "time",
        "theta1",
        "theta2",
        "omega1",
        "omega2",
        "kinetic_energy",
        "potential_energy"
    ])

    with mujoco.viewer.launch_passive(model, data) as viewer:

        print("Starting data collection...")

        for ep in range(EPISODES):

            print(f"Episode {ep+1}/{EPISODES}")

            mujoco.mj_resetData(model, data)
            randomize_state()

            start_time = data.time

            while viewer.is_running() and (data.time - start_time < SIM_TIME):

                step_start = time.time()

                mujoco.mj_step(model, data)

                theta1 = data.qpos[0]
                theta2 = data.qpos[1]

                omega1 = data.qvel[0]
                omega2 = data.qvel[1]

                kinetic, potential = compute_energy()

                writer.writerow([
                    ep,
                    data.time,
                    theta1,
                    theta2,
                    omega1,
                    omega2,
                    kinetic,
                    potential
                ])

                viewer.sync()

                # Maintain real-time simulation
                time_until_next_step = model.opt.timestep - (time.time() - step_start)
                if time_until_next_step > 0:
                    time.sleep(time_until_next_step)

print("Dataset saved at:", OUTPUT)

## Step 2 - Data Visualization and tabulation
- Now, has been acquisitated data, we need see what wee have and transform the form to see this in a tablet form.
- The data has come to us is a .csv file, like a matrix, we have in the first column a epsode in wich the data has been acquisitation from model simulation. We separe in five generations, epsode 0 to 4. In the second column we have time of acquisition data, in wich has been do the data colletion from frequence aquisition. The third and fourth column was a angle values from sine and cossine about theta1, the same form the column five and six are sine and cossine from theta2. But all of this is just a .csv file, we need a tablet data. For this, we just need work with lines and columns in .csv file to do a tablet data file. But, before, is a good option see what happenned with your model, for this we can use the matplolib to generate a graph. So, let's do this and we can found a result like a figure bellow.

<img width="1000" height="600" alt="Figure_2_Graph_Four_Angles_Inverted_Pendulum_Representation" src="https://github.com/user-attachments/assets/fa68e844-6a84-4fad-a65f-29a85a515b5d" />

OMG!!! WHAT IS THIS????????? Calm down, friend. It's O.K., even if not seems xD. But, why this is so confuse and desorganizated? Well, why we have the four angles im same graph. If we separe this we will have a situation like bellow.

