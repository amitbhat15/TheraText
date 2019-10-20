from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

train_data = load_data("rasa_dataset.json")
trainer = Trainer(config.load("config_spacy.yaml"))

#Training Data
trainer.train(train_data)

model_directory = trainer.persist("/Users/advaitmarathe/Documents/GitHub/TheraText")
