================
TianGong-AI-Chat
================


Env Preparing:
==============

Setup venv:
===========

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements:
^^^^^^^^^^^^^^^^^^^^^

```bash
pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```

Key Configurations
===================

1. **Update Secret Keys**
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

   openai_api_key = "YourKeyHere"
   pinecone_api_key = "YourKeyHere"
   pinecone_environment = "YourEnvironmentInfo"
   pinecone_index = "YourIndexInfo"
   xata_api_key = "YourKeyHere"
   xata_db_url = "YourURLHere"
   langchain_verbose = true
   llm_model = "YourModelName"
   password = "YourKeyHere" 
   # If needed, set "need_passwd" to True in `tiangong-en.py` at line 2.






一级标题
^^^^^^^^

二级标题
---------

三级标题
>>>>>>>>>

四级标题
:::::::::

五级标题
'''''''''

六级标题
""""""""


