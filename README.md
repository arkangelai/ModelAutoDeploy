## Getting Started

For deploy the algorithm, we utilized python-3.8 docker-image. We use guinicorn as server, with 2 workers and 2 threads. 

<br><br>
### Deploy on Cloud Run
___

You need to choose 2 cores and 4 GB of RAM. You must run in the console after download the project:
```
$ cd Diabetes-Eye-API
$ gcloud builds submit --tag gcr.io/$PROJECT_ID/$name_in_lowe_case .
```
After that, go to Cloud Run and create a new service (remember the minimum amount of hardware required), and look for the docker image created in the above step.


## Authors

<a href="http://ducic.ac.in/"><img src="https://arkangel.ai/assets/arkangel-logo-yellow-305b0d25317d055104b028d9db56e5b4e185f75fabf5bba3ac592e7c95974aa2.png" align="right" width="300"/></a>

* **[Jose Zea] - *jose@arkangel.ai*
* **[Daniel Lopez] - *daniel.lopez@arkangel.ai*
* **[Nicolas Munera] - *nicolas.munera@arkangel.ai*

## License

This is a private project, and belongs to Arkangel AI. Prohibited its used without the authors permission.
