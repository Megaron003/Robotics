[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MuJoCo](https://img.shields.io/badge/MuJoCo-2.3.0-green.svg)](https://mujoco.org/)

# Robotics
Multi Robots information: models, .xml, codes, simulators and process



Let's start with a MuJoCo Test. Follow the instructions below, please and have fun ;)

## First
- Open your code interface (VS Code, Pycharm, etc) to install the MuJoCo lybrarie with pip.

`pip install mujoco`

## Second
- Now, to test the lybrarie, copy and paste the code below.

```
#Writed by Guilherme Vale - LSMR, UNICAMP

import mujoco
import mujoco.viewer
import numpy as np
import time

#XML do modelo - um pêndulo simples SEM atuador
XML = """
<mujoco model="pendulo_simples">
    <visual>
        <headlight ambient="0.4 0.4 0.4"/>
    </visual>
    
    <worldbody>
        <light name="top" pos="0 0 2"/>
        
        <!-- Fixo no teto -->
        <body name="fixo" pos="0 0 1">
            <geom type="sphere" size="0.1" rgba="0 0 1 1"/>
            <joint type="hinge" axis="0 1 0" name="pivot"/>
            
            <!-- Pêndulo -->
            <body name="pendulo" pos="0 0 -0.5">
                <geom type="capsule" fromto="0 0 0 0 0 -1" size="0.05" rgba="1 0 0 1"/>
                
                <!-- Massa na ponta -->
                <body name="massa" pos="0 0 -1">
                    <geom type="sphere" size="0.15" rgba="0 1 0 1"/>
                </body>
            </body>
        </body>
    </worldbody>
</mujoco>
"""

def main():
    # Criar o modelo e dados
    model = mujoco.MjModel.from_xml_string(XML)
    data = mujoco.MjData(model)
    
    # Definir posição inicial (45 graus)
    data.qpos[0] = 0.785  # 45 graus em radianos
    
    # Criar visualizador
    with mujoco.viewer.launch_passive(model, data) as viewer:
        print("Simulação rodando! Pressione ESC para sair")
        print("Você pode:")
        print("- Clicar e arrastar para rotacionar a câmera")
        print("- Scroll para dar zoom")
        print("- Clicar com botão direito e arrastar para mover a câmera")
        
        # Loop principal
        while viewer.is_running():
            step_start = time.time()
            
            # Avançar simulação (sem controle, só física)
            mujoco.mj_step(model, data)
            
            # Sincronizar visualização
            viewer.sync()
            
            # Manter tempo real (opcional)
            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)

if __name__ == "__main__":
    main()
```
- This is code to check the proper functioning of the library and allow the user (you) to see how the environment works and what it looks like.
- You can observeted that the .xml in the code are the descripition about the simple pendulum. For outers sistems and robots we need use others .xml archives, for example, Unitree H1 from Unitree [Official Unitree Robotics Repositore](https://github.com/unitreerobotics).

## Third
- All rigth, now, let's try it with a H1 biped robot .xml model from Unitree.
- First we need to do the download of models and meshes. Paste the informations below in your VS Code terminal or similar, please.

```
# Clone the entire Menagerie repository (recommended)
git clone https://github.com/google-deepmind/mujoco_menagerie.git

# go to the H1 file
cd mujoco_menagerie/unitree_h1

# Now you can use the H1 .xml with yours meshes.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MuJoCo](https://img.shields.io/badge/MuJoCo-2.3.0-green.svg)](https://mujoco.org/)

# Robotics
Multi Robots information: models, .xml, codes, simulators and process



Let's start with a MuJoCo Test. Follow the instructions below, please and have fun ;)

## First
- Open your code interface (VS Code, Pycharm, etc) to install the MuJoCo lybrarie with pip.

`pip install mujoco`

## Second
- Now, to test the lybrarie, copy and paste the code below.

```
#Writed by Guilherme Vale - LSMR, UNICAMP

import mujoco
import mujoco.viewer
import numpy as np
import time

#XML do modelo - um pêndulo simples SEM atuador
XML = """
<mujoco model="pendulo_simples">
    <visual>
        <headlight ambient="0.4 0.4 0.4"/>
    </visual>
    
    <worldbody>
        <light name="top" pos="0 0 2"/>
        
        <!-- Fixo no teto -->
        <body name="fixo" pos="0 0 1">
            <geom type="sphere" size="0.1" rgba="0 0 1 1"/>
            <joint type="hinge" axis="0 1 0" name="pivot"/>
            
            <!-- Pêndulo -->
            <body name="pendulo" pos="0 0 -0.5">
                <geom type="capsule" fromto="0 0 0 0 0 -1" size="0.05" rgba="1 0 0 1"/>
                
                <!-- Massa na ponta -->
                <body name="massa" pos="0 0 -1">
                    <geom type="sphere" size="0.15" rgba="0 1 0 1"/>
                </body>
            </body>
        </body>
    </worldbody>
</mujoco>
"""

def main():
    # Criar o modelo e dados
    model = mujoco.MjModel.from_xml_string(XML)
    data = mujoco.MjData(model)
    
    # Definir posição inicial (45 graus)
    data.qpos[0] = 0.785  # 45 graus em radianos
    
    # Criar visualizador
    with mujoco.viewer.launch_passive(model, data) as viewer:
        print("Simulação rodando! Pressione ESC para sair")
        print("Você pode:")
        print("- Clicar e arrastar para rotacionar a câmera")
        print("- Scroll para dar zoom")
        print("- Clicar com botão direito e arrastar para mover a câmera")
        
        # Loop principal
        while viewer.is_running():
            step_start = time.time()
            
            # Avançar simulação (sem controle, só física)
            mujoco.mj_step(model, data)
            
            # Sincronizar visualização
            viewer.sync()
            
            # Manter tempo real (opcional)
            time_until_next_step = model.opt.timestep - (time.time() - step_start)
            if time_until_next_step > 0:
                time.sleep(time_until_next_step)

if __name__ == "__main__":
    main()
```
- This is code to check the proper functioning of the library and allow the user (you) to see how the environment works and what it looks like.
- You can observeted that the .xml in the code are the descripition about the simple pendulum. For outers sistems and robots we need use others .xml archives, for example, Unitree H1 from Unitree [Official Unitree Robotics Repositore](https://github.com/unitreerobotics).

## Third
- All rigth, now, let's try it with a H1 biped robot .xml model from Unitree.
- First we need to do the download of models and meshes. Paste the informations below in your VS Code terminal or similar, please.

```
#Clone the entire Menagerie repository (recommended)
git clone https://github.com/google-deepmind/mujoco_menagerie.git

#go to the H1 file
cd mujoco_menagerie/unitree_h1

#Now you can use the H1 .xml with yours meshes.
```

## Fourth
- Now, with repository already cloned, we can test if are working good. Just copy and paste the coide below.

```
#Writed by Guilherme Vale - LSMR, UNICAMP.

import mujoco
import mujoco.viewer
import os

#The path where the cloned repository is located. It should be inside the folder where this code was pasted.
full_path = r"C:\Users\Guilherme\Desktop\VS Code\MuJoCo\mujoco_menagerie\unitree_h1\scene.xml"

#Archive existing verification
if os.path.exists(full_path):
    print(f"✅ Arquivo encontrado: {full_path}")
    
    # load model
    model = mujoco.MjModel.from_xml_path(full_path)
    data = mujoco.MjData(model)
    
    print(f"\n📊 Informations about H1:")
    print(f"  - Bodies: {model.nbody}")
    print(f"  - Joints: {model.njnt}")
    print(f"  - Actuators: {model.nu}")
    
    #Visualization
    with mujoco.viewer.launch_passive(model, data) as viewer:
        print("\n🎮 H1 running! ESC to quit.")
        print("use the mouse to camera control.")
        
        while viewer.is_running():
            mujoco.mj_step(model, data)
            viewer.sync()
            
else:
    print(f"❌ File not founded! ERROR 404!: {full_path}")
    
    # Listar arquivos no diretório atual para debug
    print("\n📁 Files in current path:")
    for file in os.listdir('.'):
        print(f"  - {file}")
```

## Agradecimentos Especiais 🤝

I would like thanks to **[Unitree Robotics](https://github.com/unitree)** for:

- 🤖 Opensource robots model to MuJoCo.
- 📚 Detail technique documentation.
- 💡 Inspiration for my master's and dreams.

Thank you, Unitree!

Visit the official perfil: [@Unitree](https://github.com/unitree)

## Agradecimentos Especiais 🤝

I would like thanks to **[Unitree Robotics](https://github.com/unitree)** for:

- 🤖 Opensource robots model to MuJoCo.
- 📚 Detail technique documentation.
- 💡 Inspiration for my master's and dreams.

Thank you, Unitree!

Visit the official perfil: [@Unitree](https://github.com/unitree)
