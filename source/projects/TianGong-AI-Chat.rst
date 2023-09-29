================
TianGong AI Chat 
================

- *This is* `Github Link <https://github.com/linancn/TianGong-AI-Chat.git>`_


Introduction
============

- This is a Introduction!
- Now, let's get your project up and running!

1. Prerequisites
^^^^^^^^^^^^^^^^

1.1 System Requirements
-----------------------

- **Operating System:** 

- Windows or MacOS. If you're on Windows, you can use the Windows Subsystem for Linux (WSL).

- **Internet Access:** 

- Have access to the internet environment required for chatgpt.

1.2 Setup and Installation
--------------------------

- **Python 3.11:**

- Download and install the latest version of Python for your OS from the official website.

- **Visual Studio Code (VS Code):**

- Grab the latest version of this versatile code editor from the VS Code website.

- **GitHub and Git:**

  1. Register for an account on `GitHub <https://github.com/>`_. 
  2. Install Git:
   
  * For Windows: Download the Git setup from the `official site <https://gitforwindows.org/>`_.
  * For MacOS: You can use Homebrew: ``brew install git``.

  3. Install the Git extension from the VS Code marketplace for seamless Git integration.

1.3 Clone the Project
--------------------------

  1. Open VS Code.
  2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the command palette.
  3. Type and select "Git: Clone" and then paste the GitHub repository URL (https://github.com/linancn/TianGong-AI-Chat.git).
  4. Choose a directory to save the project and VS Code will automatically download (or "clone") it for you.

1.4 Python Environment
----------------------------

- **Create a Virtual Environment:**

  1. Open a terminal in VS Code by pressing **Ctrl+`** (or **Cmd+`** on Mac).
  2. Create a virtual environment by running the following command:

  .. code-block:: bash

     python -m venv .venv

  3. Activate the virtual environment by running the following command:

  .. code-block:: bash

     source venv/bin/activate

- **Install the Required Packages:** - Install the required packages by running the following command:
   
   .. code-block:: bash
   
     pip install --upgrade pip
     pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
     pip install -r requirements.txt --upgrade


2. API Key and Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Customize the configuration by copying ``.streamlit/secrets.dev.toml`` and renaming it to ``.streamlit/secrets.toml``, then editing the required parameters as desired:

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
   | password             | Your password. If needed, set "need_passwd" to *True* in `tiangong-en.py` at line 2. |
   +----------------------+--------------------------------------------------------------------------------------+

- Tip: Replace every place that says ``Your*`` with the correct key or information.

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


3. Launch and Deploy
^^^^^^^^^^^^^^^^^^^^

- **Launch the Project:**

  1. Launch the project by running the following command:

  .. code-block:: bash

     export ui=tiangong-en
     streamlit run AI.py

- Or Using VsCode Debug Streamlit Configuration

  2. Once executed, Streamlit will pop up a new browser window displaying your app. From this interface, you can interact with your project and also share it with others.

- **Deploy the Project:**

  1. For detailed steps on deploying and sharing using Streamlit, please refer to the official `Streamlit Get Started guide <https://docs.streamlit.io/streamlit-community-cloud/get-started>`_ and this :ref:`guide <streamit>`.

4. Customize Your UI
^^^^^^^^^^^^^^^^^^^^


That's it! Your project should now be accessible via the Streamlit interface. Explore, interact, and share as needed!


1. **Customize Your UI**

   



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


