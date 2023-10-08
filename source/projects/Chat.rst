================
Chat 
================

- This is the *Chat* project`s `Github Link <https://github.com/linancn/TianGong-AI-Chat.git>`_. You can clink `here <https://newchat.tiangong.world/>`_  to view *TianGong Chat* application.

.. tip:: 
  1. Before going any further, make sure your system meets all the :ref:`Environment <sysenv>` and :ref:`Prerequisites <prerequisites>`.
  2. Have access to the internet environment required for chatgpt.
   
Introduction
============

.. chat是什么

What is Chat?
^^^^^^^^^^^^^

Chat Application is a web application that allows users to chat with AI. 

.. It is based on the OpenAI GPT-4 model and uses the Pinecone database to store the knowledge database. It also uses the Xata to store the user's history information. The application is built using the Streamlit framework and is deployed using Streamlit Sharing.


.. chat的安装方法

Installation
============


Clone the Project
^^^^^^^^^^^^^^^^^

1. Run Visual Studio Code and open the command palette. 




.. tabs::

   .. group-tab:: Windows WSL2

    Make sure you have WSL2 installed. If not, follow the `instructions <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.

    Run Visual Studio Code in WSL using the WSL extension. You can read more about it from `here <https://code.visualstudio.com/docs/remote/wsl-tutorial>`_.

      Ctrl+Shift+P # open the command palette

   .. group-tab:: MacOS

    We recommend using the VSCode Dev Contariners. 
    
    Before proceeding, make sure you have Docker and the VS Code Dev Containers extension set up. You can read more about it from `here <https://code.visualstudio.com/docs/devcontainers/tutorial>`_.

      Cmd+Shift+P # open the command palette

2. Type and select ``Git: Clone``, then paste the GitHub repository URL *(https://github.com/linancn/TianGong-AI-Chat.git)*.

3. Choose a directory to save the project (such as ``/home/uesr/projects/``), and VS Code will automatically download (or "clone") it for you.

.. tip:: 
  Install the recommended extensions form the VS Code marketplace.

Virtual Environment
^^^^^^^^^^^^^^^^^^^

1. Create a virtual environment by running the following command in the terminal:

.. code-block:: bash

   python3.11 -m venv .venv

2. Activate the virtual environment:

.. code-block:: bash

   source venv/bin/activate

Install the required packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Upgrade pip

.. code-block:: bash

  pip install --upgrade pip

2. Install packages

.. code-block:: bash

  pip install -r requirements.txt
  # Optional: Using the Tsinghua Mirror (Recommended for users in China):
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

3. Upgrade packages

.. code-block:: bash

  pip install -r requirements.txt --upgrade

Configuration
=============

- Customize the configuration by copying ``.streamlit/secrets.dev.toml`` and renaming it to ``.streamlit/secrets.toml``, then editing the required parameters as desired:

.. table:: Configuration Parameters

  +----------------------+--------------------------------------------------------------------------------------+
  | Parameter            | Description                                                                          |
  +----------------------+--------------------------------------------------------------------------------------+
  | openai_api_key       | Your OpenAI API key, you can get it from :ref:`here <openai>`                        |
  +----------------------+--------------------------------------------------------------------------------------+
  | pinecone_api_key     | Your Pinecone API key,you can get it from :ref:`here <pinecone>`                     |
  +----------------------+--------------------------------------------------------------------------------------+
  | pinecone_environment | Details about your Pinecone environment                                              |
  +----------------------+--------------------------------------------------------------------------------------+
  | pinecone_index       | Information about your Pinecone index                                                |
  +----------------------+--------------------------------------------------------------------------------------+
  | xata_api_key         | Your Xata API key                                                                    |
  +----------------------+--------------------------------------------------------------------------------------+
  | xata_db_url          | The URL for your Xata database                                                       |
  +----------------------+--------------------------------------------------------------------------------------+
  | langchain_verbose    | Indicates if Langchain should be verbose (true/false)                                |
  +----------------------+--------------------------------------------------------------------------------------+
  | llm_model            | The name of your LLM model                                                           |
  +----------------------+--------------------------------------------------------------------------------------+
  | password (optional)  | Your password. If needed, set "need_passwd" to *True* in `tiangong-en.py` at line 2. |
  +----------------------+--------------------------------------------------------------------------------------+

.. tip:: 
  Replace every place that says ``Your*`` with the correct key or information.

  .. code-block:: bash

    openai_api_key = "YourKey"
    pinecone_api_key = "YourKey"
    pinecone_environment = "YourENV"
    pinecone_index = "YourIndex"
    xata_api_key = "YourKey"
    xata_db_url = "YourURL"
    langchain_verbose = true
    llm_model = "YourModel"
    password = "YourKey"

Customization
=============


.. 定制你的UI
.. 进入src/ui/tiangong-en.py

.. 设置密码（可选）

.. 设置

Launch
======

1. Launch the project by running the following command:

.. code-block:: bash

   streamlit run ./src/AI.py

- Or Using VsCode Debug Streamlit Configuration

2. Once executed, Streamlit will pop up a new browser window displaying your app. From this interface, you can interact with your project and also share it with others.

Deploy
======

1. Upon run or launch the application, click on the "Deploy" button in the top right corner.

.. image:: /_static/deploy-1.png

2. Click the "Deploy now" button

.. image:: /_static/deploy-2.png

3. Sign up or log in to your Streamlit account

.. image:: /_static/deploy-3.png

4. Deploy an app

- **Fill in the fields**

.. image:: /_static/deploy-4.png

+------------------------+--------------------------------------------------------------------------------------------------------------------+
| Parameter              | Description                                                                                                        |
+------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Repository**         | Select the repository you want to deploy. Default is the *current repository*.                                     |
+------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Branch**             | Select the branch you want to deploy. Default is *main*.                                                           |
+------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Main file path**     | Set the path to the main Python script that runs your app. Keep the default settings.                              |
+------------------------+--------------------------------------------------------------------------------------------------------------------+
| **App URL (Optional)** | Set the URL where your app will be deployed. Default is *https://share.streamlit.io/your-username/your-repo-name*. |
+------------------------+--------------------------------------------------------------------------------------------------------------------+

You can change the URL to something more memorable, like **aichat-example.streamlit.app**.

Navigate to Advanced settings
-----------------------------

- **Python version**: Set Python version to 3.11.

.. image:: /_static/deploy-5.png

- **Set Secrets**: Under "Secrets", paste the contents of ``.streamlit/secrets.toml`` into the blue box and click "Save".

Click the "Deploy"
-------------------------

Successfully deploy your first app!







   



.. 一级标题
.. ^^^^^^^^

.. 二级标题
.. ---------

.. 三级标题
.. >>>>>>>>>

.. 四级标题
.. :::::::::

.. 五级标题
.. '''''''''

.. 六级标题
.. """"""""


