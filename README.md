# Auction-Bidding

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
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

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![ConfluentKafka][ConfluentKafka]][ConfluentKafka-url]
* [![MySQL][MySQL]][MySQL-url]
* [![HTML][HTML]][HTML-url]
* [![JavaScript][JavaScript]][JavaScript-url]
* [![CSS][CSS]][CSS-url]


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
