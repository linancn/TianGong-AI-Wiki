============
Installation
============

.. note::
    Before proceeding, ensure **Visual Studio Code (VSCode)** is installed on your system. If it's not set up yet, please follow our `VSCode guide <your_link_here>`_.


Create Project Directory
-----------------------

.. tabs::

   .. group-tab:: Windows

      For Windows users, opt for **WSL2 with Ubuntu 22.04** or **Debian**. For setup details, refer to our `WSL2 installation guide <your_link_here>`_.

      After setting up WSL2:

      1. Launch VSCode.
      2. Activate the Remote extension using one of the following methods:
         - Click on the green remote indicator in the bottom-left corner and select `Remote-WSL: New Window`.
         - Use the command palette (`Ctrl+Shift+P`) and run:
           ::
           
              Remote-WSL: New Window

      3. Once inside WSL, update the system's package list:
         ::
         
            sudo apt update

      4. Navigate to the chosen directory for the project:
         ::
         
            cd path/to/your/directory

   .. group-tab:: MacOS

      MacOS users, utilize the **Docker Dev Container**. For setup instructions, follow the `Dev Container Configuration Guide for MacOS <your_link_here>`_.

      After setting up the Dev Container:

      1. Launch VSCode.
      2. Connect to the Dev Container using one of the following methods:
         - Click on the green remote indicator in the bottom-left corner and select `Remote-Containers: Attach to Running Container...`.
         - Use the command palette (`Ctrl+Shift+P`) and run:
           ::
           
              Remote-Containers: Attach to Running Container...

      3. After attaching, navigate to your chosen directory for the project within VSCode's integrated terminal:
         ::
         
            cd path/to/your/directory

   .. group-tab:: Linux

      On Linux, either **Ubuntu** or **Debian** distributions are suitable.

      Setting up your environment:

      1. Launch VSCode directly.
      2. Open a terminal within VSCode.
      3. Update system packages:
         ::
         
            sudo apt update

      4. Navigate to your desired directory for the project:
         ::
         
            cd path/to/your/directory


Clone Git Repository
------------------------

1. In your chosen directory within VSCode's integrated terminal, execute the following command to clone the TianGong AI Chat repository:

   ::
       
      git clone https://github.com/linancn/TianGong-AI-Chat.git

2. After cloning, you have two options to open the project in VSCode:

   a. In the VSCode menu, select `File > Open Folder` and choose the `TianGong-AI-Chat` directory.

   b. Or, navigate into the project directory using the terminal:

   ::
       
      cd TianGong-AI-Chat

You should now have the TianGong AI Chat project files ready in your VSCode workspace.

Setup Project
-----------------
.. note::
    Before we start, you need to ensure that Python is installed on your system. If you have not installed Python yet, please refer to our `Python installation guide <your_python_installation_link_here>`_.

Setup Virtual Environment 
^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Create a virtual environment**: This step sets up an isolated Python environment in the current directory.

   .. code-block:: bash

      python3.11 -m venv .venv

2. **Activate the virtual environment**: Activating the environment ensures that the Python interpreter used is from this isolated environment.

   .. code-block:: bash

      source .venv/bin/activate

Install Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensuring that you have the right packages is crucial for the functionality of the TianGong AI Chat.

1. **Upgrade pip**: Keeping pip (the Python package installer) up-to-date ensures compatibility and the latest features.

   .. code-block:: bash

      pip install --upgrade pip

2. **Install required packages**: This will fetch and install the packages listed in `requirements.txt`.

   .. code-block:: bash

      pip install -r requirements.txt

   .. Tip:: 

      If you encounter network-related issues during package installation, consider using alternative mirrors. Here are some options:

      - Tsinghua University mirror:

        .. code-block:: bash

           pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

      - Aliyun mirror:

        .. code-block:: bash

           pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

      - Douban mirror:

        .. code-block:: bash

           pip install -r requirements.txt -i https://pypi.douban.com/simple/

3. **Upgrade project packages**: This ensures that all the packages are at their latest compatible versions.

   .. code-block:: bash

      pip install -r requirements.txt --upgrade


With the installation process successfully completed, you've laid a solid foundation for TianGong AI Chat on your system. Next, let's proceed with the essential configuration to get your chatbot up and running.