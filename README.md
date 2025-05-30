
<!-- Anchor to the Top -->
<a name="readme-top"></a>




<h3 align="center">Sentimental Analyser for Discor messages</h3>

  <p align="center"> 
    <br />
   
  </p>
</div>



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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Discord bot performing sentiment analysis on messages and labeling them into 28 different categories and storing the results using Mongo-DB.



<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Remove any of these if they dont match your project, or add more if you need to.

* Tensorflow
* Disnake
* Transformers
* PyMongo
* python-dotenv

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Docker

### Installation

1. Creat a free discord bot [Discord developers portal](https://discord.com/developers/applications) to get a bot token
2. Invite you new bot with admin permissions in your discord server
3. Clone the repo
   ```sh
   git clone https://github.com/vannsoko/SentimentalAnalyserBot.git
   ```
4. Renaming .env.exemple to .env
5. Enter the needed env variables
   ```dotenv
    BOT_TOKEN="EXAMPLE TOKEN REPLACE IN YOUR OWN ENV FILE"
    CHANNEL_ID="EXAMPLE CHANNEL ID REPLACE IN YOUR OWN ENV FILE" Ex: "123,456,678"

    MongoDBurl="EXEMPLE mongodb://localhost:27017/"
    DATABASE_NAME="EXAMPLE DATABASE NAME REPLACE IN YOUR OWN ENV FILE"
    COLLECTION_NAME="EXAMPLE COLLECTION NAME REPLACE IN YOUR OWN ENV FILE"
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

1. Find an issue or create one your self. If you have create the issue please make sure that it is relevant to the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`). Please use the name of the issue in the branch name. or reference the issue id in the name.
3. Do your changes and commit them (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request and wait for it to be merged

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->



