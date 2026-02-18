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