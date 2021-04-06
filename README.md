
# Diseases Detection for Eye Color Fundus Images

> In this project we proposed an algorithm for Disease Detection in eye color fundus images. We used a variety of techniques: eye detection, antialiassing filter, mean subtraction and CNN for multilabel disease classification. We tried multioutput and multiple losses functions, we found that the best loss function was cosine simmilarity distance (it was proposed with the hypothesis that the classification was multilabel and no single label).

<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/DanielLopez-1805/Imagenes/master/DiagramaFlujo.png" style="border-radius: 50%;"/>
</p>

<br><br>


## Guiding workflows based on another github projects
<ul>
  <li>https://towardsdatascience.com/building-a-multi-output-convolutional-neural-network-with-keras-ed24c7bc1178</li>
</ul>

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

## Metrics

Presicion Recall Curve:

<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/DanielLopez-1805/Imagenes/master/Metricas/Presicion_Recall_Curve.png" style="border-radius: 50%;"/>
</p>
<br>

Metrics:

<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/DanielLopez-1805/Imagenes/master/Metricas/Metrics.png" style="border-radius: 50%;"/>
</p>
<br>

Testing with Diabetes and Normal Images:

<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/DanielLopez-1805/Imagenes/master/Metricas/Ensamble.png" style="border-radius: 50%;"/>
</p>
<br>

## Decision Tree
<br>
<p align="center">
  <img src="https://raw.githubusercontent.com/DanielLopez-1805/Imagenes/master/Metricas/Diagrama%20de%20Desicion.png" style="border-radius: 50%;"/>
</p>
<br>

## Authors

<a href="http://ducic.ac.in/"><img src="https://arkangel.ai/assets/arkangel-logo-yellow-305b0d25317d055104b028d9db56e5b4e185f75fabf5bba3ac592e7c95974aa2.png" align="right" width="300"/></a>

* **[Jose Zea] - *jose@arkangel.ai*
* **[Daniel Lopez] - *daniel.lopez@arkangel.ai*

## License

This is a private project, and belongs to Arkangel AI. Prohibited its used without the authors permission.
