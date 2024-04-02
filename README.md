Raccoon AI Startup

Server:
1. Installing Virtual Environment and Dependencies
Before running the server, ensure you have Python and pip installed on your system. Then, follow these steps to set up the virtual environment and install dependencies:
  1. Open a terminal or command prompt.
  2. Navigate to the project directory using cd.
  3. Create a virtual environment named venv:
      ```python -m venv venv```
  4. Activate the virtual environment:
      On Windows:
        ```venv\Scripts\activate```
      On Unix or MacOS:
        ```source venv/bin/activate```
  5. Once the virtual environment is activated, install the project dependencies using the requirements.txt file:
      ```pip install -r requirements.txt```

2. Running the Server
After setting up the virtual environment and installing the dependencies, you're ready to run the server. Follow these steps:
  1. Navigate to the src folder using cd.
  2. Run the server script server.py:
      ```python server.py```
The server should now be running, and you should see output indicating that the server is listening on a specific port.

3. Accessing the Server
Once the server is running, you can access it using the appropriate endpoint or URL. The exact URL will depend on your server configuration and the routes defined in your server.py file. Consult your project documentation or codebase for more information on accessing the server endpoints.

4. Deactivating the Virtual Environment (Optional)
When you're done working with the project, you can deactivate the virtual environment:
```deactivate```
This will return you to your regular command prompt environment.

Client:
1. Installing Node.js and npm
Before running the client, make sure you have Node.js and npm (Node Package Manager) installed on your system. If you haven't already installed them, you can download and install them from the official Node.js website: Node.js Downloads

2. Installing Dependencies
Once Node.js and npm are installed, follow these steps to install the required dependencies for the client:
  1. Open a terminal or command prompt.
  2. Navigate to the client directory of your project using cd.
  3. Run the following command to install the dependencies specified in the package.json file:
      ```npm install```
     
3. Running the Client
After installing the dependencies, you can start the client application by running the following command:
  ```npm run dev```
This command will execute the script defined in the package.json file, typically used to start the development server or build the client application. Ensure that the script dev is properly configured in your package.json file to start the client application.

4. Accessing the Client Application
Once the client application is running, you can access it using a web browser. The exact URL will depend on the configuration of your client application and any routes or endpoints defined within it. Consult your project documentation or codebase for more information on accessing the client application.

5. Stopping the Client Application
To stop the client application, you can typically press Ctrl + C in the terminal or command prompt where it is running. This will halt the execution of the npm run dev command and stop the development server.
