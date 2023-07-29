## InStockSystem API

This is the documentation for the InStockSystem API, which is used for managing an inventory of items. The API provides endpoints to create, retrieve, update, and delete items in the inventory.


### API Deployment

The API is currently deployed and accessible at [https://issinstocksyste-1-f1055394.deta.app](https://issinstocksyste-1-f1055394.deta.app).

### Requirements

To run the API and access the frontend, you need to have the following frameworks and libraries installed:

- [FastAPI](https://fastapi.tiangolo.com/) - Install using `pip install fastapi`
- [uvicorn](https://www.uvicorn.org/) - Install using `pip install uvicorn`
- [pydantic](https://pydantic-docs.helpmanual.io/) - Install using `pip install pydantic`
- [JQuery](https://jquery.com/)

### Installation and Local Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

3. Install the required Python packages:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. Start the API server using uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Endpoints

- **Get Index** (`GET /`): Returns the HTML content of the index page.
- **Get All Items** (`GET /get-all-items`): Returns a list of all items in the inventory.
- **Get Item by ID** (`GET /get-item/{item_id}`): Returns the details of an item specified by its ID.
- **Get Item by Name** (`GET /get-by-name`): Returns the details of an item specified by its name.
- **Create Item** (`POST /create-item/{item_id}`): Creates a new item in the inventory with the specified ID.
- **Update Item** (`PUT /update-item/{item_id}`): Updates the details of an existing item specified by its ID.
- **Delete Item** (`DELETE /delete-item`): Deletes an item from the inventory specified by its ID.


### Frontend

The frontend is automatically served when you run the local server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

The frontend includes the following functionalities:

- Show Stock: Displays all items in the inventory.
- Create Item: Creates a new item in the inventory.
- Get Item by ID: Retrieves the details of an item by its ID.
- Get Item by Name: Retrieves the details of an item by its name.
- Update Item: Updates the details of an existing item.
- Delete Item: Deletes an item from the inventory.

### Future Enhancements

The following enhancements and additional features are planned for future development:

1. **Adding Images**: Allow users to add images to the items in the inventory for visual representation.

2. **Integration with SQL Database**: Implement integration with a SQL database to store the inventory data persistently.

3. **User Profile and Authentication**: Add user profile functionality and implement authentication mechanisms to secure user access to the API.

4. **Item Creation Timestamps**: Track and display the date and time when items were added to the inventory.

### License


This project is licensed under the MIT License.