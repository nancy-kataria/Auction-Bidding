# Auction-Bidding

<a id="readme-top"></a>
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#demonstration">Demonstration</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img width="1421" alt="Screenshot 2024-09-18 at 11 44 43 PM" src="https://github.com/user-attachments/assets/2018bf31-fcbb-456f-823c-ac48014a4a6e">
Auction Bidding project is a live streaming project that uses kafka to stream bidding data from Flask website.

The project is based on an auction where people bid for certain products. It is an end-to-end pipeline where a web application takes input from the end user and the submissions are stored in a database. A real time dashboard then shows the latest insights on that data.

This project uses kafka to publish records to the DB and consume from it to display on a dashboard.

Here's why we need Confluent Kafka in this project:
* Confluent Kafka is a cloud version of Kafka which means the data will be stored on cloud.
* Instead of using multiple servers running parallely, we use one web server with auto-scaling.
* To prevent loss of data while parallel processing, Kafka enables multiple consumers in same group to share the messages among themselves so that they can perform operations on their set of data in parallel. :smile:

The producer gets data from the website and loads it on kafka topic.
There can be Thousands of people bidding at the same time so we will use multiple consumers to consume messages from kafka topic and load in database parallely. They run parallel so, messages are divided among consumers.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![ConfluentKafka][ConfluentKafka]][ConfluentKafka-url]
* [![MySQL][MySQL]][MySQL-url]
* [![HTML][HTML]][HTML-url]
* [![JavaScript][JavaScript]][JavaScript-url]
* [![CSS][CSS]][CSS-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Results

<img width="1427" alt="Screenshot 2024-09-24 at 4 39 34 PM" src="https://github.com/user-attachments/assets/c9499b23-a415-49bd-bb7b-4683e33d3961">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Demonstration

#### A demonstration on how parallel processing works when 15-20 people bid at the same time.

#### Flushing Records into Kafka Topic:
![Screenshot 2024-09-29 at 11 50 14 PM](https://github.com/user-attachments/assets/27c1b659-5b9a-4273-9af0-0358a73c6769)

#### 1st Consumer of Kafka topic records:
![Screenshot 2024-09-29 at 11 50 38 PM](https://github.com/user-attachments/assets/49c5a967-d0e4-4a5b-af4c-db41cb3c634a)

#### 1st Consumer of Kafka topic records:
![Screenshot 2024-09-29 at 11 51 03 PM](https://github.com/user-attachments/assets/7a7b3d17-1e39-4694-8d33-00097422eef7)

#### Messages in Kafka Topic:
<img width="1100" alt="Screenshot 2024-09-30 at 8 50 03 PM" src="https://github.com/user-attachments/assets/ba217806-bcf1-4076-83c5-d84dde15fcff">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nancy-kataria8/
<!-- Badges (Icons) -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Flask]: https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask&logoColor=white
[ConfluentKafka]: https://img.shields.io/badge/ConfluentKafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white
[MySQL]: https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[HTML]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[CSS]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white

<!-- URLs -->
[Python-url]: https://www.python.org/
[Flask-url]: https://flask.palletsprojects.com/
[ConfluentKafka-url]: https://www.confluent.io/
[MySQL-url]: https://www.mysql.com/
[HTML-url]: https://developer.mozilla.org/en-US/docs/Web/HTML
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
