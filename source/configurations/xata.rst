.. _xata:

====
Xata
====


Get your Xata API Key and Database URL in these steps:

1. **Sign Up/Log In**:
   - Sign in to `Xata using GitHub or Google <https://xata.io/>`_.

2. **Retrieve Your API Key**:
   a. Click on your profile at the top right and choose "Account settings".
      
      .. image:: /_static/xata-1.png
      
   b. Start adding a new API key.
      
      .. image:: /_static/xata-2.png
      .. image:: /_static/xata-3.png
      
   c. Copy this key.
      
      .. image:: /_static/xata-4.png
      
   d. Include this in your code:

      .. code-block:: bash

         xata_api_key = "YourKey"

3. **Get Your Database URL**:
   a. Create a new database.
      
      .. image:: /_static/xata-5.png
      
   b. Click on the gear icon, then "Copy Database URL".
      
      .. image:: /_static/xata-6.png
      .. image:: /_static/xata-7.png
      
   c. Add this to your code:

      .. code-block:: bash

         xata_db_url = "YourURL"

LLM model
=========

[Details about LLM model configuration]

Password (optional)
===================

[Description and steps to set up optional password]

Customize Your UI
=================

Edit the file at:

.. code-block:: text

   ./src/ui/tiangong-en.py

Run Locally
===========

Use the following command:

.. code-block:: bash

   export ui=tiangong-en
   streamlit run AI.py

Or, if you're using VS Code, opt for the Debug Streamlit Config.
