======
Launch and Deploy
======

Launch
======

Chat (with Streamlit)
---------------------

**1. Via VSCode UI**:

- Open the **Run and Debug** sidebar by clicking on its icon in the left pane or pressing `Ctrl+Shift+D`.
- From the dropdown at the top, select "Chat".
- Press the green "Run" arrow button next to the dropdown to start the Streamlit app.

**2. Command Line (Within VSCode Terminal)**:

- Press ``Ctrl+` `` to open the terminal in VSCode.
- Navigate to the root directory of your project.
- Run the command:
  
  .. code-block:: bash

     streamlit run src/Chat.py

**Post-Launch**:

Upon successfully launching the Streamlit app, your default web browser should automatically open, displaying the TianGong AI Chat interface. If it doesn't, you can manually navigate to `http://localhost:8501` in your web browser to access the application. Here, you'll be able to interact with the chatbot, input queries, and view responses based on your previous customizations.


FastAPI
-------

**1. Via VSCode UI**:

- Open the **Run and Debug** sidebar by clicking on its icon in the left pane or pressing `Ctrl+Shift+D`.
- From the dropdown at the top, select "FastAPI".
- Press the green "Run" arrow button next to the dropdown to start the FastAPI server.

**2. Command Line (Within VSCode Terminal)**:

- Press ``Ctrl+` `` to open the terminal in VSCode.
- Navigate to the root directory of your project.
- Run the command:

  .. code-block:: bash

     uvicorn src.main:app --reload

**Post-Launch**:

After starting the FastAPI server, it will begin listening for incoming requests. By default, you can access the FastAPI documentation and test endpoints by visiting `http://localhost:8000/docs` in your web browser. This documentation interface, powered by Swagger, allows you to test API routes, view schemas, and understand the server's capabilities in detail.

Deploy
======

Streamlit
---------------------

Streamlit offers a seamless way to deploy your applications directly from the platform. This deployment method is straightforward and swift, making it ideal for fast prototyping or immediate usage.


Here's how you can do it:

1. **Initiate Deployment**:
   
   After running or launching the application, click on the "Deploy" button located in the top right corner.
   
   .. image:: /_static/deploy-1.png

2. **Start Deployment**:

   Click on the "Deploy now" button.

   .. image:: /_static/deploy-2.png

3. **Streamlit Account**:

   If you're not already logged in, you'll be prompted to sign up or log into your Streamlit account.

   .. image:: /_static/deploy-3.png

4. **App Deployment Settings**:

   Here, you'll provide details about your app's source and configuration.

   .. image:: /_static/deploy-4.png

   +------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Parameter              | Description                                                                                                        |
   +------------------------+--------------------------------------------------------------------------------------------------------------------+
   | **Repository**         | Choose the repository to deploy. By default, it selects the current repository.                                    |
   +------------------------+--------------------------------------------------------------------------------------------------------------------+
   | **Branch**             | Choose the branch for deployment. The default is *main*.                                                           |
   +------------------------+--------------------------------------------------------------------------------------------------------------------+
   | **Main file path**     | Specify the main Python script that powers your app. Retain the default if unsure.                                 |
   +------------------------+--------------------------------------------------------------------------------------------------------------------+
   | **App URL (Optional)** | Define your app's URL. The default format is *https://share.streamlit.io/your-username/your-repo-name*.             |
   +------------------------+--------------------------------------------------------------------------------------------------------------------+

   Consider setting a more memorable URL, such as **aichat-example.streamlit.app**.

5. **Advanced Settings**:

   Navigate to the advanced settings section.
   
   - **Python version**: Ensure the Python version is set to 3.11.
   
     .. image:: /_static/deploy-5.png

   - **Set Secrets**: In the "Secrets" section, input the contents of ``.streamlit/secrets.toml`` into the blue box and then click "Save".

6. **Finalize Deployment**:

   Click on the "Deploy" button to complete the process. Once done, your TianGong AI Chat is live and accessible to users worldwide!


Docker
------

Docker provides a more robust method of deployment suitable for production use. Below is the step-by-step process to deploy TianGong AI Chat using Docker:

.. note:: 
   The steps provided are for illustrative purposes. Always adapt these steps according to your deployment environment and specific requirements. Replace placeholders like ``[your-dockerhub-username]``, ``[version-tag]``, ``[YourDeploymentURL]``, and ``[YourEmailAddress]`` with your specific values when implementing the steps.


Docker Image Building
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Build the Docker image:
   
   .. code-block:: bash

      docker build -t [your-dockerhub-username]/tiangong-ai-chat:[version-tag] .

2. Push the built image to DockerHub:

   .. code-block:: bash

      docker push [your-dockerhub-username]/tiangong-ai-chat:[version-tag]

Production Deployment
^^^^^^^^^^^^^^^^^^^^

1. Create a dedicated Docker network:

   .. code-block:: bash

      docker network create tiangongbridge

2. Install and manage the nginx service:

   .. code-block:: bash

      sudo apt update
      sudo apt install nginx
      sudo nginx
      sudo nginx -s reload
      sudo nginx -s stop

3. Set up the nginx-proxy for reverse proxying:

   .. code-block:: bash

      docker run --detach \
          --name nginx-proxy \
          --restart=always \
          --publish 80:80 \
          --publish 443:443 \
          --volume certs:/etc/nginx/certs \
          --volume vhost:/etc/nginx/vhost.d \
          --volume html:/usr/share/nginx/html \
          --volume /var/run/docker.sock:/tmp/docker.sock:ro \
          --network=tiangongbridge \
          --network-alias=nginx-proxy \
          nginxproxy/nginx-proxy:latest

4. Deploy the nginx-proxy ACME companion for SSL certificate handling:

   .. code-block:: bash

      docker run --detach \
          --name nginx-proxy-acme \
          --restart=always \
          --volumes-from nginx-proxy \
          --volume /var/run/docker.sock:/var/run/docker.sock:ro \
          --volume acme:/etc/acme.sh \
          --network=tiangongbridge \
          --network-alias=nginx-proxy-acme \
          nginxproxy/acme-companion:latest

5. Launch TianGong AI Chat:

   .. code-block:: bash

      docker run --detach \
          --name tiangong-ai-chat \
          --restart=always \
          --expose 8501 \
          --net=tiangongbridge \
          --env ui=tiangong-en \
          --env VIRTUAL_HOST=[YourDeploymentURL] \
          --env VIRTUAL_PORT=8501 \
          --env LETSENCRYPT_HOST=[YourDeploymentURL] \
          --env LETSENCRYPT_EMAIL=[YourEmailAddress] \
          [your-dockerhub-username]/tiangong-ai-chat:[version-tag]

6. Copy the secrets file to the running container:

   .. code-block:: bash

      docker cp .streamlit/secrets.toml tiangong-ai-chat:/app/.streamlit/secrets.toml
