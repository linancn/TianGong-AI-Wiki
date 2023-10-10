======
Customization
======

Text and Locale
===============

**Introduction**: 
To provide a unique user experience and cater to various localization needs, TianGong AI Chat offers extensive customization of its user interface text and locale settings. All of these modifications are performed within the ``src/ui`` directory, enabling you to tailor the chatbot's linguistic and thematic elements as per your requirements.

**What can be customized**:
TianGong's design enables you to personalize a wide range of user interface components. Below is a comprehensive list of the user interface components in TianGong that you can modify:

- **Theme Color**: `theme["primaryColor"]`
- **Page Details**:
   - Title: `page_title`
   - Icon: `page_icon`
   - Custom Styles: `page_markdown`
- **Sidebar Content**:
   - Image: `sidebar_image`
   - Title: `sidebar_title`
   - Subheader: `sidebar_subheader`
   - Markdown Content: `sidebar_markdown`
   - Expanded Section Title: `sidebar_expander_title`
   - File Uploader Settings: `sidebar_file_uploader_title`, `sidebar_file_uploader_spinner`, `sidebar_file_uploader_error`
   - New Chat Button Label: `sidebar_newchat_button_label`
   - Delete Chat Button Label: `sidebar_delete_button_label`
- **Chat Interaction Messages**:
   - AI's Welcome Message: `chat_ai_welcome`
   - User's Input Placeholder: `chat_human_placeholder`
   - Chat History Title: `current_chat_title`
   - AI's Avatar: `chat_ai_avatar`
   - User's Avatar: `chat_user_avatar`
- **Search Options**:
   - Knowledge Base Checkbox Label: `search_knowledge_base_checkbox_label`
   - Internet Checkbox Label: `search_internet_checkbox_label`
   - Wikipedia Checkbox Label: `search_wikipedia_checkbox_label`
   - arXiv Checkbox Label: `search_arxiv_checkbox_label`
   - Documents Checkbox Label: `search_docs_checkbox_label`
   - Document Search Options and Descriptions: `search_docs_options`, `search_docs_options_isolated`, `search_docs_options_combined`
- **Password Requirement**: `need_passwd`

To modify these components, simply update the values within the ``ui_data`` dictionary in the provided ``tiangong-en.py`` file or any custom file you create. After making your changes, the system fetches the UI configuration by referencing the appropriate file in ``src/ui_config.py``.

.. tip:: 
   For instance, if you want the chatbot to greet users in Spanish, you'd change the ``chat_ai_welcome`` entry in the ``ui_data`` dictionary to: "¿En qué puedo ayudarte?".

By tapping into the flexibility of this structure, you can create a truly personalized experience, catering to different audiences and regions.


Image
===================

TianGong AI Chat allows for the customization of its visual elements, ensuring that the chatbot's appearance aligns with your branding or desired aesthetics.

**Image Directory**: 
All images utilized by TianGong AI Chat are housed in the ``src/static`` folder. This directory includes essential images like favicons, logos, and other visual elements that contribute to the chatbot's user interface.

**Customizing Images**:
To personalize the chatbot's imagery:

1. Place your desired images within the ``src/static`` directory.
2. Adjust the relevant paths in the configuration files to point to your new images using relative paths. For instance, if you've added a new logo named "mylogo.png", you'd update the corresponding entry in the configuration to: ``"src/static/mylogo.png"``.

By following these steps, you can give your chatbot a unique visual identity that resonates with your brand or project theme.

With the text, locale, and image customizations complete, your TianGong AI Chat is now tailored to provide a unique user experience. Next, we'll guide you through the essential steps to debug, launch, and deploy your customized chatbot, ensuring its smooth and efficient operation.