.. _deploy:

=========================
Deploy Your First Project
=========================

Follow the steps below to deploy your first app
================================================

.. 如何发布自己的项目

.. 1. 启动后，点击右上角的Deploy按钮

.. 2. 点击Deploy now按钮

.. 3. 注册或登录自己的streamlit账号

.. 4. 发布一个app

.. 4.1 Repository、Branch、Main file path、App URL (Optional)

.. 4.2 Advanced settings

.. 4.2.1 Python version=3.11

.. 4.2.2 Secrets：把.streamlit/secrets.toml的内容粘贴在蓝色框内，点击保存

.. 4.3 点击Deploy按钮

=================

Step1: Click on the "Deploy" button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon run or launch the application, click on the "Deploy" button in the top right corner.

.. image:: /_static/deploy-1.png

Step2: Click the "Deploy now" button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/deploy-2.png

Step3: Log in Streamlit account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sign up or log in to your Streamlit account

.. image:: /_static/deploy-3.png

Step4: Deploy an app
^^^^^^^^^^^^^^^^^^^^

Fill in the fields
---------------------

.. image:: /_static/deploy-4.png

Repository
>>>>>>>>>> 

Select the repository you want to deploy. Default is the **current repository**.

Branch
>>>>>>

Select the branch you want to deploy. Default is **main**.

Main file path
>>>>>>>>>>>>>>

Set the path to the main Python script that runs your app. Keep the default settings. 

App URL (Optional)
>>>>>>>>>>>>>>>>>>

Set the URL where your app will be deployed. Default is **https://share.streamlit.io/your-username/your-repo-name**. 

You can change the URL to something more memorable, like **aichat-example.streamlit.app**.

Navigate to Advanced settings
-----------------------------

Python version
>>>>>>>>>>>>>>

Set Python version to 3.11.

.. image:: /_static/deploy-5.png

Set Secrets
>>>>>>>>>>>

Under "Secrets", paste the contents of *.streamlit/secrets.toml* into the blue box and click "Save".

Click the "Deploy" button
-------------------------

Step5: Successfully deploy your first app!