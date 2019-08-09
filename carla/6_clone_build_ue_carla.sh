git clone --depth=1 -b 4.22 https://github.com/EpicGames/UnrealEngine.git ~/UnrealEngine_4.22 && \
cd ~/UnrealEngine_4.22 && \
./Setup.sh && ./GenerateProjectFiles.sh && make && \
export UE4_ROOT=~/UnrealEngine_4.22 && \
git clone https://github.com/carla-simulator/carla ~/carla && \
cd ~/carla && \
./Update.sh && \
make launch && \    # Compiles the simulator and launches Unreal Engine's Editor.
make PythonAPI && \  # Compiles the PythonAPI module necessary for running the Python examples.
make package &&\   # Compiles everything and creates a packaged version able to run without UE4 editor.
make help &&\      # Print all available commands.

