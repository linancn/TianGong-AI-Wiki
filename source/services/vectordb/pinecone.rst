.. _pinecone:

========
Pinecone
========

---------------------------------

.. code-block:: bash

      # Pinecone API Key and Environment
      pinecone_api_key = "YourKey"
      pinecone_environment = "YourENV"
      pinecone_index = "YourIndex"

1. **Sign Up or Log In**
   - If you're new to Pinecone, first `sign up here <https://app.pinecone.io/?sessionType=signup>`_.
   - If you have an account, `log in here <https://www.pinecone.io/>`_.

   .. image:: /_static/pinecone-1.png

2. **Get Your API Key and Environment**
   a. After logging in, click "API Keys" on the left.
   b. Create a new API key or use the default one.

   .. image:: /_static/pinecone-2.png

   c. Copy both the API key and the Environment.

   .. image:: /_static/pinecone-3.png

   d. Then, add them to your code:

   .. code-block:: bash

      pinecone_api_key = "YourKey"
      pinecone_environment = "YourENV"

3. **Set Up Pinecone Index**
   a. First, make a new Index.

   .. image:: /_static/pinecone-4.png

   b. Configure the Index:
      - Choose a name for the index, like "gpt".
      - Pick the type, size, and other settings. For example: 1536 dimensions, cosine metric, and the Default starter Pod Type.

   .. image:: /_static/pinecone-5.png

   c. Copy the Index Name and add to your code:

   .. code-block:: bash

      pinecone_index = "YourIndex"
