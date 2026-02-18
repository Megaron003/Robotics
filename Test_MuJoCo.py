import mujoco
import mujoco.viewer
import os

# CAMINHO CORRETO baseado onde você está
caminho_completo = r"C:\Users\Guilherme\Desktop\VS Code\MuJoCo\mujoco_menagerie\unitree_h1\scene.xml"

# Verificar se o arquivo existe
if os.path.exists(caminho_completo):
    print(f"✅ Arquivo encontrado: {caminho_completo}")
    
    # Carregar modelo
    model = mujoco.MjModel.from_xml_path(caminho_completo)
    data = mujoco.MjData(model)
    
    print(f"\n📊 Informações do H1:")
    print(f"  - Corpos: {model.nbody}")
    print(f"  - Juntas: {model.njnt}")
    print(f"  - Atuadores: {model.nu}")
    
    # Visualizar
    with mujoco.viewer.launch_passive(model, data) as viewer:
        print("\n🎮 H1 rodando! ESC para sair")
        print("Use mouse para controlar câmera")
        
        while viewer.is_running():
            mujoco.mj_step(model, data)
            viewer.sync()
            
else:
    print(f"❌ Arquivo NÃO encontrado: {caminho_completo}")
    
    # Listar arquivos no diretório atual para debug
    print("\n📁 Arquivos no diretório atual:")
    for arquivo in os.listdir('.'):
        print(f"  - {arquivo}")