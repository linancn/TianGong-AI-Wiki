.. _openai:

======
OpenAI
======

1. **Account Access**
   - If you're new to OpenAI, sign up `here <https://platform.openai.com/signup>`_.
   - Otherwise, just log in at `OpenAI API <https://platform.openai.com/>`_.

2. **Get Your API Key**

   a. Click on your account name (top right). Choose "View API keys".
   
   .. image:: /_static/openai-api-1.png
   
   b. Click to make a new API key.
   
   .. image:: /_static/openai-api-2.png
   
   c. Copy the shown API key.
   
   .. image:: /_static/openai-api-3.png
   
   d. Return to your ``.streamlit/secrets.toml`` file. Paste the API key:
   
   .. code-block:: bash

    openai_api_key = "YourKeyHere"