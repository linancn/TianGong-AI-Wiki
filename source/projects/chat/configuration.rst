=============
Configuration
=============

TianGong AI Chat integrates with various online services; configuring the parameters in secrets.toml ensures seamless connectivity and operation with these services.

Creating `secrets.toml`
-----------------------

There are two methods to establish your `secrets.toml`:

1. **Using the Template**:
   
   - Copy the provided template ``.streamlit/secrets.dev.toml``.
   - Rename this copy to ``.streamlit/secrets.toml``.
   
2. **From Scratch**:

   - Create a new file named ``secrets.toml`` in the ``.streamlit`` directory.
   - Copy the following configuration code and paste it into your newly created file:

   .. code-block:: toml

      openai_api_key = "YourOpenAIKey"
      pinecone_api_key = "YourPineconeKey"
      pinecone_environment = "YourPineconeEnvironmentDetails"
      pinecone_index = "YourPineconeIndex"
      xata_api_key = "YourXataKey"
      xata_db_url = "YourXataDatabaseURL"
      langchain_verbose = true
      llm_model = "YourLLMModelName"
      password = "YourPassword"

Parameters
------------------------

Here are the parameters you'll need to set, along with descriptions and links to acquire the necessary credentials or details:

.. table:: 
    
  +----------------------+------------------------------------------------------------------------------------------------+
  | Parameter            | Description                                                                                    |
  +----------------------+------------------------------------------------------------------------------------------------+
  | openai_api_key       | Your API key for `OpenAI </configurations/openai.html>`_.                                      |
  +----------------------+------------------------------------------------------------------------------------------------+
  | pinecone_api_key     | Your API key for `Pinecone </configurations/pinecone.html>`_.                                  |
  +----------------------+------------------------------------------------------------------------------------------------+
  | pinecone_environment | Details about your `Pinecone environment </configurations/pinecone.html>`_.                    |
  +----------------------+------------------------------------------------------------------------------------------------+
  | pinecone_index       | Information about your `Pinecone index </configurations/pinecone.html>`_.                      |
  +----------------------+------------------------------------------------------------------------------------------------+
  | xata_api_key         | Your API key for `Xata </configurations/xata.html>`_.                                          |
  +----------------------+------------------------------------------------------------------------------------------------+
  | xata_db_url          | The `URL </configurations/xata.html>`_ for your Xata database.                                 |
  +----------------------+------------------------------------------------------------------------------------------------+
  | langchain_verbose    | Indicates if LangChain should be verbose (true/false). Default is *true*.                      |
  +----------------------+------------------------------------------------------------------------------------------------+
  | llm_model            | The name of your LLM model. Default is *gpt-4*.                                                |
  +----------------------+------------------------------------------------------------------------------------------------+
  | password (optional)  | Your password. If needed, refer to `Customization <customization.html>`_ for password settings.|
  +----------------------+------------------------------------------------------------------------------------------------+

For acquiring the necessary API keys and more specifics for each service, kindly follow the links provided in the table.


Having completed the configuration, TianGong AI Chat is now ready to integrate with the designated online services. Next, we'll dive into enhancing the user interface by customizing texts, locales, and adding images to refine your chatbot's appearance.