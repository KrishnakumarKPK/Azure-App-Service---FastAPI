# Example of Deploying a FastAPI App using Azure App Service

An example of how a machine learning model can be served from a REST API using [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/), a PaaS for hosting web applications.  
### Directory Contents
- `scripts/` contains the Python scripts used in the `main.py` file
- `static/` contains the Jupyter notebook, the data used for our model, and the model itself
- `main.py` contains the logic for our API

### Instructions for Deployment
**local deployment**
1. Create a Python environment for this project (e.g. `python3 -m venv azure-app-service`).
2. Activate your new environment and install the dependencies listed in `requirements.txt`. If using PIP, run `pip install` from this project's root directory.
3. Run `uvicorn main:app` from your projects root directory.
4. Navigate to `http://localhost:8000` from a browser.

**from the Azure Portal**
1. Fork the [repo](https://github.com/roshmadosh/azure-app-service-fastapi) to your own github account.  
2. From the Azure portal, look up "App Services" on the search bar and navigate to the service.  
3. Click "create"
4. Fill out the first page. 
   - "Runtime stack" should be "Python 3.10"
   - "Pricing plan" must be "Basic" or better for Github deployment (**this is not a free pricing plan. if you don't want to incur charges, remember to delete resources**).
5. On the "Deployment" page, connect to the forked repository on your Github account. 
6. Create the app service.
7. Once created, go to the resource and navigate to the "Configuration" setting.
8. Under the "General Settings" tab, copy and paste `gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000` into startup command.
9. Go back to the "Overview" section and restart the App Service.
10. Go to the "Overview" tab and click on the link under `Default domain`.

### Use of API  
Making a GET request to your `Default domain` or navigtaing to it from the browser should return the page seen in the image above.  

A POST request to `{your_default_domain}/predict?color={some_color}&shape={some_shape}` makes use of our ML model, and returns a response with our target variable `happiness_score`.  
### Troubleshooting  

- If you get a 429 error, try recreating the App Service in a different region.  
- You should not have to specify a port. It takes a while for the app to deploy so give it 5-10 mins.
