﻿# Rasa Stack starter-pack + Dash boilerplate app

This starter-pack is a combination of Rasa official start pack: https://github.com/RasaHQ/starter-pack-rasa-stack and a simple Dash app from https://adamspannbauer.github.io/2018/03/15/building-a-rasa-chatbot/


<p align="center">
  <img src="./rasa-stack-mockup.gif">
</p>


## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt
```

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```

### Files for training the Rasa NLU model

- **data/nlu_data.json** file contains training examples of six intents: 
	- greet
	- goodbye
	- thanks
	- deny
	- joke
	- name (examples of this intent contain an entity called 'name')
	
- **nlu_config.yml** file contains the configuration of the Rasa NLU pipeline:  
```text
language: "en"

pipeline: spacy_sklearn
```	

### Files for training the Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action which retrieves a Chuck Norris joke by making an external API call.
- **endpoints.yml** file contains the webhook configuration for custom action.
- **dash_demo_app.py** file contains the Dash app

## How to use this starter-pack?
1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. Start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the Dash assistant by running:  
```python dash_demo_app.py```  
This will load the assistant in a Dash server for you to chat.

