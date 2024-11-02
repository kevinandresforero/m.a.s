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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Proyecto de reconococimiento de emociones usando deepface</h3>

  <p align="center">
    Esta es una aplicacion desarrolladada con Flask para poder ser utilizada por una pagina web que implemente una camara en la que se de el reconocimiento de emociones de los estudiantes
    <br />
    <a href="#"><strong>Revisa la documentación »</strong></a>
    <br />
    <br />
    <a href="#">Ver un Demo</a>
    ·
    <a href="#">Ver una guia </a>
    ·
    <a href="#">Comunicate con nosotros</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li>
      <a href="#about-the-project">Acerca del Proyecto</a>
      <ul>
        <li><a href="#built-with">Contruido con</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Para Empezar</a>
      <ul>
        <li><a href="#prerequisites">Prerequisitos</a></li>
        <li><a href="#installation">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#usage">Como usar</a></li>
    <li><a href="#contributing">Contribución</a></li>
    <li><a href="#license">Licencia</a></li>
    <li><a href="#contact">Contacto</a></li>
    <li><a href="#acknowledgments">Agradecimientos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Proyecto de reconococimiento de emociones usando deepface][product-screenshot]](https://example.com)

Esta es una aplicacion desarrolladada con Flask para poder ser utilizada por una pagina web que implemente una camara en la que se de el reconocimiento de emociones de los estudiantes

¿Como funciona?
Se crea una carpeta de carga de archivos que acepta las siguientes extenciones 'png', 'jpg', 'jpeg' y 'gif' donde se subiran las grabaciones que se grabene en la 
pagina o las imagenes que se tomen para posteriormentente se analizen con deepface, dada una imagen se reconocen todos los rostros de la imagen tomada se recorta el rostro.
se cambia el color de la imagen para poder analizarla por medio de cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) debido a que el reconocimiento de emociones se ve afectado por el color del rostro 
, se pide y se analizan datos de edad genero raza y emocion de los que solo se recolecta la emocion y se clasifica en una de las siguientes Enojado,Disgustado,Miedoso,Feliz,Triste,Sorprendido y Neutral
se pide una confianza mayor al 0.8 de confianza y se retorna la emocion.


<p align="right">(<a href="#readme-top">bVolver al inicio</a>)</p>


### Construido con

En esta sección deberías enumerar los principales frameworks/bibliotecas utilizados para arrancar tu proyecto.

absl-py==2.1.0 Apache Software License (Apache 2.0) libre
astunparse==1.6.3 Licencia BSD libre
attrs==24.2.0 MIT License libre
beautifulsoup4==4.12.3 MIT License libre
blinker==1.8.2 MIT License libre
certifi==2024.8.30   Mozilla Public License 2.0 (MPL 2.0) (MPL-2.0) libre
cffi==1.17.1   MIT License libre
charset-normalizer==3.3.2 MIT License libre
click==8.1.7 BSD License (BSD-3-Clause) libre
-e git+https://github.com/serengil/deepface.git@5c242e2c852335ca4f8f05f88af634c050b70b28#egg=deepface OSI Approved :: MIT License
Flask: BSD License
Flask-Cors: MIT License (MIT)
flatbuffers: Apache Software License (Apache 2
fonttools: MIT License (MIT)
gast: BSD License (BSD 3-Clause)
gdown: MIT License (MIT)
google-pasta: Apache Software License (Apache 2
grpcio: Apache Software License (Apache License 2
gunicorn: MIT License (MIT)
h5py: BSD License (BSD-3-Clause)
idna: BSD License
itsdangerous: BSD License
jax: Apache-2
jaxlib: Apache-2
Jinja2: BSD License
keras: Apache License 2
kiwisolver: BSD License (
libclang: Apache Software License (Apache License 2
Markdown: BSD License (BSD 3-Clause License  Copyright 2007
markdown-it-py: MIT License
MarkupSafe: BSD License (BSD-3-Clause)
matplotlib: Python Software Foundation License (License agreement for matplotlib versions 1
mdurl: MIT License
mediapipe: Apache Software License (Apache 2
ml-dtypes: Apache Software License ( Apache License Version 2
mtcnn: MIT
namex: licensed under the Apache License, Version 2.0 (the "License");
numpy: BSD License (Copyright (c) 2005-2024
opencv-contrib-python: Apache Software License (Apache 2
opencv-python: Apache Software License (Apache 2
opt-einsum: OSI Approved (MIT)
optree: Apache Software License (Apache License
packaging: Apache Software License
pandas: BSD License (BSD 3-Clause License  Copyright (c) 2008-2011
pillow: Historical Permission Notice and Disclaimer (HPND) (HPND)
protobuf: 3-Clause BSD License
pycparser: BSD License (BSD-3-Clause)
Pygments: BSD License (BSD-2-Clause)
pyparsing: MIT License
PySocks: BSD
python-dateutil: Apache Software License
pytz: MIT License (MIT)
requests: Apache Software License (Apache-2
retina-face: MIT License
rich: MIT License (MIT)
scipy: BSD License (Copyright (c) 2001-2002 Enthought
six: MIT License (MIT)
sounddevice: MIT License (MIT)
soupsieve: MIT License
tensorboard: Apache Software License (Apache 2
tensorboard-data-server: Apache Software License (Apache 2
tensorflow: Apache Software License (Apache 2
tensorflow-intel: Apache Software License (Apache 2
tensorflow-io-gcs-filesystem: Apache Software License
termcolor: MIT License (MIT)
tf_keras: Apache Software License (Apache 2
tqdm: MIT License
typing_extensions: Python Software Foundation License
tzdata: Apache Software License (Apache-2
urllib3: MIT License
Werkzeug: BSD License
wrapt: BSD License (BSD)
colorama: BSD License
contourpy: BSD License (BSD 3-Clause License  Copyright (c) 2021-2024
cycler: BSD License (Copyright (c) 2015
