================
TianGong-AI-Chat 
================

- Github: `TianGong-AI-Chat <https://github.com/linancn/TianGong-AI-Chat.git>`_

--------------------

**Prerequisites**: 

Before we dive in, it's assumed that you:

1. Already have a Python environment set up.
2. Have access to the internet environment required for chatgpt.

--------------------

Now, let's get your project up and running!
  

Follow these steps to set up and launch the project


1. **Setting Up Your Development Environment with VS Code**
   
   We recommend using Visual Studio Code (VS Code) for a smoother development experience.

   a. If you haven't already, `download and install VS Code <https://code.visualstudio.com/download>`_.
   b. Install git on your computer. `Download and install git <https://git-scm.com/downloads>`_.
   c. Install the Git extension from the VS Code marketplace for seamless Git integration.

2. **Download the Project from GitHub using VS Code**
   
   Once you have VS Code set up:

   a. Open VS Code.
   b. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the command palette.
   c. Type and select "Git: Clone" and then paste the GitHub repository URL (https://github.com/linancn/TianGong-AI-Chat.git).
   d. Choose a directory to save the project and VS Code will automatically download (or "clone") it for you.

3. **Set Up the Environment**
   
   a. Open a terminal in VS Code by pressing **Ctrl+`** (or **Cmd+`** on Mac).
   b. Create a virtual environment by running the following command:

   .. code-block:: bash

      python -m venv .venv

   c. Activate the virtual environment by running the following command:

   .. code-block:: bash
   
      source venv/bin/activate
   
   d. Install the required packages by running the following command:

   .. code-block:: bash

      pip install --upgrade pip
      pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
      pip install -r requirements.txt --upgrade




4. **Get Your API Keys**
   
   Customize the configuration by copying ``.streamlit/secrets.dev.toml`` and renaming it to ``.streamlit/secrets.toml``, then editing the required parameters as desired:

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


5. **Launch and Deploy**

   a. Launch the project by running the following command:
   
   .. code-block:: bash

      export ui=tiangong-en
      streamlit run AI.py

   Or Using VsCode Debug Streamlit Configuration

   b. Once executed, Streamlit will pop up a new browser window displaying your app. From this interface, you can interact with your project and also share it with others.

   c. For detailed steps on deploying and sharing using Streamlit, please refer to the official `Streamlit Get Started guide <https://docs.streamlit.io/streamlit-community-cloud/get-started>`_ and this :ref:`guide <streamit>`.

That's it! Your project should now be accessible via the Streamlit interface. Explore, interact, and share as needed!


6. **Customize Your UI**

   You can customize your UI by :ref:`Customize <ui>`



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


