# Run the neural search over start-ups 💡
*A gif with a demo speaks louder than a thousand words:*

![Demo](assets/demo.gif)


 *A TABLE OF CONTENTS *
 
- [Overview](#overview)
- [🐍 Build the app with Python](#-build-the-app-with-python)
- [🔮 About Me](#-about-me)
- [🔨 Next steps, building your own app](#-next-steps-building-your-own-app)
- [🙍 Community](#-community)
- [🦄 License](#-license)


## Overview
Having recently visited Web Summit, I have realized how many brilliant ideas there are in the world and how much the proper search over them is necessary. However, simple Google search over start-up description using partial descriptions of start-up specializations might be not very successful. That's where neural search might be handy.

| About this app: |  |
| ------------- | ------------- |
| Learnings | 1) Doing first neural search and even NLP-related solution 2) After [FineTuner event](https://www.google.com/url?q=https://www.meetup.com/jina-community-meetup/events/279857954&sa=D&source=calendar&usd=2&usg=AOvVaw0IcJx4z1GNZyoQuwPYcyhy) applying better and faster tuning strategies|
| Dataset used | *[Link to Start-Up dataset](https://storage.googleapis.com/generall-shared-data/startups_demo.json)* |
| Model used | *[Link to Sentence-Transformers model](https://www.sbert.net/)* |


## 🐍 Build the app with Python

These instructions explain how to build the app and deploy it with Python.   


### 🗝️ Requirements

*It is recommended to consider several points before diving in using the Startup Search app such as following:* 

1. You have a working Python 3.8 environment. 
2. We recommend creating a [new Python virtual environment](https://docs.python.org/3/tutorial/venv.html) to have a clean installation of Jina and prevent dependency conflicts.   
3. You have at least 2GB of free space on your hard drive. 

### 👾 Step 1. Clone the repo and install Jina

Begin by cloning the repo, so you can get the required files and datasets. (If you already have this repository on your machine make sure to fetch the most recent version)

```sh
git clone https://github.com/EliaLesyk/startup-search.git
````

And enter the correct folder:

```sh
cd startup-search
```

In your terminal, you should now be located in you the *startup-search* folder. Let's install Jina and the other required Python libraries. For further information on installing Jina check out [our documentation](https://docs.jina.ai/chapters/core/setup/).

```sh
pip install -r requirements.txt
```

### 📥 Step 2. Download your data to search (Optional)

You can use bash script for getting the data. There are some default settings set to ensure that the file will be downloaded from the link and converted to the necessary format.

**Bash script:** 
   - Run `sh get_data.sh`.

### 🏃 Step 3. Index your data
In this step, we will index our data. For this step you can use this command:
```
python app.py --index
```
*It is also possible to run indexing over the small part to come to the result faster:*

`python app.py --index --n 10`

If you see the following output, it means your data has been correctly indexed.

```
Flow@5162[S]:flow is closed and all resources are released, current build level is 0
```

### 🔎 Step 4: Query your data
Next, we will deploy our query Flow. We're doing it in the interface from Streamlit that will be automatically opened in your default browser. 

1. Open a new terminal without closing the one with Indexing.
2. Run the query Flow in your terminal like this:
```
streamlit run run.py
``` 
### 🚀 Step 5: Check the results
Now you should see the web interface where you can:
- type the keywords that will be used for neaural search over the descriptions of start-ups
- give feedback to the system with "Mark as Relevant" and "Mark as Irrelevant", thus, changing the parameters of the system and receiving more relevant results.
______

## 📖 References

Embracing the power of open source, I have used the following websites to build the neural search over start-ups:
- [Source of code inspiration](https://github.com/fissoreg/papers-search) - the showcase solution with Jina for the search over scientific articles from arXiv.
- [Source of data](https://qdrant.tech/articles/neural-search-tutorial/#) - the article describing the usage of neural search for quering start-up data.
- [Source of model](https://github.com/allenai/specter) - the model called SPECTER: Document-level Representation Learning using Citation-informed Transformers.

## 🔮 About Me

![Official Photo](assets/photo.jpeg)

I'm currently Master Student in Friedrich-Alexander University of Erlangen-Nuremberg. My Master Programme is International Information Systems with majors in Business Analytics, Machine Learning and Business Intelligence. 
- [E-Mail](mailto:elina.lesyk@gmail.com)

My work is in the area of digital health for radiology at Siemens Healthineers. We're building the validated prototypes helping doctors cure cancer.
- [Linkedin with more details on past and current experience](https://www.linkedin.com/in/elina-lesyk/)

The ongoing research I undertake is in the area of speech emotion recognition applying deep learning and transfer knowledge methods for children and adult speech data.
- [GitHub with more description about my research](https://github.com/EliaLesyk)


_____
## ⏭️ Next steps

1) The next version of the app might include the filter over cities where start-ups are located.
2) Dealing with Docker on MacOS with M1 Chip is still the problematic issue. It needs more time to be solved to be deployed for this app.

## 👩‍👩‍👧‍👦 Jina Community

- [Slack channel](https://slack.jina.ai/) - a communication platform for developers to discuss Jina.
- [LinkedIn](https://www.linkedin.com/company/jinaai/) - get to know Jina AI as a company and find job opportunities.
- [![Twitter Follow](https://img.shields.io/twitter/follow/JinaAI_?label=Follow%20%40JinaAI_&style=social)](https://twitter.com/JinaAI_) - follow us and interact with us using hashtag `#JinaSearch`.  
- [Company](https://jina.ai) - know more about our company, we are fully committed to open-source!

## 🦄 License

Copyright (c) 2021 Jina AI Limited. All rights reserved.

Jina is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/jina-ai/examples/blob/master/LICENSE) for the full license text.
